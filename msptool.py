#  Copyright (c) 2021 Upside Down Labs
#  Author: Deepak Khatri <myupsidedownlab@gmail.com>
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import serial
import argparse

# Argument parsing
help = {"port": "USB-UART bridge port, Windows: COM#, Linux: /dev/tty#",
        "firmware": "TI-TXT format firmware image from msp430-gcc/CCS"}
parser = argparse.ArgumentParser()
parser.add_argument('-p', '--port', required=True, type = str, help=help["port"])
parser.add_argument('-f', '--firmware', required=True, type=argparse.FileType('r'), help=help["firmware"])
args = parser.parse_args()

# Extract info from parsed arguments
comPort = args.port
firmwareImage = args.firmware.name

# Method to Reset connected MSP430
def reset():
    '''Generate reset signal on DTR pin of USB-UART bridge'''
    bridge = serial.Serial(comPort, 9600)
    print("Resetting...")
    bridge.dtr = 0
    bridge.dtr = 1
    bridge.close()

# Get the OS specific command to execute
if os.name == 'nt':
    '''OS is Windows'''
    #command = "rom-bsl.exe -c" + str.upper(comPort) + " -m1 -ievpr " + firmwareImage
    command = ".\mspdebug\mspdebug.exe rom-bsl -d " + comPort + " \"prog " + firmwareImage + "\""
else:
    '''OS is Linux'''
    command = "./mspdebug/mspdebug rom-bsl -d " + comPort + " \"prog " + firmwareImage + "\""

# Print the command
print("Executing: " + command)
# Execute command
os.system(command)
# Reset chip
reset()

