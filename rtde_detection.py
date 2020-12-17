"""
Easier version of main.py program.
It uses RT connection and output_register to start and stop
detection. This provides faster evaluation and less code
in the UR Polyscope.
"""

import socket
import time
import sys
sys.path.append('..\\ur-interface')
import URBasic
# FIXME: unresolved import (haven't solved this problem yet).
from detection import detect

HOST = '169.254.54.9'
PORT = 29999
PORT_30003 = 30003

urModel = URBasic.robotModel.RobotModel()
robot = URBasic.urScriptExt.UrScriptExt(host=HOST, robotModel=urModel)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(10)
s.connect((HOST, PORT))
print('Starting UR program...\n')
time.sleep(0.08)

# Starting program with dashboard.
s.send('play\n'.encode())
time.sleep(0.08)

# Checks if the program is running.
s.send('running\n'.encode())
# FIXME: timeout might not work sometimes, so that program halts.
time.sleep(0.6)
data = s.recv(4096).decode().split()[-1]

# Secondary program to change register value from 111 to 400.
secondary = """sec secondaryProgram():
write_output_integer_register(0, 400)
end"""

while data == 'true':
  reg = urModel.OutputIntRegister0()
  if reg == 111:
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.settimeout(10)
    soc.connect((HOST, PORT_30003))
    time.sleep(0.08)
    print('Starting detection')
    detect(0)
    soc.send(f'{secondary}\n'.encode())
    time.sleep(0.08)
    soc.close()
  s.send('running\n'.encode())
  time.sleep(0.08)
  data = s.recv(4096).decode().split()[-1]
  time.sleep(0.08)

s.close()
robot.close()