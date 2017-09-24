__author__ = 'hakon0601'

''' This file enables your Python code to read from a serial port, which you must insure
 is the SAME serial port that your Arduino writes to.

 The 'serial' module is part of the 'pyserial' package, which you can install via
 pip:  'pip3 install pyserial'
'''

import serial


# **** For MACs ******

# arport = Arduino device port, which you can find at the bottom of your arduino window or via Arduino menu options tools/port.
#   The default will probably NOT work for your machine, but it may look quite similar, differing only
#  in the final 4 digits.

def basic_connect(arport='/dev/cu.wchusbserial1410'):
    return serial.Serial(arport, 9600, timeout=.1)