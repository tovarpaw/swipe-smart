## ---- Imports ---- ##
import time
import board
from digitalio import Pull
from piper_blockly import *

## ---- Definitions ---- ##
oms = None
GP13 = piperPin(board.GP13, "GP13")

try:
  set_digital_view(True)
except:
  pass

GP26 = piperPin(board.GP26, "GP26", "Analog")
GP15 = piperServoPin(board.GP15, "GP15")


## ---- Code ---- ##
while True:
  while not GP13.checkPin(Pull.UP):
    oms = GP26.readVoltage()
servo    print(oms)
    if oms > 3:
      GP15.setServoAngle(0)
      time.sleep(5)
      GP15.setServoAngle(120)
      time.sleep(0.5)
    if oms >= 1:
      GP15.setServoAngle(0)
      time.sleep(3)
      GP15.setServoAngle(120)
      time.sleep(0.5)
    if oms < 1:
      GP15.setServoAngle(0)
      time.sleep(1)
      GP15.setServoAngle(120)
      time.sleep(0.5)

  time.sleep(1)