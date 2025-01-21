import time
from PySide6.QtCore import QThread, Signal, QTimer
from pymodbus.client import ModbusSerialClient
from pymodbus.exceptions import ModbusException

class WeightAmplifier(QThread):
    weight_amplifier1_signal = Signal(float)  # Emit a float for weight
    weight_amplifier2_signal = Signal(float)  # Emit a float for weight
    weight_amplifier3_signal = Signal(float)  # Emit a float for weight
    weight_amplifier4_signal = Signal(float)  # Emit a float for weight
    modbus_error_signal = Signal(str)  # Emit a string for error message

    def __init__(self, modbus_client):
        super().__init__()  # Call the parent constructor
        self.weight_client = modbus_client
        if not self.weight_client.connect():
            self.modbus_error_signal.emit("Failed to connect to the weight amplifier")
            print("Failed to connect to the weight amplifier")
        else:
            print("Connected to the weight amplifier")
        
        self._isRunning = True
        # save the client list as [slave_id, register_address]
        self.weight_client_list = [[1,80],[2,80],[3,80],[4,80]]
        
        self.upper_weight_list = []
        self.lower_weight_list = []
        self.end_thread_loop = False
        
    def set_upper_weight(self, weight_list):
        # weight_list = [weight_id, weight_value]
        self.upper_weight_list = weight_list
    
    def set_lower_weight(self, weight_list):
        # weight_list = [weight_id, weight_value]
        self.lower_weight_list = weight_list

    def run(self):
        # prepare something
        self._isRunning = True
        self.looping()

    
    def looping(self):
        while self._isRunning:
            self.end_thread_loop = False
            try:
                # Ensure the client is connected
                if not self.weight_client.is_socket_open():
                    if not self.weight_client.connect():
                        self.modbus_error_signal.emit("Failed to reconnect to the weight amplifier")
                        print("Failed to reconnect to the weight amplifier")
                        time.sleep(1)
                        continue
                # # if lower weight list is not empty, write the set weight to the weight amplifier
                # if len(self.lower_weight_list) > 0:
                #     client_list = self.lower_weight_list.pop(0)
                #     # Write weight data
                #     response = self.weight_client.write_register(address=301, value=client_list[1], unit=client_list[0])
                #     time.sleep(0.01)  # Wait for 0.1 second
                #     # Check for errors in the response
                #     if response.isError():
                #         self.modbus_error_signal.emit(f"Error writing weight id= {client_list[0]}, value = {client_list[1]}: {response}")
                            
                # if upper weight list is not empty, write the set weight to the weight amplifier
                if len(self.upper_weight_list) > 0:
                    client_list = self.upper_weight_list.pop(0)                    
                    # Write weight data
                    response = self.weight_client.write_register(address=330, value=client_list[1], unit=client_list[0])
                    time.sleep(0.01)  # Wait for 0.1 second
                    # Check for errors in the response
                    if response.isError():
                        self.modbus_error_signal.emit(f"Error writing weight id= {client_list[0]}, value = {client_list[1]}: {response}")
                        
                # read the weight data from the weight amplifier
                weight_list = []
                for client_list in self.weight_client_list:
                    # Read weight data
                    response = self.weight_client.read_holding_registers(address=client_list[1], count=1, slave=client_list[0])
                    time.sleep(0.01)  # Wait for 0.1 second
                    # Check for errors in the response
                    if response.isError():
                        self.modbus_error_signal.emit(f"Error reading weight: {response}")
                    else:
                        weight = response.registers[0]
                        weight_list.append(weight)
                
                if len(weight_list) == 4:
                    self.weight_amplifier1_signal.emit(weight_list[0])
                    self.weight_amplifier2_signal.emit(weight_list[1])
                    self.weight_amplifier3_signal.emit(weight_list[2])
                    self.weight_amplifier4_signal.emit(weight_list[3])

            except Exception as e:
                self.modbus_error_signal.emit(f"Modbus communication in Weight controller error: {e}")

            self.end_thread_loop = True
            time.sleep(0.5)  # Wait for 1 second
            
    def stop(self):
        self._isRunning = False
        if self.end_thread_loop:
            if self.weight_client.is_socket_open():
                self.weight_client.close()
        else:
            QTimer.singleShot(50, self.stop)
