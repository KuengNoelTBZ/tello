#
#   project: tello_test.py
#   author: Noel Kueng
#

from tello import Tello

drone = Tello()

drone.takeoff()
drone.up(x=50)
drone.land()