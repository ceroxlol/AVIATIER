from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Say hello :)
print("Hello, AVIATIER!")


class Aviatier():
    ROCK_COLORS = Color.RED

    def __init__(self):
        # Wheels
        self.rightMotor = Motor(Port.A)
        self.leftMotor = Motor(Port.B)
        # Grabber
        self.grabber = Motor(Port.F)
        # Sensors
        # self.sherloc = ColorSensor(Port.C)
        self.eyes = UltrasonicSensor(Port.D)

        self.hub = InventorHub()
        self.scan_distance()

    def stop(self):
        self.rightMotor.stop()
        self.leftMotor.stop()

    def scan_distance(self):
        while True:
            # Print the measured distance.
            print(self.eyes.distance())

            # If an object is detected closer than 500mm:
            if self.eyes.distance() < 500:
                # Turn the lights on.
                self.hub.speaker.beep()
                print("found something")

                wait(100)


def find_ball(self):
    print("scanning for colour RED")
    while True:
        # If a ball color is detected, log it
        if self.sherloc.color() is self.ROCK_COLORS:
            print("Colour found!")
            self.hub.speaker.beep()

        wait(100)


def grab():
    while True:
        grabSpeed = 100
        grabber.run_target(-1 * grabSpeed)
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
        rightMotor.run(-1 * speed)

        wait(1000)
        leftMotor.stop()
        rightMotor.stop()
        wait(1000)

        print(leftMotor.angle())
        print("+90=")
        newAngle = leftMotor.angle() + 90

        print(newAngle)

        leftMotor.run_angle(500, newAngle)


aviatier = Aviatier()
