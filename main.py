from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# We'll use two motors. One is a dial
# to set the speed of the other motor.
leftMotor = Motor(Port.B)
rightMotor = Motor(Port.A)
grabber = Motor(Port.F)

# Say hello :)
print("Hello, Pybricks!")

# First, we'll move the dial to zero.
# dial.run_target(500, 0, Stop.COAST)

while True:
    grabSpeed = 100
    grabber.run_target(-1*grabSpeed)
    wait()
    grabber.stop()
    wait(1000)


def drive():
    while True:
        # Set the speed based on dial angle
        speed = 500
        if abs(speed) < 100:
            speed = 0

        leftMotor.run(speed)
        rightMotor.run(-1*speed)

        wait(1000)
        leftMotor.stop()
        rightMotor.stop()
        wait(1000)

        print(leftMotor.angle())
        print("+90=")
        newAngle = leftMotor.angle()+90

        print(newAngle)

        leftMotor.run_angle(500, newAngle)

        wait(1000)