# Impordime vajalikud konstandid
from constants import *

class Animator(object):
    def __init__(self, frames=[], speed=20, loop=True):
        # Initsialiseerime animaatori atribuudid
        self.frames = frames  # Kaadrite list
        self.current_frame = 0  # Praegune kaader
        self.speed = speed  # Kiirus kaadrite vahel
        self.loop = loop  # Kas animatsioon peaks tsüklis olema
        self.dt = 0  # Ajahetk kaadrite vahel
        self.finished = False  # Kas animatsioon on lõppenud

    def reset(self):
        # Lähtestame animatsiooni algseisundi
        self.current_frame = 0
        self.finished = False

    def update(self, dt):
        # Uuendame animatsiooni olekut
        if not self.finished:
            self.nextFrame(dt)  # Liigume järgmise kaadri juurde
        # Kontrollime, kas animatsioon on lõppenud
        if self.current_frame == len(self.frames):
            if self.loop:
                self.current_frame = 0  # Alustame uuesti
            else:
                self.finished = True  # Märkame, et animatsioon on lõppenud
                self.current_frame -= 1  # Tagasi eelmisele kaadrile
        # Tagastame praeguse kaadri
        return self.frames[self.current_frame]

    def nextFrame(self, dt):
        # Liigume järgmisele kaadrile sõltuvalt kiirusest
        self.dt += dt
        if self.dt >= (1.0 / self.speed):
            self.current_frame += 1
            self.dt = 0  # Nullime ajahetke
