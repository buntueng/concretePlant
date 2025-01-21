from pymodbus.client import ModbusSerialClient
from pymodbus.exceptions import ModbusException
from PySide6.QtCore import QThread, Signal, QTimer
import time


class ConcreteMixingTask(QThread):
    modbus_error_signal = Signal(str)  # Emit a string for error message
    coils_signal = Signal(dict)  # Emit a string for coil status
    
    def __init__(self, plc_client):
        super().__init__()
        self.plc_client = plc_client
        if not self.plc_client.connect():
            self.modbus_error_signal.emit("Failed to connect to the PLC")
            print("Failed to connect to the PLC")
        else:
            print("Connected to the PLC")
        
        self.plc_cmd_list = []
        self.slave_id = 1
        self._isRunning = True
        self.end_thread_loop = False
        self.coil_status = {'rock1': False, 'sand': False, 'rock2': False, 'flyash': False, 'cement': False, 'water': False, 'chem1': False, 'chem2': False}
        
    def run(self):
        # prepare something
        self.looping()
        
    def start_measure_rock1(self):
        # Write weight data
        self.plc_cmd_list.append([1, 20])

    def looping(self):
        while self._isRunning:
            self.end_thread_loop = False
            try:
                # Ensure the client is connected
                if not self.plc_client.is_socket_open():
                    if not self.plc_client.connect():
                        self.modbus_error_signal.emit("Failed to reconnect to the weight amplifier")
                        print("Failed to reconnect to the weight amplifier")
                        time.sleep(1)
                        continue
                # run state in rock and sand preparation
                if len(self.plc_cmd_list) > 0:
                    cmd_list = self.plc_cmd_list.pop(0)
                    # Write weight data
                    response = self.plc_client.write_coils(address=cmd_list[0], value=cmd_list[1], unit=self.slave_id)
                    time.sleep(0.01)  # Wait for 0.1 second
                    if response.isError():
                        self.modbus_error_signal.emit(f"Error start writing coils address{cmd_list[0]} value {cmd_list[1]}: {response}")
                # read coil status
                self.read_process_status()
                self.coils_signal.emit(self.coil_status)
            except Exception as e:
                self.modbus_error_signal.emit(f"Modbus communication error: {e}")
                print(f"Modbus communication error: {e}")
            self.end_thread_loop = True
            time.sleep(0.5)  # Wait for 1 second
            
    def stop(self):
        self._isRunning = False
        if self.end_thread_loop:
            if self.plc_client.is_socket_open():
                self.plc_client.close()
        else:
            QTimer.singleShot(50, self.stop)
            
            
    def read_process_status(self):
        try:
            # ================= read rcok1 measuring state =================
            response = self.plc_client.read_coils(address=21, count=1, unit=self.slave_id)
            time.sleep(0.01)  # Wait for 0.1 second
            if response.isError():
                self.modbus_error_signal.emit(f"Error reading rock1 measuring state: {response}")
            else:
                self.coil_status['rock1'] = response.bits[0]
                
            # ================= read sand measuring state =================
            response = self.plc_client.read_coils(address=31, count=1, unit=self.slave_id)
            time.sleep(0.01)  # Wait for 0.1 second
            if response.isError():
                self.modbus_error_signal.emit(f"Error reading sand measuring state: {response}")
            else:
                self.coil_status['sand'] = response.bits[0]
            
            # ================= read rock2 measuring state =================
            response = self.plc_client.read_coils(address=41, count=1, unit=self.slave_id)
            time.sleep(0.01)  # Wait for 0.1 second
            if response.isError():
                self.modbus_error_signal.emit(f"Error reading rock2 measuring state: {response}")
            else:
                self.coil_status['rock2'] = response.bits[0]

            # ================= read flyash measuring state =================
            response = self.plc_client.read_coils(address=51, count=1, unit=self.slave_id)
            time.sleep(0.01)  # Wait for 0.1 second
            if response.isError():
                self.modbus_error_signal.emit(f"Error reading flyash measuring state: {response}")
            else:
                self.coil_status['flyash'] = response.bits[0]
                
            # ================= read cement measuring state =================
            response = self.plc_client.read_coils(address=61, count=1, unit=self.slave_id)
            time.sleep(0.01)  # Wait for 0.1 second
            if response.isError():
                self.modbus_error_signal.emit(f"Error reading cement measuring state: {response}")
            else:
                self.coil_status['cement'] = response.bits[0]
                
            # ================= read water measuring state =================
            response = self.plc_client.read_coils(address=71, count=1, unit=self.slave_id)
            time.sleep(0.01)  # Wait for 0.1 second
            if response.isError():
                self.modbus_error_signal.emit(f"Error reading water measuring state: {response}")
            else:
                self.coil_status['water'] = response.bits[0]
                
            # ================= read chem1 measuring state =================
            response = self.plc_client.read_coils(address=81, count=1, unit=self.slave_id)
            time.sleep(0.01)  # Wait for 0.1 second
            if response.isError():
                self.modbus_error_signal.emit(f"Error reading chem1 measuring state: {response}")
            else:
                self.coil_status['chem1'] = response.bits[0]
                
            # ================= read chem2 measuring state =================
            response = self.plc_client.read_coils(address=91, count=1, unit=self.slave_id)
            time.sleep(0.01)  # Wait for 0.1 second
            if response.isError():
                self.modbus_error_signal.emit(f"Error reading chem2 measuring state: {response}")
            else:
                self.coil_status['chem2'] = response.bits[0]
                
        except:
            self.modbus_error_signal.emit(f"Error reading process status")