import pygame
from entity import Entity
from constants import *
from sprites import FruitSprites

class Fruit(Entity):
    def __init__(self, node, level=0):
        Entity.__init__(self, node)
        self.name = FRUIT
        self.color = GREEN
        self.lifespan = 5
        self.timer = 0
        self.destroy = False
        self.points = 100 + level*20
        self.setBetweenNodes(RIGHT)
        self.sprites = FruitSprites(self, level)

    def update(self, dt):
        self.timer += dt
        if self.timer >= self.lifespan:
            self.destroy = True
            
            
            
class Teleport(Entity):
    def __init__(self, node, target_node):
        Entity.__init__(self, node)
        self.name = TELEPORT
        self.color = BLUE  # Võite värvi muuta vastavalt soovile
        self.target_node = target_node

    def teleport(self, entity):
        entity.node = self.target_node
        entity.position = self.target_node.position

    def update(self, dt):
        pass  # Siin saate vajadusel lisada mingeid uuendusi

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)  # Muutke vastavalt vajadusele

