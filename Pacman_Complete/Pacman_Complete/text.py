# Impordime vajalikud moodulid ja konstandid
import pygame
from vector import Vector2
from constants import *

class Text(object):
    def __init__(self, text, color, x, y, size, time=None, id=None, visible=True):
        # Teksti atribuudid
        self.id = id  # Teksti unikaalne identifikaator
        self.text = text  # Teksti sisu
        self.color = color  # Teksti värv
        self.size = size  # Teksti suurus
        self.visible = visible  # Kas tekst on nähtav
        self.position = Vector2(x, y)  # Teksti asukoht
        self.timer = 0  # Ajatimer
        self.lifespan = time  # Teksti eluiga
        self.label = None  # Pildipind teksti renderdamiseks
        self.destroy = False  # Kas tekst tuleb kustutada
        self.setupFont("PressStart2P-Regular.ttf")  # Teksti fondi seadistamine
        self.createLabel()  # Teksti pildipinna loomine

    def setupFont(self, fontpath):
        # Seadistame teksti fondi
        self.font = pygame.font.Font(fontpath, self.size)

    def createLabel(self):
        # Loome teksti pildipinna
        self.label = self.font.render(self.text, 1, self.color)

    def setText(self, newtext):
        # Määrame teksti uue sisu ja uuendame pildipinda
        self.text = str(newtext)
        self.createLabel()

    def update(self, dt):
        # Uuendame tekstile seotud väärtusi
        if self.lifespan is not None:
            self.timer += dt
            if self.timer >= self.lifespan:
                self.timer = 0
                self.lifespan = None
                self.destroy = True  # Märkame, et tekst tuleb kustutada

    def render(self, screen):
        # Renderdame tekstile vastava pildipinna ekraanile
        if self.visible:
            x, y = self.position.asTuple()
            screen.blit(self.label, (x, y))


class TextGroup(object):
    def __init__(self):
        # Tekstirühma initsialiseerimine
        self.nextid = 10  # Järgmise teksti ID
        self.alltext = {}  # Kõik tekstid
        self.setupText()  # Tekstide seadistamine
        self.showText(READYTXT)  # Näita valmisoleku teksti

    def addText(self, text, color, x, y, size, time=None, id=None):
        # Lisa uus tekst rühma
        self.nextid += 1
        self.alltext[self.nextid] = Text(text, color, x, y, size, time=time, id=id)
        return self.nextid

    def removeText(self, id):
        # Eemalda tekst rühmast
        self.alltext.pop(id)
        
    def setupText(self):
        # Seadista algtekstid
        size = TILEHEIGHT
        self.alltext[SCORETXT] = Text("0".zfill(8), WHITE, 0, TILEHEIGHT, size)
        self.alltext[LEVELTXT] = Text(str(1).zfill(3), WHITE, 23*TILEWIDTH, TILEHEIGHT, size)
        self.alltext[READYTXT] = Text("READY!", YELLOW, 11.25*TILEWIDTH, 20*TILEHEIGHT, size, visible=False)
        self.alltext[PAUSETXT] = Text("PAUSED!", YELLOW, 10.625*TILEWIDTH, 20*TILEHEIGHT, size, visible=False)
        self.alltext[GAMEOVERTXT] = Text("GAMEOVER!", YELLOW, 10*TILEWIDTH, 20*TILEHEIGHT, size, visible=False)
        self.addText("SCORE", WHITE, 0, 0, size)
        self.addText("LEVEL", WHITE, 23*TILEWIDTH, 0, size)

    def update(self, dt):
        # Uuendame tekstide olekut
        for tkey in list(self.alltext.keys()):
            self.alltext[tkey].update(dt)
            if self.alltext[tkey].destroy:
                self.removeText(tkey)

    def showText(self, id):
        # Näita valitud teksti
        self.hideText()
        self.alltext[id].visible = True

    def hideText(self):
        # Peida kõik tekstid
        self.alltext[READYTXT].visible = False
        self.alltext[PAUSETXT].visible = False
        self.alltext[GAMEOVERTXT].visible = False

    def updateScore(self, score):
        # Uuenda skoori teksti
        self.updateText(SCORETXT, str(score).zfill(8))

    def updateLevel(self, level):
        # Uuenda taseme teksti
        self.updateText(LEVELTXT, str(level + 1).zfill(3))

    def updateText(self, id, value):
        # Uuenda teksti sisu
        if id in self.alltext.keys():
            self.alltext[id].setText(value)

    def render(self, screen):
        # Renderda kõik tekstid ekraanile
        for tkey in list(self.alltext.keys()):
            self.alltext[tkey].render(screen)

