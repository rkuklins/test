#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from ev3_server import *
from command_parser import *

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

def top_left_channel(state):
    print("Top left: %s" % state)


#iSensor = InfraredSensor(Port.S1);
print("Initialize EV3")
#ev3.speaker.beep()

#Start server to listen to commands
server_program()

#Close the EV3
ev3.speaker.say("Goodbye")
