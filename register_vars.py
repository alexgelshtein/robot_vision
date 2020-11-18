import sys 
import time
from detection import detect
sys.path.append('C:\\Users\\laser\\Documents\\VSCode projects\\ur-interface')
import URBasic

host = "169.254.54.9"

urModel = URBasic.robotModel.RobotModel()
robot = URBasic.urScriptExt.UrScriptExt(host=host, robotModel=urModel)
robot.reset_error()

rob = URBasic.dashboard.DashBoard(urModel)
rob.ur_play()

# Wait for register_0 to get True
register = urModel.OutputBitRegister()[0]
while register == False:
  register = urModel.OutputBitRegister()[0]
rob.ur_pause()
time.sleep(0.08)

print("Starting Detection")
detect(0)

rob.ur_play()
time.sleep(0.08)
rob.close()
robot.close()