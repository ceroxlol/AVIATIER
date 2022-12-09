from pybricks.geometry import Matrix
from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.parameters import Color, Side, Icon
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

        # set volume
        self.hub.speaker.volume(30)

        self.scan_for_action_triggers()


        # self.angry_mode()

    def alarm_song(self):
        alarm_song = ["E4/4", "C4/2*1.5", "E4/4", "C4/2*1.5",
                "E4/4", "C4/4", "E4/4", "C4/4", "E4/8", "C4/8", "D4/2*1.5",
                "D4/8", "E4/8", "F4/4", "F4/4", "R/4",
                "E4/8", "D4/8", "E4/4", "C4/4", "R/4",
                "C4/8", "E4/8", "D4/4", "G3/4", "B3/4", "D4/4", "C4/2*1.5"]

        self.hub.speaker.play_notes(alarm_song, tempo=180)

    def drive(self, speed):
        self.leftLeg.run(-1*speed)
        self.rightLeg.run(speed)

    def turn(self, direction, speed):
        if direction == 'clockwise':
            self.leftLeg.run(speed)
            self.rightLeg.run(speed)
        elif direction == 'anti':
            self.leftLeg.run(-1*speed)
            self.rightLeg.run(-1*speed)

    def stop(self):
        self.leftLeg.stop()
        self.rightLeg.stop()

    def test_gaga(self):
        notes = ["A3/4", "A3/4", "E4/8", "E4/8", "F4/8", "E4/8"]
        notes2 = ["R/8", "A3/8", "A3/4", "E4/8", "E4/8", "F4/8", "E4/8"]
        notes3 = ["A3/4", "A3/4", "E4/8", "E4/8", "F4/8", "E4/8"]
        notes4 = ["R/8", "C4/8", "C4/8", "A3/8",  "C4/8",  "C4/4", "R/8"]
        notes5 = ["F5/4", "F5/4", "F5/8", "E5/4", "D5/4", "B4/4", "B4/8", "C5/4", "D5/4", "E5/4", "E5/8", "E5/8", "E5/8", "D5/4", "C5/4", "R/8", "R/4", "R/8", "A4/8", "C5/8", "E5/8"]
        notes6 = ["F5/4", "F5/4", "F5/8", "E5/4", "D5/4", "B4/4", "B4/8", "C5/4", "D5/4", "E5/4", "E5/8", "E5/8", "E5/8", "D5/4", "C5/4", "R/8", "R/1"]
        notes7 = ["A3/4", "A3/4", "E4/8", "E4/8", "F4/8", "E4/8"]
        notes8 = ["R/8", "A3/8", "A3/4", "E4/8", "E4/8", "F4/8", "E4/8"]
        notes9 = ["A3/4", "A3/4", "E4/8", "E4/8", "F4/8", "E4/8"]
        notes10 = ["R/8", "C4/8", "C4/8", "A3/8",  "C4/8",  "C4/4"]
        lady_gaga = notes+notes2+notes3+notes4 + notes5+notes6+notes7+notes8+notes9+notes10

        self.hub.speaker.play_notes(lady_gaga, tempo=150)

    def flying(self):
        fly1 = ["C4/2/3", "B3/2/3", "C4/2/3", "C4/2/3", "A3/1", 
               "D4/2/3", "D4/2/3", "D4/2/3", "E4/2/3", "F4/2/3", "F4/2/3"]
        fly2 = ["E4/2/3", "C4/2/3",  "G3/1",
               "C4/2/3", "C4/2/3", "C4/2/3", "C4/2/3", "D4/2/3", "E4/2/3"]
        fly3 = ["E4/2/3", "D4/2/3", "C4/2/3", "D4/1",
               "B3/2/3", "B3/2/3", "B3/2/3", "B3/2/3", "C4/2/3", "D4/2/3"]
        fly4 = ["D4/2/3", "C4/1"]

        flyingSpeed = 300

        self.drive(100)
        self.arms.run(flyingSpeed/2)
        self.hub.speaker.play_notes(fly1, tempo=375)
        self.arms.run(-1*flyingSpeed)

        self.hub.speaker.play_notes(fly2, tempo=375)
        self.arms.run(flyingSpeed)

        self.hub.speaker.play_notes(fly3, tempo=375)
        self.arms.run(-1*flyingSpeed)

        self.hub.speaker.play_notes(fly4, tempo=375)
        self.arms.run(flyingSpeed)
        wait(500)
        self.arms.stop()


        # reverse to starting position
        self.drive(-300)
        wait(4000)
        self.stop()


    def bad_romance(self, speed):
        while True:
            print('Dancing...')
            #Move hands
            notes = ["A4/4", "A4/4", "E5/8", "E5/8", "F5/8", "E5/8"]
            notes2 = ["R/8", "A4/8", "A4/4", "E5/8", "E5/8", "F5/8", "E5/8"]
            notes3 = ["A4/4", "A4/4", "E5/8", "E5/8", "F5/8", "E5/8"]
            notes4 = ["R/8", "C5/8", "C5/4", "A4/8",  "C5/8",  "C5/4"]

            notes = ["A4/4", "A4/4", "E5/8", "E5/8", "F5/8", "E5/8"]

            self.turn('clockwise', speed)
            self.hub.speaker.play_notes(notes, tempo=200)
            self.drive(speed)
            self.hub.speaker.play_notes(notes2, tempo=200)
            self.turn('anti', speed)
            self.hub.speaker.play_notes(notes3, tempo=200)
            self.drive(speed)
            self.hub.speaker.play_notes(notes4, tempo=200)
            self.stop()
            print('Done moving')

    def jingle_bells(self):
        print("starting jingle bells")
        movingSpeed = 700

        self.arms.run(movingSpeed)
        self.turn('clockwise', 400)
        self.hub.speaker.play_notes(["E4/4", "E4/4", "E4/2"], tempo=200)
        self.arms.run(-2*movingSpeed)
        self.hub.speaker.play_notes(["E4/4", "E4/4", "E4/2"], tempo=200)
        self.arms.run(2*movingSpeed)
        self.hub.speaker.play_notes(
            ["E4/4", "G4/4", "C4/4", "D4/4"], tempo=200)
        self.arms.run(-2*movingSpeed)
        self.hub.speaker.play_notes(["E4/1"], tempo=200)
        self.arms.run(2*movingSpeed)
        self.turn('anti', 400)
        self.hub.speaker.play_notes(
            ["F4/4", "F4/4", "F4/4", "F4/4"], tempo=200)
        self.arms.run(-2*movingSpeed)
        self.hub.speaker.play_notes(["F4/4", "E4/4", "E4/2"], tempo=200)
        self.arms.run(2*movingSpeed)
        self.hub.speaker.play_notes(
            ["G4/4", "G4/4", "F4/4", "D4/4"], tempo=200)
        self.arms.run(-2*movingSpeed)
        self.hub.speaker.play_notes(["C4/1"], tempo=200)
        
        self.arms.run(movingSpeed)
        wait(1200)

        self.arms.stop()


    def angry_mode(self):
        startingAngle = self.arms.angle()
        print("starting at:")
        print(startingAngle)

        self.arms.run_target(500, startingAngle+800)

        wait(1000)

        angry_rotation = self.detect_enemy()
        self.arms.run_target(500, startingAngle+100)

        self.alarm_song() 

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

    def angry_face(self):
        self.light.on(Color.RED)

        sadface = Matrix(
            [
                [100, 0, 0, 0, 100],
                [0, 100, 0, 100, 0],
                [0, 0, 0, 0, 0],
                [25, 100, 100, 100, 25],
                [100, 15, 0, 15, 100]
            ]
        )

        self.display.icon(sadface)

        wait(5000)

    def happy_face2(self):
        self.light.on(Color.RED)

        happyface = Matrix(
            [
                [100, 100, 0, 100, 100],
                [100, 100, 0, 100, 100],
                [0, 0, 0, 0, 0],
                [100, 15, 0, 15, 100],
                [15, 100, 100, 100, 0]
            ]
        )

        self.display.icon(happyface)

        wait(5000)

    def pissed_face(self):
        self.light.on(Color.RED)

        pissedface = Matrix(
            [
                [0, 0, 0, 0, 0],
                [100, 100, 0, 100, 100],
                [0, 0, 0, 0, 0],
                [25, 100, 100, 100, 25],
                [100, 15, 0, 15, 100]
            ]
        )

        self.display.icon(pissedface)

        wait(5000)

    def blinking_sad_face(self):
        self.light.on(Color.RED)

        sad_face = Matrix(
            [
                [0, 100, 0, 100, 0],
                [100, 100, 0, 100, 100],
                [0, 0, 0, 0, 0],
                [25, 100, 100, 100, 25],
                [100, 15, 0, 15, 100]
            ]
        )

        self.display.icon(sad_face)
        wait(5000)

    def heart_and_stars_face(self):
        heart_icon = Icon.HEART

        star = Matrix(
            [
                [50, 0, 100, 0, 50],
                [0, 50, 100, 50, 0],
                [100, 100, 100, 100, 100],
                [0, 50, 100, 50, 0],
                [50, 0, 100, 0, 50]
            ]
        )
        self.display.animate([heart_icon, star], 600)
        wait(5000)

    def battery_face(self):
        self.light.on(Color.RED)

        battery1 = Matrix(
            [
                [0, 0, 0, 0, 0],
                [0, 100, 100, 100, 100],
                [100, 100, 0, 100, 100],
                [0, 100, 100, 100, 100],
                [0, 0, 0, 0, 0]
            ]
        )
        battery2 = Matrix(
            [
                [0, 0, 0, 0, 0],
                [0, 100, 100, 100, 100],
                [100, 100, 0, 0, 100],
                [0, 100, 100, 100, 100],
                [0, 0, 0, 0, 0]
            ]
        )
        self.display.animate([battery1, battery2], 500)
        wait(5000)

    def christmas_face(self):
        self.light.animate([Color.GREEN, Color.RED], 500)

        christmas = Matrix(
            [
                [0, 0, 100, 0, 0],
                [0, 75, 100, 75, 0],
                [70, 60, 100, 75, 35],
                [100, 100, 100, 100, 100],
                [0, 0, 100, 0, 0]
            ]
        )
        self.display.icon(christmas)
        wait(5000)

    def plane_face(self):
        self.light.animate([Color.GREEN, Color.BLUE, Color.VIOLET], 500)

        plane = Matrix(
            [
                [100, 25, 0, 0, 0],
                [25, 100, 75, 75, 50],
                [0, 75, 100, 15, 15],
                [0, 75, 15, 100, 15],
                [0, 50, 15, 15, 100]
            ]
        )
        self.display.icon(plane)
        wait(5000)

    def aviatar_face(self):
        self.light.animate([Color.GREEN, Color.BLUE, Color.VIOLET], 500)

        aviatar = Matrix(
            [
                [50, 100, 100, 100, 100],
                [100, 50, 0, 0, 100],
                [100, 100, 100, 0, 100],
                [0, 0, 100, 50, 100],
                [0, 0, 100, 100, 50]
            ]
        )

        self.display.icon(aviatar)
        wait(5000)

    def explosion(self):
        self.light.on(Color.RED)

        explosion1 = Matrix(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 100, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]
            ]
        )
        explosion2 = Matrix(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 100, 0, 0],
                [0, 100, 75, 100, 0],
                [0, 0, 100, 0, 0],
                [0, 0, 0, 0, 0]
            ]
        )
        explosion3 = Matrix(
            [
                [0, 0, 100, 0, 0],
                [0, 100, 75, 100, 0],
                [100, 75, 50, 75, 100],
                [0, 100, 75, 100, 0],
                [0, 0, 100, 0, 0]
            ]
        )
        explosion4 = Matrix(
            [
                [0, 100, 75, 100, 0],
                [100, 75, 50, 75, 100],
                [75, 50, 25, 50, 75],
                [100, 75, 50, 75, 100],
                [0, 100, 75, 100, 0]
            ]
        )
        explosion5 = Matrix(
            [
                [100, 75, 50, 75, 100],
                [75, 50, 25, 50, 75],
                [50, 25, 0, 25, 50],
                [75, 50, 25, 50, 75],
                [100, 75, 50, 75, 100]
            ]
        )
        explosion6 = Matrix(
            [
                [75, 50, 25, 50, 75],
                [50, 25, 0, 25, 50],
                [25, 0, 0, 0, 25],
                [50, 25, 0, 25, 50],
                [75, 50, 25, 50, 75]
            ]
        )
        explosion7 = Matrix(
            [
                [50, 25, 0, 25, 50],
                [25, 0, 0, 0, 25],
                [0, 0, 0, 0, 0],
                [25, 0, 0, 0, 25],
                [50, 25, 0, 25, 50]
            ]
        )
        explosion8 = Matrix(
            [
                [25, 0, 0, 0, 25],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [25, 0, 0, 0, 25]
            ]
        )

        self.display.animate(
            [explosion1, explosion2, explosion3, explosion4, explosion5, explosion6, explosion7, explosion8], 200)
        wait(5000)

aviatier = Aviatier()
