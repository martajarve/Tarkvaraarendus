# Impordime vajalikud moodulid ja konstandid
import pygame
from vector import Vector2
from constants import *
import numpy as np

class Pellet(object):
    def __init__(self, row, column):
        # Initsialiseerime pelleti atribuudid
        self.name = PELLET
        self.position = Vector2(column * TILEWIDTH, row * TILEHEIGHT)
        self.color = WHITE
        self.radius = int(2 * TILEWIDTH / 16)
        self.collideRadius = 2 * TILEWIDTH / 16
        self.points = 10
        self.visible = True
        
    def render(self, screen):
        # Renderdame pelleti ekraanile
        if self.visible:
            adjust = Vector2(TILEWIDTH, TILEHEIGHT) / 2
            p = self.position + adjust
            pygame.draw.circle(screen, self.color, p.asInt(), self.radius)


class PowerPellet(Pellet):
    def __init__(self, row, column):
        # Initsialiseerime võimendatud pelleti atribuudid, pärib Pelleti omadused
        super().__init__(row, column)
        self.name = POWERPELLET
        self.radius = int(8 * TILEWIDTH / 16)
        self.points = 50
        self.flashTime = 0.2
        self.timer = 0
        
    def update(self, dt):
        # Uuendame võimendatud pelleti olekut
        self.timer += dt
        if self.timer >= self.flashTime:
            self.visible = not self.visible
            self.timer = 0


class PelletGroup(object):
    def __init__(self, pelletfile):
        # Initsialiseerime pelletigrupi ja loome pelletid antud failist
        self.pelletList = []
        self.powerpellets = []
        self.createPelletList(pelletfile)
        self.numEaten = 0

    def update(self, dt):
        # Uuendame võimendatud pelletite olekut
        for powerpellet in self.powerpellets:
            powerpellet.update(dt)
                
    def createPelletList(self, pelletfile):
        # Loome pelletite listi tekstifailist
        data = self.readPelletfile(pelletfile)        
        for row in range(data.shape[0]):
            for col in range(data.shape[1]):
                if data[row][col] in ['.', '+']:
                    self.pelletList.append(Pellet(row, col))
                elif data[row][col] in ['P', 'p']:
                    pp = PowerPellet(row, col)
                    self.pelletList.append(pp)
                    self.powerpellets.append(pp)
                    
    def readPelletfile(self, textfile):
        # Loeme tekstifaili ja tagastame andmed numpy massiivina
        return np.loadtxt(textfile, dtype='<U1')
    
    def isEmpty(self):
        # Kontrollime, kas pelletite list on tühi
        return len(self.pelletList) == 0
    
    def render(self, screen):
        # Renderdame kõik pelletid ekraanile
        for pellet in self.pelletList:
            pellet.render(screen)
