#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

def move_forward(data):
    print("Move forward")
    
    motorL = Motor(Port.B)
    motorR = Motor(Port.C)
    motorL.run(500)
    motorR.run(500)

def move_backward(data):
    print("Move forward")
    
    motorL = Motor(Port.B)
    motorR = Motor(Port.C)
    motorL.run(-500)
    motorR.run(-500)


def turn_left(data):
    print("Left")
    
    motorL = Motor(Port.B)
    motorR = Motor(Port.C)
    motorL.run(-500)
    motorR.run(500)

def turn_right(data):
    print("Right")
    
    motorL = Motor(Port.B)
    motorR = Motor(Port.C)
    motorL.run(500)
    motorR.run(-500)


def stop(data):
    print("stop")
    
    motorL = Motor(Port.B)
    motorR = Motor(Port.C)
    motorL.stop()
    motorR.stop()


def unknown_command(data):
    print("UNKNOWN COMMAND:" + data)
    ev3.screen.print(data)
    #ev3.speaker.say(data)

