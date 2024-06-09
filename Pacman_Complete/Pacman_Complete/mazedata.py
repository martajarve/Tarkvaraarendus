from constants import *

class MazeBase(object):
    def __init__(self):
        # Baasiklass määratleb ühiseid meetodeid ja atribuute
        self.portalPairs = {}  # Paarid portaalide koordinaatide jaoks
        self.homeoffset = (0, 0)  # Koordinaadid koduõõnes
        self.ghostNodeDeny = {UP:(), DOWN:(), LEFT:(), RIGHT:()}  # Keelatud ligipääsu sõlmed kummituste jaoks

    def setPortalPairs(self, nodes):
        # Seadistab portaalide paarid sõlmedele
        for pair in list(self.portalPairs.values()):
            nodes.setPortalPair(*pair)

    def connectHomeNodes(self, nodes):
        # Ühendab koduõõnes olevad sõlmed
        key = nodes.createHomeNodes(*self.homeoffset)
        nodes.connectHomeNodes(key, self.homenodeconnectLeft, LEFT)
        nodes.connectHomeNodes(key, self.homenodeconnectRight, RIGHT)

    def addOffset(self, x, y):
        # Lisab nihke koordinaatidele
        return x + self.homeoffset[0], y + self.homeoffset[1]

    def denyGhostsAccess(self, ghosts, nodes):
        # Keelab kummitustel ligipääsu teatud sõlmedele
        nodes.denyAccessList(*(self.addOffset(2, 3) + (LEFT, ghosts)))
        nodes.denyAccessList(*(self.addOffset(2, 3) + (RIGHT, ghosts)))

        for direction in list(self.ghostNodeDeny.keys()):
            for values in self.ghostNodeDeny[direction]:
                nodes.denyAccessList(*(values + (direction, ghosts)))


class Maze1(MazeBase):
    def __init__(self):
        # Esimese labürindi konkreetsed atribuudid
        MazeBase.__init__(self)
        self.name = "maze1"
        self.portalPairs = {0:((0, 17), (27, 17))}
        self.homeoffset = (11.5, 14)
        self.homenodeconnectLeft = (12, 14)
        self.homenodeconnectRight = (15, 14)
        self.pacmanStart = (15, 26)
        self.fruitStart = (9, 20)
        self.ghostNodeDeny = {UP:((12, 14), (15, 14), (12, 26), (15, 26)), LEFT:(self.addOffset(2, 3),),
                              RIGHT:(self.addOffset(2, 3),)}


class Maze2(MazeBase):
    def __init__(self):
        # Teise labürindi konkreetsed atribuudid
        MazeBase.__init__(self)
        self.name = "maze2"
        self.portalPairs = {0:((0, 4), (27, 4)), 1:((0, 26), (27, 26))}
        self.homeoffset = (11.5, 14)
        self.homenodeconnectLeft = (9, 14)
        self.homenodeconnectRight = (18, 14)
        self.pacmanStart = (16, 26)
        self.fruitStart = (11, 20)
        self.ghostNodeDeny = {UP:((9, 14), (18, 14), (11, 23), (16, 23)), LEFT:(self.addOffset(2, 3),),
                              RIGHT:(self.addOffset(2, 3),)}


class MazeData(object):
    def __init__(self):
        # Labürindi andmete haldamise klass
        self.obj = None
        self.mazedict = {0: Maze1, 1: Maze2}  # Labürindide sõnastik

    def loadMaze(self, level):
        # Laeb labürindi kindlal tasemel
        self.obj = self.mazedict[level % len(self.mazedict)]()  # Valib labürindi vastavalt tasemele
