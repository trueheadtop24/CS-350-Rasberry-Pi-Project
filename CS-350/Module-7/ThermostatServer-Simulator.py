#
# ThermostatServer-Simulator.py - This is the Python code that will be used
# to simulate the Thermostat Server. It will read the data that the
# thermostat is sending to the server over the serial port and print it 
# to the screen. 
#
# This script will loop until the user interrupts the program by 
# pressing CTRL-C
#
#------------------------------------------------------------------
# Change History
#------------------------------------------------------------------
# Version   |   Description
#------------------------------------------------------------------
#    1          Initial Development
#------------------------------------------------------------------

# Load the time module so that we can utilize the sleep method to 
# inject a pause into our operation
#!/usr/bin/env python3

#!/usr/bin/env python3

# This lets the program use a clock and take short naps.
# -------------------------
# DEFAULTS
# -------------------------
# ThermostatServer-Simulator.py
# Simulates the thermostat server and displays incoming serial data

import time
import serial

ser = serial.Serial(
        port='/dev/ttyUSB0',
        baudrate=115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

repeat = True

while repeat:
    try:
        # Read serial line
        dataline = (ser.readline().decode("utf-8")).strip().lower()

        if len(dataline) > 1:

            # Expecting format:
            # state,setpoint,current_temp

            fields = dataline.split(",")

            if len(fields) == 3:

                state = fields[0]
                setpoint = fields[1]
                current_temp = fields[2]

                print("------------------------------------------------")
                print("Thermostat Update Received")
                print("State:        ", state)
                print("Setpoint:     ", setpoint + " F")
                print("Current Temp: ", current_temp + " F")
                print("------------------------------------------------")

            else:
                print("Invalid data format:", dataline)

    except KeyboardInterrupt:
        repeat = False
        print("\nServer shutting down cleanly.")