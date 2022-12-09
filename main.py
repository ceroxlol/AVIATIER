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

        # set volume
        self.hub.speaker.volume(20)

        self.jingle_bells()

        # self.angry_mode()

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



    def jingle_bells(self):
        print("starting jingle bells")
        movingSpeed = 700

        self.arms.run(movingSpeed)
        self.turn('clockwise', movingSpeed)
        self.hub.speaker.play_notes(["E4/4", "E4/4", "E4/2"], tempo=200)
        self.arms.run(-2*movingSpeed)
        self.hub.speaker.play_notes(["E4/4", "E4/4", "E4/2"], tempo=200)
        self.arms.run(2*movingSpeed)
        self.hub.speaker.play_notes(
            ["E4/4", "G4/4", "C4/4", "D4/4"], tempo=200)
        self.arms.run(-2*movingSpeed)
        self.hub.speaker.play_notes(["E4/1"], tempo=200)
        self.arms.run(2*movingSpeed)
        self.turn('anti', movingSpeed)
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

            leftLeg.run(speed)
            rightLeg.run(-1 * speed)

            wait(1000)
            leftLeg.stop()
            rightLeg.stop()
            wait(1000)

            print(leftLeg.angle())
            print("+90=")
            newAngle = leftLeg.angle() + 90

            print(newAngle)

            leftLeg.run_angle(500, newAngle)


aviatier = Aviatier()
