from pymodbus.client import ModbusSerialClient
from pymodbus.exceptions import ModbusException
from PySide6.QtCore import QThread, Signal, QTimer

from controllers.weightReader import WeightAmplifier
from controllers.concreteMixer import ConcreteMixingTask

import time

from PySide6.QtGui import QValidator, QKeyEvent
from PySide6.QtWidgets import QMessageBox
import sys

class FloatValidator(QValidator):
    def validate(self, input_text, pos):
        # Empty input is considered intermediate
        if not input_text:
            return QValidator.Intermediate, input_text, pos

        # Allow a single dot
        if input_text.count('.') > 1:
            return QValidator.Invalid, input_text, pos

        # Check if the input is a valid float
        try:
            float(input_text)
            return QValidator.Acceptable, input_text, pos
        except ValueError:
            # Allow a single leading minus sign
            if input_text == '-' and pos == 1:
                return QValidator.Intermediate, input_text, pos
            # Allow a single dot as intermediate if not already present
            elif input_text == '.' and pos == 1 and '.' not in input_text:
                return QValidator.Intermediate, input_text, pos
            else:
                return QValidator.Invalid, input_text, pos

class MainMixerController:
    def __init__(self, ui, MainWindow, db_conn):
        self.ui = ui
        self.MainWindow = MainWindow
        self.db_conn = db_conn
        
        self.main_state = 0
        self.weight_agg_state = 0
        self.weight_cement_state = 0
        self.weight_water_state = 0
        self.weight_chemical_state = 0
        
        self.coil_status = {'rock1': False, 'sand': False, 'rock2': False, 'flyash': False, 'cement': False, 'water': False, 'chem1': False, 'chem2': False}
        
        self.weight_formula = []
        
        self.weight_client = ModbusSerialClient(
            method='rtu', port='COM11', baudrate=9600,
            bytesize=8, parity='N', stopbits=1, timeout=1
        )

        self.plc_client = ModbusSerialClient(
            method='rtu', port='COM12', baudrate=9600,
            bytesize=8, parity='N', stopbits=1, timeout=1
        )
        # check input in concreteOrder_lineEdit. It should be digit and single dot only
        validator = FloatValidator()
        self.ui.concreteOrder_lineEdit.setValidator(validator)
        # create a thread to read the weight amplifier
        self.weight_reader_thread = WeightAmplifier(self.weight_client)
        self.weight_reader_thread.weight_amplifier1_signal.connect(self.weight_amplifier1)
        self.weight_reader_thread.weight_amplifier2_signal.connect(self.weight_amplifier2)
        self.weight_reader_thread.weight_amplifier3_signal.connect(self.weight_amplifier3)
        self.weight_reader_thread.weight_amplifier4_signal.connect(self.weight_amplifier4)
        self.weight_reader_thread.modbus_error_signal.connect(self.save_error_message)
        
        # create a thread to mix the concrete
        self.concrete_mixer = ConcreteMixingTask(self.plc_client)
        self.concrete_mixer.modbus_error_signal.connect(self.save_error_message)
        self.concrete_mixer.coils_signal.connect(self.update_coil_status)
        
        # Connect signals and slots
        self.ui.startProcess_pushButton.clicked.connect(self.start_process)
        self.ui.terminateProcess_pushButton.clicked.connect(self.terminate_process)
        
        # set default background color for frames
        self.reset_background_color()
        
        # create timer to run main task
        self.main_task_timer = QTimer()
        self.main_task_timer.setInterval(100)
        # Connect the timer's timeout signal to the update_label slot
        self.main_task_timer.timeout.connect(self.run_main_task)
        
        # clear all lcdNumber and input widgets
        self.reset_lcdNumber()
        self.clear_input_widgets()
        
        
    def run_main_task(self):
        if self.main_state == 0:            # idle state
            if self.ui.targetAmount_lcdNumber.value() >= 1:
                self.ui.inProcessAmount_lcdNumber.display(1)
                new_target_amount = float(self.ui.targetAmount_lcdNumber.value() - 1)
                self.ui.targetAmount_lcdNumber.display(new_target_amount)
            elif self.ui.targetAmount_lcdNumber.value() > 0:
                self.ui.inProcessAmount_lcdNumber.display(self.ui.targetAmount_lcdNumber.value())
                self.ui.targetAmount_lcdNumber.display(0)
            else:
                new_target_amount = 0
                # stop run main task
                self.main_task_timer.stop()
            # update material weights
            self.ui.rock1Waiting_lcdNumber.display(int(self.weight_formula[0])*self.ui.inProcessAmount_lcdNumber.value())
            self.ui.sandWaiting_lcdNumber.display(int(self.weight_formula[1])*self.ui.inProcessAmount_lcdNumber.value())
            self.ui.rock2Waiting_lcdNumber.display(int(self.weight_formula[2])*self.ui.inProcessAmount_lcdNumber.value())
            self.ui.cementWaiting_lcdNumber.display(int(self.weight_formula[3])*self.ui.inProcessAmount_lcdNumber.value())
            self.ui.flyashWaiting_lcdNumber.display(int(self.weight_formula[4])*self.ui.inProcessAmount_lcdNumber.value())
            self.ui.waterWaiting_lcdNumber.display(int(self.weight_formula[5])*self.ui.inProcessAmount_lcdNumber.value())
            self.ui.chem1Waiting_lcdNumber.display(float(self.weight_formula[6])*self.ui.inProcessAmount_lcdNumber.value())
            self.ui.chem2Waiting_lcdNumber.display(float(self.weight_formula[7])*self.ui.inProcessAmount_lcdNumber.value())
            
            self.main_state = 1
        elif self.main_state == 1:          # prerunning state
            self.main_state = 2
        elif self.main_state == 2:          # running state
            self.run_agg_task()
            self.run_cement_task()
            self.run_water_task()
            
            if self.weight_agg_state == 3 and self.weight_cement_state == 2 and self.weight_water_state == 3 and self.weight_chemical_state == 3:
                self.main_state =3
        elif self.main_state == 3:          # mixing state
            pass
        else:
            print('Main state is not defined')
        
        
    def run_agg_task(self):
        if self.weight_agg_state == 0:
            # set weight value to Loadcell amplifier1
            weight_list = [1, int(self.ui.rock1Waiting_lcdNumber.value())]
            self.set_upper_weight(weight_list)
            self.weight_agg_state = 1
        elif self.weight_agg_state == 1:
            # set coil to plc to start measuring weight
            self.concrete_mixer.start_measure_rock1()
        elif self.weight_agg_state == 2:
            pass
        elif self.weight_agg_state == 3:
            pass
        elif self.weight_agg_state == 4:
            pass
        else:
            print("error")
        
    def run_cement_task(self):
        if self.weight_cement_state == 0:
            # set weight value to Loadcell amplifier2
            weight_list = [2, int(self.ui.flyashWaiting_lcdNumber.value())]
            self.set_upper_weight(weight_list)
            self.weight_cement_state = 1
        elif self.weight_cement_state == 1:
            if self.coil_status['flyash']:
                self.weight_cement_state = 2
        elif self.weight_cement_state == 2:
            print("Flyash completed")
        else:
            print("Error")
            
    def run_water_task(self):
        if self.weight_water_state == 0:
            pass
        elif self.weight_water_state == 1:
            pass
        elif self.weight_water_state == 2:
            pass
        elif self.weight_water_state == 3:
            pass
        else:
            print("Error")
            
    def run_chemical_task(self):
        if self.weight_chemical_state == 0:
            pass
        elif self.weight_chemical_state == 1:
            pass
        elif self.weight_chemical_state == 2:
            pass
        elif self.weight_chemical_state == 3:
            pass
        else:
            print("error")
        
    def reset_background_color(self):
        self.ui.rock1_frame.setStyleSheet("background-color: #babdbf")
        self.ui.sand_frame.setStyleSheet("background-color: #babdbf")
        self.ui.rock2_frame.setStyleSheet("background-color: #babdbf")
        self.ui.cement_frame.setStyleSheet("background-color: #babdbf")
        self.ui.flyash_frame.setStyleSheet("background-color: #babdbf")
        self.ui.water_frame.setStyleSheet("background-color: #babdbf")
        self.ui.chem1_frame.setStyleSheet("background-color: #babdbf")
        self.ui.chem2_frame.setStyleSheet("background-color: #babdbf")
        
        self.ui.mixer_frame.setStyleSheet("background-color: #babdbf")
        self.ui.conveyor_frame.setStyleSheet("background-color: #babdbf")
        self.ui.mixerValve_frame.setStyleSheet("background-color: #babdbf")
        
        self.ui.cementValve_frame.setStyleSheet("background-color: #babdbf")
        self.ui.waterValve_frame.setStyleSheet("background-color: #babdbf")
        self.ui.chemValve_frame.setStyleSheet("background-color: #babdbf")

    def active_background_color(self, frame_name):
        if frame_name == 'rock1':
            self.ui.rock1_frame.setStyleSheet("background-color: #42b6f5")
        elif frame_name == 'sand':
            self.ui.sand_frame.setStyleSheet("background-color: #42b6f5")
        elif frame_name == 'rock2':
            self.ui.rock2_frame.setStyleSheet("background-color: #42b6f5")
        elif frame_name == 'cement':
            self.ui.cement_frame.setStyleSheet("background-color: #42b6f5")
        elif frame_name == 'flyash':
            self.ui.flyash_frame.setStyleSheet("background-color: #42b6f5")
        elif frame_name == 'water':
            self.ui.water_frame.setStyleSheet("background-color: #42b6f5")
        elif frame_name == 'chem1':
            self.ui.chem1_frame.setStyleSheet("background-color: #42b6f5")
        elif frame_name == 'chem2':
            self.ui.chem2_frame.setStyleSheet("background-color: #42b6f5")
        elif frame_name == 'mixer':
            self.ui.mixer_frame.setStyleSheet("background-color: #42b6f5")
        elif frame_name == 'conveyor':
            self.ui.conveyor_frame.setStyleSheet("background-color: #42b6f5")
        elif frame_name == 'mixerValve':
            self.ui.mixerValve_frame.setStyleSheet("background-color: #42b6f5")
        elif frame_name == 'cementValve':
            self.ui.cementValve_frame.setStyleSheet("background-color: #42b6f5")
        elif frame_name == 'waterValve':
            self.ui.waterValve_frame.setStyleSheet("background-color: #42b6f5")
        elif frame_name == 'chemValve':
            self.ui.chemValve_frame.setStyleSheet("background-color: #42b6f5")
        else:
            pass
        
    def set_upper_weight(self, weight_list):
        # weight_list = [weight_id, weight_value]
        self.weight_reader_thread.set_upper_weight([weight_list])
        
    def set_lower_weight(self, weight_list):
        # weight_list = [weight_id, weight_value]
        self.weight_reader_thread.set_lower_weight([weight_list])
        
    def start_process(self):
        if self.ui.concreteOrder_lineEdit.text() == "":
            QMessageBox.critical(self.MainWindow, "Error", "กรุณาระบุปริมาณคอนกรีตที่ต้องการผสม")
            return
        self.main_state = 0     # reset main state
        # disable input widgets
        self.disable_input_widgets()
        
        # save values and read database
        # read formula from database
        sql_query = "SELECT rock1,sand,rock2,cement,flyash,water,chem1,chem2 FROM concrete_formula WHERE name = ?"
        db_cursor = self.db_conn.cursor()
        db_cursor.execute(sql_query, (self.ui.concreteFormula_comboBox.currentText(),))
        result = db_cursor.fetchone()
        self.weight_formula = list(result)
        # load target amount to lcdNumber
        self.ui.targetAmount_lcdNumber.display(self.ui.concreteOrder_lineEdit.text())
                
        # check rs485 connection to weight amplifier
        if not self.weight_client.is_socket_open():
            self.weight_client.connect()
        self.ui.startProcess_pushButton.setEnabled(False)
        self.weight_reader_thread.start()
        self.main_task_timer.start()

    def terminate_process(self):
        # terminate the process
        if self.weight_reader_thread:
            self.weight_reader_thread.stop()  # Stop the thread
            self.weight_reader_thread.wait()  # Wait for the thread to finish
        # stop timer if running
        if self.main_task_timer.isActive():
            self.main_task_timer.stop()
        # reset main state
        self.main_state = 0
        # reset background color
        self.reset_background_color()
        # clear all lcdNumber
        self.reset_lcdNumber()
        # enable start button and input widgets
        self.ui.startProcess_pushButton.setEnabled(True)
        
        # clear input widgets and enable input widgets
        self.clear_input_widgets()
        self.enable_input_widgets()
            
    def save_error_message(self, error_message):
        # this function will save the error message to the database
        print(error_message)

    def weight_amplifier1(self, weight):
        # print(weight)
        pass
        
    def weight_amplifier2(self, weight):
        # print(weight)
        pass
        
    def weight_amplifier3(self, weight):
        # self.ui.waterValue_lcdNumber.display(weight)
        pass
    
    def weight_amplifier4(self, weight):
        # print(weight)
        pass

    def disable_input_widgets(self):
        self.ui.customerName_lineEdit.setEnabled(False)
        self.ui.phoneNumber_lineEdit.setEnabled(False)
        self.ui.address_plainTextEdit.setEnabled(False)
        
        self.ui.concreteFormula_comboBox.setEnabled(False)
        self.ui.concreteOrder_lineEdit.setEnabled(False)
        
        self.ui.keepSample_radioButton.setEnabled(False)
        self.ui.noKeepSample_radioButton.setEnabled(False)
        
        self.ui.truckID_lineEdit.setEnabled(False)
        self.ui.comment_plainTextEdit.setEnabled(False)
        
    def enable_input_widgets(self):
        self.ui.customerName_lineEdit.setEnabled(True)
        self.ui.phoneNumber_lineEdit.setEnabled(True)
        self.ui.address_plainTextEdit.setEnabled(True)
        
        self.ui.concreteFormula_comboBox.setEnabled(True)
        self.ui.concreteOrder_lineEdit.setEnabled(True)
        
        self.ui.keepSample_radioButton.setEnabled(True)
        self.ui.noKeepSample_radioButton.setEnabled(True)
        
        self.ui.truckID_lineEdit.setEnabled(True)
        self.ui.comment_plainTextEdit.setEnabled(True)        
        
    def closeEvent(self,event):
        try:
            self.weight_reader_thread.stop()
            self.weight_reader_thread.wait()
        except:
            pass
        
        try:
            if self.weight_client.is_socket_open():
                self.weight_client.close()
            # stop plc client
            if self.plc_client.is_socket_open():
                self.plc_client.close()
        except:
            pass
        
        # close database connection and windows
        try:
            self.db_conn.close()
            self.MainWindow.close()
        except:
            pass
        event.accept()
        
    def clear_input_widgets(self):
        self.ui.customerName_lineEdit.clear()
        self.ui.phoneNumber_lineEdit.clear()
        self.ui.address_plainTextEdit.clear()
        
        self.ui.concreteFormula_comboBox.setCurrentIndex(0)
        self.ui.concreteOrder_lineEdit.clear()
        
        self.ui.keepSample_radioButton.setChecked(True)
        self.ui.noKeepSample_radioButton.setChecked(False)
        
        self.ui.truckID_lineEdit.clear()
        self.ui.comment_plainTextEdit.clear()
        
    def reset_lcdNumber(self):
        #  reset all lcdNumber in waiting frame
        self.ui.rock1Waiting_lcdNumber.display(0)
        self.ui.sandWaiting_lcdNumber.display(0)
        self.ui.rock2Waiting_lcdNumber.display(0)
        self.ui.cementWaiting_lcdNumber.display(0)
        self.ui.flyashWaiting_lcdNumber.display(0)
        self.ui.waterWaiting_lcdNumber.display(0)
        self.ui.chem1Waiting_lcdNumber.display(0)
        self.ui.chem2Waiting_lcdNumber.display(0)
        # reset all lcdNumber in value frame
        self.ui.rock1Finish_lcdNumber.display(0)
        self.ui.sandFinish_lcdNumber.display(0)
        self.ui.rock2Finish_lcdNumber.display(0)
        self.ui.cementFinish_lcdNumber.display(0)
        self.ui.flyashFinish_lcdNumber.display(0)
        self.ui.waterFinish_lcdNumber.display(0)
        self.ui.chem1Finish_lcdNumber.display(0)
        self.ui.chem2Finish_lcdNumber.display(0)
        
        self.ui.rock1Target_lcdNumber.display(0)
        self.ui.sandTarget_lcdNumber.display(0)
        self.ui.rock2Target_lcdNumber.display(0)
        self.ui.cementTarget_lcdNumber.display(0)
        self.ui.flyashTarget_lcdNumber.display(0)
        self.ui.waterTarget_lcdNumber.display(0)
        self.ui.chem1Target_lcdNumber.display(0)
        self.ui.chem2Target_lcdNumber.display(0)
        
        self.ui.rock1Value_lcdNumber.display(0)
        self.ui.sandValue_lcdNumber.display(0)
        self.ui.rock2Value_lcdNumber.display(0)
        self.ui.cementValue_lcdNumber.display(0)
        self.ui.flyashValue_lcdNumber.display(0)
        self.ui.waterValue_lcdNumber.display(0)
        self.ui.chem1Value_lcdNumber.display(0)
        self.ui.chem2Value_lcdNumber.display(0)
        
        self.ui.targetAmount_lcdNumber.display(0)
        self.ui.inProcessAmount_lcdNumber.display(0)
        self.ui.finishAmount_lcdNumber.display(0)
        
        
    def update_coil_status(self, coil_status):
        self.coil_status = coil_status
        print(self.coil_status)        
        