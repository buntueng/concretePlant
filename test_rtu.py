from pymodbus.client import ModbusSerialClient
from pymodbus.exceptions import ModbusException

def read_holding_registers(com_port, slave_id, start_address, count):
    # Initialize the Modbus RTU client
    client = ModbusSerialClient(
        method="rtu",
        port=com_port,
        baudrate=9600,       # Replace with your device's baud rate
        timeout=1,           # Timeout in seconds
        stopbits=1,
        bytesize=8,
        parity='N'
    )

    # Connect to the Modbus RTU server
    if not client.connect():
        print("Unable to connect to the Modbus device.")
        return None

    try:
        # Read holding registers
        response = client.read_holding_registers(
            address=start_address,  # Starting address of the registers
            count=count,            # Number of registers to read
            slave=slave_id          # Slave ID of the Modbus device
        )
        
        if response.isError():  # Check if there was an error
            print(f"Error reading registers: {response}")
            return None

        # Return the values as a list
        return response.registers
    except ModbusException as e:
        print(f"Modbus exception occurred: {e}")
        return None
    finally:
        # Close the client connection
        client.close()

# Example usage
if __name__ == "__main__":
    com_port = "COM11"         # Replace with your COM port
    slave_id = 1              # Replace with your device's slave ID
    start_address = 0         # Replace with your start address
    count = 10                # Number of registers to read

    registers = read_holding_registers(com_port, slave_id, start_address, count)
    if registers:
        print(f"Holding Registers: {registers}")
    else:
        print("Failed to read registers.")
