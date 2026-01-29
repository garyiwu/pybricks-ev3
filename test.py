from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, GyroSensor, InfraredSensor, TouchSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = EV3Brick()

hub.screen.clear()
hub.screen.print("hello world")
hub.screen.print("program 1")

hub.speaker.beep(1000, 100)

m1 = Motor(Port.A)
m1.run_angle(500, 500)
m1.run_angle(500, -500)

hub.speaker.beep(2000, 100)
