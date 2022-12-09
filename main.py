from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

print("Hello, AVIATIER!")
class Aviatier():

    def __init__(self):
        self.COLOR_TRIGGERED_ACTIONS = {
             # Color.BLUE: self.aviatar,
             Color.GREEN: self.angry_mode,
             # Color.RED: self.christmas_ball,
             # Color.YELLOW: self.pride
         }
        self.gun = Motor(Port.B)
        self.arms = Motor(Port.D)
        self.rightLeg = Motor(Port.A)
        self.leftLeg = Motor(Port.E)
        self.eyes = UltrasonicSensor(Port.C)
        self.colorEye = ColorSensor(Port.F)
        self.hub = InventorHub()

        self.scan_for_action_triggers()

    def stop(self):
        self.rightMotor.stop()
        self.leftMotor.stop()

    def play_song(self):
        notes = ["A4/4", "A4/4", "E5/8", "E5/8", "F5/8", "E5/8"]
        notes2 = ["R/8", "A4/8", "A4/4", "E5/8", "E5/8", "F5/8", "E5/8"]
        notes3 = ["A4/4", "A4/4", "E5/8", "E5/8", "F5/8", "E5/8"]
        notes4 = ["R/8", "C5/8", "C5/4", "A4/8",  "C5/8",  "C5/4"]
        lady_gaga = notes+notes2+notes3+notes4
        #hub.speaker.play_notes(lady_gaga, tempo=200)

        jingle_bells = ["E4/4", "E4/4", "E4/2",
                        "E4/4", "E4/4", "E4/2",
                        "E4/4", "G4/4", "C4/4", "D4/4", "E4/1",
                        "F4/4", "F4/4", "F4/4", "F4/4", "F4/4", "E4/4", "E4/2",
                        "G4/4", "G4/4", "F4/4", "D4/4", "C4/1"]
        #hub.speaker.play_notes(jingle_bells, tempo=200)

        fly = ["C4/2/3", "B4/2/3", "C4/2/3", "C4/8", "A3/4*1.5",
              "D4/2/3", "D4/2/3", "D4/2/3", "E4/2/3", "F/2/3", "F4/2/3",
              "F4/2/3", "E4/2/3", "C4/2/3", "G3/2",
              "C4/2/3", "C4/2/3", "C4/2/3", "C4/2/3", "D4/2/3", "E4/2/3",
              "E4/2/3", "D4/2/3", "C4/2/3", "D4/2",
              "H4/2/3", "H4/2/3", "H4/2/3", "H4/2/3", "C4/2/3", "D4/2/3",
              "D4/2/3", "C4/2/3"]
        # hub.speaker.play_notes(fly, tempo=100)

        alarm = ["E4/8", "C4/8", "E4/8", "C4/8"]

        alarm_song = ["E4/4", "C4/2*1.5", "E4/4", "C4/2*1.5",
                "E4/4", "C4/4", "E4/4", "C4/4", "E4/8", "C4/8", "D4/2*1.5",
                "D4/8", "E4/8", "F4/4", "F4/4", "R/4",
                "E4/8", "D4/8", "E4/4", "C4/4", "R/4",
                "C4/8", "E4/8", "D4/4", "G3/4", "B3/4", "D4/4", "C4/2*1.5"]

        self.hub.speaker.play_notes(alarm_song, tempo=180)


    def angry_mode(self):
        startingAngle = self.arms.angle()
        print("starting at:")
        print(startingAngle)

        self.arms.run_target(500, startingAngle+800)

        wait(1000)

        angry_rotation = self.detect_enemy()
        self.arms.run_target(500, startingAngle+100)

        self.play_song()

        self.shoot(3)

        wait(1000)
        self.arms.run_target(200, startingAngle)

        print("resetting by:")
        print(angry_rotation)
        self.reset_position(angry_rotation)

    def shoot(self, chamber:int):
        originalAngle = self.gun.angle()
        print("original angle:")
        print(originalAngle)

        if (chamber == 1):
            print("shooting left")
            newAngle = originalAngle-60
            self.gun.run_target(500, newAngle)
            print("shot fired")
        if (chamber == 2):
            print("shooting right")
            newAngle = originalAngle+60
            self.gun.run_target(500, newAngle)
            print("shot fired")
        else:
            print("rapid fire")
            self.gun.run_target(1000, originalAngle+60)
            print("shot right")
            self.gun.run_target(1000, originalAngle-60)
            print("shot left")

        # reset shooting motor to original position
        self.gun.run_target(100, originalAngle)


    def reset_position(self, angle):
        self.rightLeg.run_angle(100, -1*angle, Stop.HOLD, False)
        self.leftLeg.run_angle(100, -1*angle, Stop.HOLD, True)
        wait(1000)


    def detect_enemy(self):
        angry_rotation = 0

        while True:
            # Print the measured distance.
            print(self.eyes.distance())

            # If an object is detected closer than 500mm:
            if self.eyes.distance() < 800:
                print("enemy detected!")
                return angry_rotation
            else:
                self.rightLeg.run_angle(100, 20, Stop.HOLD, False)
                self.leftLeg.run_angle(100, 20, Stop.HOLD, True)
                self.hub.speaker.play_notes(
                    ["E4/4", "C4/4"], tempo=180)
                angry_rotation = angry_rotation + 20


    def find_ball(self):
        ROCK_COLORS = Color.RED
        print("scanning for colour RED")
        while True:
            # If a ball color is detected, log it
            if self.colorEye.color() is ROCK_COLORS:
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

    def scan_for_action_triggers(self):
        lightStages = [[50, 0, 0], [0, 50, 0], [0, 0, 50]]
        lightNumber = 0
        self.hub.light.on(Color.WHITE)

        while True:
            foundColor = self.colorEye.color()
            if (foundColor == Color.NONE):
                self.colorEye.lights.on(lightStages[lightNumber % 3])
                lightNumber = lightNumber + 1 if lightNumber < 2 else 0
            if (foundColor in self.COLOR_TRIGGERED_ACTIONS):
                self.colorEye.lights.off()
                self.hub.light.on(foundColor)
                self.COLOR_TRIGGERED_ACTIONS[foundColor]()
                self.hub.light.on(Color.WHITE)
            wait(100)

aviatier = Aviatier()
