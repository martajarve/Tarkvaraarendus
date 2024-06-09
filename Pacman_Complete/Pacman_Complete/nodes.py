import pygame  # Impordi pygame moodul
from vector import Vector2  # Impordi Vector2 klass
from constants import *  # Impordi kõik konstandid
import numpy as np  # Impordi numpy moodul

class Node(object):
    def __init__(self, x, y):
        self.position = Vector2(x, y)  # Loo positsiooni vektor
        self.neighbors = {UP:None, DOWN:None, LEFT:None, RIGHT:None, PORTAL:None}  # Loo naabrite sõnastik
        self.access = {UP:[PACMAN, BLINKY, PINKY, INKY, CLYDE, FRUIT], 
                       DOWN:[PACMAN, BLINKY, PINKY, INKY, CLYDE, FRUIT], 
                       LEFT:[PACMAN, BLINKY, PINKY, INKY, CLYDE, FRUIT], 
                       RIGHT:[PACMAN, BLINKY, PINKY, INKY, CLYDE, FRUIT]}  # Loo ligipääsu sõnastik

    def denyAccess(self, direction, entity):
        if entity.name in self.access[direction]:  # Kui antud suuna ligipääsu sõnastikus on antud olendi nimi
            self.access[direction].remove(entity.name)  # Eemalda olendi nimi antud suuna ligipääsu sõnastikust

    def allowAccess(self, direction, entity):
        if entity.name not in self.access[direction]:  # Kui antud suuna ligipääsu sõnastikus pole antud olendi nime
            self.access[direction].append(entity.name)  # Lisa olendi nimi antud suuna ligipääsu sõnastikku

    def render(self, screen):
        for n in self.neighbors.keys():  # Käi läbi kõik naabrid
            if self.neighbors[n] is not None:  # Kui naaber on olemas
                line_start = self.position.asTuple()  # Saada positsiooni tuple
                line_end = self.neighbors[n].position.asTuple()  # Saada naabri positsiooni tuple
                pygame.draw.line(screen, WHITE, line_start, line_end, 4)  # Joonista joon ekraanile
                pygame.draw.circle(screen, RED, self.position.asInt(), 12)  # Joonista ring ekraanile


class NodeGroup(object):
    def __init__(self, level):
        self.level = level  # Määra tase
        self.nodesLUT = {}  # Loo sõlmede otsingutabel
        self.nodeSymbols = ['+', 'P', 'n']  # Loo sõlmesümbolite list
        self.pathSymbols = ['.', '-', '|', 'p']  # Loo teesümbolite list
        data = self.readMazeFile(level)  # Loe labürindi fail
        self.createNodeTable(data)  # Loo sõlmetabel
        self.connectHorizontally(data)  # Ühenda sõlmed horisontaalselt
        self.connectVertically(data)  # Ühenda sõlmed vertikaalselt
        self.homekey = None  # Loo koduvõtme muutuja

    def readMazeFile(self, textfile):
        return np.loadtxt(textfile, dtype='<U1')  # Loe tekstifail numpy array'na

    def createNodeTable(self, data, xoffset=0, yoffset=0):
        for row in list(range(data.shape[0])):  # Käi läbi kõik read
            for col in list(range(data.shape[1])):  # Käi läbi kõik veerud
                if data[row][col] in self.nodeSymbols:  # Kui antud element on sõlmesümbol
                    x, y = self.constructKey(col+xoffset, row+yoffset)  # Konstrueeri võti
                    self.nodesLUT[(x, y)] = Node(x, y)  # Lisa sõlm sõlmede otsingutabelisse

    def constructKey(self, x, y):
        return x * TILEWIDTH, y * TILEHEIGHT  # Konstrueeri võti

    def connectHorizontally(self, data, xoffset=0, yoffset=0):
        for row in list(range(data.shape[0])):  # Käi läbi kõik read
            key = None
            for col in list(range(data.shape[1])):  # Käi läbi kõik veerud
                if data[row][col] in self.nodeSymbols:  # Kui antud element on sõlmesümbol
                    if key is None:  # Kui võtit pole veel loodud
                        key = self.constructKey(col+xoffset, row+yoffset)  # Loo võti
                    else:  # Kui võti on juba loodud
                        otherkey = self.constructKey(col+xoffset, row+yoffset)  # Loo teine võti
                        self.nodesLUT[key].neighbors[RIGHT] = self.nodesLUT[otherkey]  # Ühenda sõlmed paremale
                        self.nodesLUT[otherkey].neighbors[LEFT] = self.nodesLUT[key]  # Ühenda sõlmed vasakule
                        key = otherkey  # Määra teine võti esimeseks võtmeks
                elif data[row][col] not in self.pathSymbols:  # Kui antud element pole teesümbol
                    key = None  # Nulli võti

    def connectVertically(self, data, xoffset=0, yoffset=0):
        dataT = data.transpose()  # Transponeeri andmed
        for col in list(range(dataT.shape[0])):  # Käi läbi kõik veerud
            key = None
            for row in list(range(dataT.shape[1])):  # Käi läbi kõik read
                if dataT[col][row] in self.nodeSymbols:  # Kui antud element on sõlmesümbol
                    if key is None:  # Kui võtit pole veel loodud
                        key = self.constructKey(col+xoffset, row+yoffset)  # Loo võti
                    else:  # Kui võti on juba loodud
                        otherkey = self.constructKey(col+xoffset, row+yoffset)  # Loo teine võti
                        self.nodesLUT[key].neighbors[DOWN] = self.nodesLUT[otherkey]  # Ühenda sõlmed alla
                        self.nodesLUT[otherkey].neighbors[UP] = self.nodesLUT[key]  # Ühenda sõlmed üles
                        key = otherkey  # Määra teine võti esimeseks võtmeks
                elif dataT[col][row] not in self.pathSymbols:  # Kui antud element pole teesümbol
                    key = None  # Nulli võti

    def getStartTempNode(self):
        nodes = list(self.nodesLUT.values())  # Saada sõlmede list
        return nodes[0]  # Tagasta esimene sõlm

    def setPortalPair(self, pair1, pair2):
        key1 = self.constructKey(*pair1)  # Konstrueeri esimene võti
        key2 = self.constructKey(*pair2)  # Konstrueeri teine võti
        if key1 in self.nodesLUT.keys() and key2 in self.nodesLUT.keys():  # Kui mõlemad võtmed on olemas
            self.nodesLUT[key1].neighbors[PORTAL] = self.nodesLUT[key2]  # Ühenda esimene sõlm teise sõlmega
            self.nodesLUT[key2].neighbors[PORTAL] = self.nodesLUT[key1]  # Ühenda teine sõlm esimese sõlmega

    def createHomeNodes(self, xoffset, yoffset):
        homedata = np.array([['X','X','+','X','X'],
                             ['X','X','.','X','X'],
                             ['+','X','.','X','+'],
                             ['+','.','+','.','+'],
                             ['+','X','X','X','+']])  # Loo koduandmed

        self.createNodeTable(homedata, xoffset, yoffset)  # Loo kodusõlmetabel
        self.connectHorizontally(homedata, xoffset, yoffset)  # Ühenda kodusõlmed horisontaalselt
        self.connectVertically(homedata, xoffset, yoffset)  # Ühenda kodusõlmed vertikaalselt
        self.homekey = self.constructKey(xoffset+2, yoffset)  # Loo koduvõti

        return self.homekey

    def connectHomeNodes(self, homekey, otherkey, direction):     
        key = self.constructKey(*otherkey)
        self.nodesLUT[homekey].neighbors[direction] = self.nodesLUT[key]
        self.nodesLUT[key].neighbors[direction*-1] = self.nodesLUT[homekey]

    def getNodeFromPixels(self, xpixel, ypixel):
        if (xpixel, ypixel) in self.nodesLUT.keys():
            return self.nodesLUT[(xpixel, ypixel)]
        return None

    def getNodeFromTiles(self, col, row):
        x, y = self.constructKey(col, row)
        if (x, y) in self.nodesLUT.keys():
            return self.nodesLUT[(x, y)]
        return None

    def denyAccess(self, col, row, direction, entity):
        node = self.getNodeFromTiles(col, row)
        if node is not None:
            node.denyAccess(direction, entity)

    def allowAccess(self, col, row, direction, entity):
        node = self.getNodeFromTiles(col, row)
        if node is not None:
            node.allowAccess(direction, entity)

    def denyAccessList(self, col, row, direction, entities):
        for entity in entities:
            self.denyAccess(col, row, direction, entity)

    def allowAccessList(self, col, row, direction, entities):
        for entity in entities:
            self.allowAccess(col, row, direction, entity)

    def denyHomeAccess(self, entity):
        self.nodesLUT[self.homekey].denyAccess(DOWN, entity)

    def allowHomeAccess(self, entity):
        self.nodesLUT[self.homekey].allowAccess(DOWN, entity)

    def denyHomeAccessList(self, entities):
        for entity in entities:
            self.denyHomeAccess(entity)

    def allowHomeAccessList(self, entities):
        for entity in entities:
            self.allowHomeAccess(entity)

    def render(self, screen):
        for node in self.nodesLUT.values():
            node.render(screen)