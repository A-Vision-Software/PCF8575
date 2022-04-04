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

# Get all (16) PCF inputs
print(PCF.port)

# Set bit/output 0 to HIGH
PCF.port[0] = True

while True:
    # flashing bit/output 0
	PCF.port[0] = False
	sleep(0.1)
	PCF.port[0] = True
	sleep(0.1)
