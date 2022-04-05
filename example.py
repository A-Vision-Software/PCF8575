#/*******************************************************************************
#*
#* File description :        PCF8575 IO expander chip python example
#*
#* Created by       :        Arnold Velzel
#* Created on       :        04-04-2022
#*
#*******************************************************************************/
from time import sleep

from pcf8575 import PCF8575

# initialise I/O expander
PCF = PCF8575(1, 0x20)
# set all inouts HIGH
PCF.port = [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True]
# set all inouts LOW
PCF.port = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]

# Read all (16) PCF inputs
print(PCF.port)
# Read PCF input P14
print(PCF.port[12])

# Set bit/output P00 to HIGH
PCF.port[0] = True

# fill/unfill bits/outputs
while True:
    for i in range(8):
        PCF.port[i] = True  # Set output P00..P07 HIGH

        for i in range(8, 12):
            PCF.port[i] = PCF.port[i+4] # Read input P14..P17 and Set output P10..P13

        sleep(0.1)

    for i in range(7, 0, -1):
        PCF.port[i] = False  # Set output P00..P07 LOW

        for i in range(8, 12):
            PCF.port[i] = PCF.port[i+4] # Read input P14..P17 and Set output P10..P13

        sleep(0.1)
