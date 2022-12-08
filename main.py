from pybricks.geometry import Matrix
from pybricks.hubs import InventorHub
from pybricks.parameters import Color, Side, Icon
from pybricks.tools import wait, StopWatch


class Aviatier:
    def __init__(self):
        self.hub = InventorHub()
        self.hub.display.orientation(up=Side.RIGHT)
        self.display = self.hub.display
        self.light = self.hub.light

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

    def happy_face(self):
        self.light.on(Color.RED)

        happyface = Matrix(
            [
                [15, 100, 0, 100, 15],
                [100, 30, 100, 30, 100],
                [0, 0, 0, 0, 0],
                [100, 25, 10, 25, 100],
                [15, 100, 100, 100, 15]
            ]
        )

        self.display.icon(happyface)

        wait(5000)

    def happy_face2(self):
        self.light.on(Color.RED)

        happyface = Matrix(
            [
                [0, 100, 0, 100, 0],
                [0, 100, 0, 100, 0],
                [100, 0, 0, 0, 100],
                [15, 100, 0, 100, 15],
                [0, 15, 100, 15, 0]
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

        matrix = [Matrix(
            [
                [100, 100, 0, 100, 100],
                [100, 100, 0, 100, 100],
                [0, 0, 0, 0, 0],
                [25, 100, 100, 100, 25],
                [100, 15, 0, 15, 100]
            ]
        ), Matrix(
            [
                [0, 0, 0, 0, 0],
                [100, 100, 0, 100, 100],
                [0, 0, 0, 0, 0],
                [25, 100, 100, 100, 25],
                [100, 15, 0, 15, 100]
            ]
        )]

        self.display.animate(matrix, 600)
        wait(10000)

    def heart_and_stars_face(self):
        heart = Matrix(
            [
                [10, 100, 25, 100, 10],
                [100, 10, 100, 10, 100],
                [100, 10, 0, 10, 100],
                [0, 100, 0, 100, 0],
                [0, 0, 100, 0, 0]
            ]
        )

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
        self.display.animate([heart_icon, star], 10)

    def battery_face(self):
        self.light.on(Color.RED)

        battery1 = Matrix(
            [
                [0, 0, 0, 0, 0],
                [100, 100, 100, 100, 100],
                [100, 0, 0, 100, 100],
                [100, 100, 100, 100, 100],
                [0, 0, 0, 0, 0]
            ]
        )
        battery2 = Matrix(
            [
                [0, 0, 0, 0, 0],
                [100, 100, 100, 100, 100],
                [100, 0, 0, 0, 100],
                [100, 100, 100, 100, 100],
                [0, 0, 0, 0, 0]
            ]
        )
        self.display.animate([battery1, battery2], 50)
        wait(5000)

    def christmas_face(self):
        self.light.animate([Color.GREEN, Color.RED], 500)

        christmas = Matrix(
            [
                [0, 0, 100, 0, 0],
                [0, 25, 100, 25, 0],
                [25, 50, 100, 50, 25],
                [50, 75, 100, 75, 50],
                [75, 100, 100, 100, 75]
            ]
        )
        self.display.icon(christmas)
        wait(5000)

    def plane_face(self):
        self.light.animate([Color.GREEN, Color.BLUE, Color.VIOLET], 500)

        plane = Matrix(
            [
                [100, 25, 0, 0, 0],
                [25, 100, 50, 10, 0],
                [0, 50, 100, 75, 75],
                [0, 10, 75, 100, 15],
                [0, 0, 75, 15, 100]
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
            [explosion1, explosion2, explosion3, explosion4, explosion5, explosion6, explosion7, explosion8], 50)


aviatier = Aviatier()
