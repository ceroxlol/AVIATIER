from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

print("Hello, AVIATIER!")
class Aviatier():
    ROCK_COLORS = Color.RED

    def __init__(self):
        self.gun = Motor(Port.B)
        self.arms = Motor(Port.D)
        self.rightLeg = Motor(Port.A)
        self.leftLeg = Motor(Port.E)
        self.eyes = UltrasonicSensor(Port.C)
        self.hub = InventorHub()
        
        self.angry_mode()

    def stop(self):
        self.rightMotor.stop()
        self.leftMotor.stop()

    def angry_mode(self):
        startingAngle = self.arms.angle()
        print("starting at:")
        print(startingAngle)

        self.arms.run_target(500, startingAngle+540)
        
        # scanning...
        self.detect_enemy()
        self.arms.run_target(500, startingAngle-500)

        self.shoot(1)
        self.shoot(2)

    def shoot(self, chamber:int):
        originalAngle = self.gun.angle()
        print("original angle:")
        print(originalAngle)
                
        if (chamber == 1):
            print("shooting left")
            newAngle = originalAngle-60
            self.gun.run_target(500, newAngle)
            print("shot fired")
            self.gun.run_target(100, originalAngle)
        else:
            print("shooting right")
            newAngle = originalAngle+60
            self.gun.run_target(500, newAngle)
            print("shot fired")
            self.gun.run_target(100, originalAngle)
        

    def detect_enemy(self):
        while True:
            # Print the measured distance.
            print(self.eyes.distance())

            # If an object is detected closer than 500mm:
            if self.eyes.distance() < 800:
                print("enemy detected!")
                return True
            else:
                self.rightLeg.run_angle(100, 1, Stop.HOLD, False)
                self.leftLeg.run_angle(100, 1, Stop.HOLD, False)


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
