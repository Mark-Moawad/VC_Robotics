from vcScript import *
from vcHelpers.Robot2 import *

def OnRun():
  #get robot
  app = getApplication()
  robot_comp = app.findComponent("GenericRobot")
  robot = getRobot(robot_comp)
  
  #use sensor signal to initiate part pick-up
  comp = getComponent()
  sensor_signal = comp.findBehaviour("SensorSignal")
  
  stack_size = 8
  x,y,z = 0,0,0
  while stack_size > 0:
    triggerCondition(lambda: sensor_signal.Value != None)
    part = sensor_signal.Value
    robot.callSubRoutine("PickPart")
    pallet = app.findComponent("Euro Pallet")
    robot.placeInPattern(pallet,x,y,z,2,2,2)
    stack_size -= 1
    #x,y,z are index values
    if x < 1:
      x += 1
    else:
      x = 0
      y += 1
    if y > 1:
      y = 0
      z += 1
  
  #return robot to initial position
  robot.driveJoints(0,0,90,0,90,0)