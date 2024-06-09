# Impordib vajalikud konstandid ja klassid
from constants import *
from pacman import Pacman
from nodes import NodeGroup
from pellets import PelletGroup
from ghosts import GhostGroup
from fruit import Fruit
from pauser import Pause
from text import TextGroup
from Menus import StartMenu, RetryMenu
from pygame.locals import QUIT, KEYDOWN, K_m
from pygame.locals import QUIT, KEYDOWN, KEYUP, K_m
from sprites import LifeSprites
from sprites import MazeSprites
from mazedata import MazeData
from pygame.locals import QUIT, KEYDOWN, K_SPACE
import pygame
import sys
import os

# Mängu kontrolli klass
class GameController(object):
    def __init__(self):
        # Initsialiseerib Pygame'i ja heli
        pygame.init()
        pygame.mixer.init()
        
        # Algseadistused ja muutujad
        self.pacman_speed = 5  # algne kiirus
        self.death_sound = pygame.mixer.Sound("death-quack.wav")
        self.start_sound = pygame.mixer.Sound("menu.wav") 
        self.screen = pygame.display.set_mode(SCREENSIZE, 0, 32)
        self.background = None
        self.background_norm = None
        self.background_flash = None
        self.clock = pygame.time.Clock()
        self.fruit = None
        self.teleport = None  # Lisatud Teleport objekt
        self.pause = Pause(True)
        self.level = 0
        self.lives = 5
        self.score = 0
        self.start_time = pygame.time.get_ticks()  # Salvestab mängu alguse aja millisekundites
        self.timer_font = pygame.font.SysFont('PressStart2P-Regular.ttf', 36)
        self.timer_text = None
        self.textgroup = TextGroup()
        self.lifesprites = LifeSprites(self.lives)
        self.flashBG = False
        self.flashTime = 0.2
        self.flashTimer = 0
        self.fruitCaptured = []
        self.fruitNode = None
        self.start_time = pygame.time.get_ticks()  # Salvestab mängu alguse aja millisekundites
        self.m_key_pressed = False
        self.timer_text = None
        self.mazedata = MazeData()
        self.highscore = self.loadHighscore()

        
        
    def loadHighscore(self):
        # Kontrollib, kas kõrgeima skoori fail eksisteerib
        if not os.path.exists("high_score.txt"):
        # Kui faili pole, luuakse see ja sisestatakse sinna algväärtus 0
            with open("high_score.txt", "w") as f:
                f.write("0")
        # Avab faili ja loeb sealt kõrgeima skoori
        with open("high_score.txt", "r") as f:
            high_score = f.read().strip()  # Eemaldab tühikud ja reavahetused
            if high_score == "":
                high_score = "0"  # Kui fail on tühi, seatakse kõrgeim skoor 0-ks
            return int(high_score)

    def updateHighscore(self):
        # Kontrollib, kas mängija hetkeskoor on suurem kui kõrgeim salvestatud skoor
        if self.score > self.highscore:
            # Kui jah, uuendatakse kõrgeimat skoori ja salvestatakse see faili
            self.highscore = self.score
            with open("high_score.txt", "w") as f:
                f.write(str(self.highscore))

    def checkGhostEvents(self):
        # Kontrollib kummituste ja pacman'i kokkupõrkeid
        for ghost in self.ghosts:
            if self.pacman.collideGhost(ghost):
                # Kui pacman puutub kokku kummitusega
                if ghost.mode.current is FREIGHT:
                    # Kui kummitus on "freight" režiimis
                    self.pacman.visible = False
                    ghost.visible = False
                    self.updateScore(ghost.points)                  
                    self.textgroup.addText(str(ghost.points), WHITE, ghost.position.x, ghost.position.y, 8, time=1)
                    self.ghosts.updatePoints()
                    self.pause.setPause(pauseTime=1, func=self.showEntities)
                    ghost.startSpawn()
                    self.nodes.allowHomeAccess(ghost)
                elif ghost.mode.current is not SPAWN:
                    # Kui kummitus pole "spawn" režiimis
                    if self.pacman.alive:
                        # Kui pacman on elus
                        self.lives -=  1
                        self.lifesprites.removeImage()
                        self.pacman.die()               
                        self.ghosts.hide()
                        pygame.mixer.Sound("death-quack.wav").play()
                        if self.lives <= 0:
                            # Kui elud on otsas, lõpetatakse mäng
                            self.textgroup.showText(GAMEOVERTXT)
                            self.pause.setPause(pauseTime=3, func=self.restartGame)
                        else:
                            # Muidu alustatakse uut taset
                            self.pause.setPause(pauseTime=3, func=self.resetLevel)
   
        
    def checkFruitEvents(self):
        # Kontrollib puuviljade sündmusi
        if self.pellets.numEaten == 50 or self.pellets.numEaten == 140:
            # Kui on söödud teatud arv punkte, ilmub puuvili
            if self.fruit is None:
                self.fruit = Fruit(self.nodes.getNodeFromTiles(9, 20), self.level)
        if self.fruit is not None:
            # Kui puuviljale otsa komistatakse
            if self.pacman.collideCheck(self.fruit):
                self.updateScore(self.fruit.points)
                self.textgroup.addText(str(self.fruit.points), WHITE, self.fruit.position.x, self.fruit.position.y, 8, time=1)
                fruitCaptured = False
                for fruit in self.fruitCaptured:
                    if fruit.get_offset() == self.fruit.image.get_offset():
                        fruitCaptured = True
                        break
                if not fruitCaptured:
                    self.fruitCaptured.append(self.fruit.image)
                self.fruit = None
            elif self.fruit.destroy:
                # Kui puuvili on hävitatud
                self.fruit = None



    def setBackground(self):
        # Määra taustapildid
        self.background_norm = pygame.surface.Surface(SCREENSIZE).convert()
        self.background_norm.fill(BLACK)
        self.background_flash = pygame.surface.Surface(SCREENSIZE).convert()
        self.background_flash.fill(BLACK)
        
        # Loo mängu taustapildid vastavalt praegusele tasemele
        self.background_norm = self.mazesprites.constructBackground(self.background_norm, self.level%5)
        self.background_flash = self.mazesprites.constructBackground(self.background_flash, 5)
        
        # Lülita välja vilkumise efekt
        self.flashBG = False
        self.background = self.background_norm

    def startGame(self):
        # Alusta uut mängu
        self.invincibleMode = False
        self.beep_sound = pygame.mixer.Sound('beep.wav')
        
        # Lae uus labürint vastavalt tasemele
        self.mazedata.loadMaze(self.level)
        self.start_time = pygame.time.get_ticks()
        self.mazesprites = MazeSprites(self.mazedata.obj.name+".txt", self.mazedata.obj.name+"_rotation.txt")
        self.setBackground()
        
        # Loo mängu elemendid nagu pacman, viljad ja kummitused
        self.nodes = NodeGroup(self.mazedata.obj.name+".txt")
        self.mazedata.obj.setPortalPairs(self.nodes)
        self.mazedata.obj.connectHomeNodes(self.nodes)
        self.pacman = Pacman(self.nodes.getNodeFromTiles(*self.mazedata.obj.pacmanStart))
        self.pellets = PelletGroup(self.mazedata.obj.name+".txt")
        self.ghosts = GhostGroup(self.nodes.getStartTempNode(), self.pacman)

        # Määra kummituste algusasukohad
        self.ghosts.pinky.setStartNode(self.nodes.getNodeFromTiles(*self.mazedata.obj.addOffset(2, 3)))
        self.ghosts.inky.setStartNode(self.nodes.getNodeFromTiles(*self.mazedata.obj.addOffset(0, 3)))
        self.ghosts.clyde.setStartNode(self.nodes.getNodeFromTiles(*self.mazedata.obj.addOffset(4, 3)))
        self.ghosts.setSpawnNode(self.nodes.getNodeFromTiles(*self.mazedata.obj.addOffset(2, 3)))
        self.ghosts.blinky.setStartNode(self.nodes.getNodeFromTiles(*self.mazedata.obj.addOffset(2, 0)))

        # Keela kummitustele pääs alguspunkti ja kodu vahel
        self.nodes.denyHomeAccess(self.pacman)
        self.nodes.denyHomeAccessList(self.ghosts)

        # Määrake erisused kummituste liikumises
        self.ghosts.inky.startNode.denyAccess(RIGHT, self.ghosts.inky)
        self.ghosts.clyde.startNode.denyAccess(LEFT, self.ghosts.clyde)
        self.mazedata.obj.denyGhostsAccess(self.ghosts, self.nodes)



    def startGame_old(self):
        # Lülita välja vanade mänguhelide esitamine
        self.start_sound.stop()
        
        # Lae mängulabürint ja loo sellest sobivad spraidid
        self.mazedata.loadMaze(self.level)
        self.mazesprites = MazeSprites("maze1.txt", "maze1_rotation.txt")
        
        # Määra taustapildid
        self.setBackground()
        
        # Loo mängu sõlmed ja ühendused
        self.nodes = NodeGroup("maze1.txt")
        self.nodes.setPortalPair((0,17), (27,17))
        homekey = self.nodes.createHomeNodes(11.5, 14)
        self.nodes.connectHomeNodes(homekey, (12,14), LEFT)
        self.nodes.connectHomeNodes(homekey, (15,14), RIGHT)
        
        # Loo mängu tegelased
        self.pacman = Pacman(self.nodes.getNodeFromTiles(15, 26))
        self.pellets = PelletGroup("maze1.txt")
        self.ghosts = GhostGroup(self.nodes.getStartTempNode(), self.pacman)
        
        # Määra kummituste algusasukohad ja kodu
        self.ghosts.blinky.setStartNode(self.nodes.getNodeFromTiles(2+11.5, 0+14))
        self.ghosts.pinky.setStartNode(self.nodes.getNodeFromTiles(2+11.5, 3+14))
        self.ghosts.inky.setStartNode(self.nodes.getNodeFromTiles(0+11.5, 3+14))
        self.ghosts.clyde.setStartNode(self.nodes.getNodeFromTiles(4+11.5, 3+14))
        self.ghosts.setSpawnNode(self.nodes.getNodeFromTiles(2+11.5, 3+14))

        # Keela kummitustele pääs alguspunkti ja kodu vahel
        self.nodes.denyHomeAccess(self.pacman)
        self.nodes.denyHomeAccessList(self.ghosts)
        self.nodes.denyAccessList(2+11.5, 3+14, LEFT, self.ghosts)
        self.nodes.denyAccessList(2+11.5, 3+14, RIGHT, self.ghosts)
        self.ghosts.inky.startNode.denyAccess(RIGHT, self.ghosts.inky)
        self.ghosts.clyde.startNode.denyAccess(LEFT, self.ghosts.clyde)
        self.nodes.denyAccessList(12, 14, UP, self.ghosts)
        self.nodes.denyAccessList(15, 14, UP, self.ghosts)
        self.nodes.denyAccessList(12, 26, UP, self.ghosts)
        self.nodes.denyAccessList(15, 26, UP, self.ghosts)

    def gameOver(self):
        # Kuvame "Game Over" sõnumi koos skooriga
        self.textgroup.showText("GAME OVER", (200, 250))
        score_text = self.timer_font.render(f"Your score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (200, 300))    

    def update(self):
        # Ajavahemiku värskendamine
        dt = self.clock.tick(30) / 1000.0
        
        # Uuendage tekstigruppi ja punkte
        self.textgroup.update(dt)
        self.pellets.update(dt)
        
        # Kontrollige, kas mäng on peatatud
        if not self.pause.paused:
            # Uuendage kummitusi, vilju ja kontrollige sündmusi
            self.ghosts.update(dt)      
            if self.fruit is not None:
                self.fruit.update(dt)
            self.checkPelletEvents()
            self.checkGhostEvents()
            self.checkFruitEvents()
            self.textgroup.updateScore(self.score)
            
            # Uuendage kõrgeimat skoori
            self.updateHighscore()
        
        # Uuendage pacmanit, kui ta on elus
        if self.pacman.alive:
            if not self.pause.paused:
                self.pacman.update(dt)
        else:
            self.pacman.update(dt)

        # Välku tausta, kui vajalik
        if self.flashBG:
            self.flashTimer += dt
            if self.flashTimer >= self.flashTime:
                self.flashTimer = 0
                if self.background == self.background_norm:
                    self.background = self.background_flash
                else:
                    self.background = self.background_norm
        
        # Ajakulutamise teksti uuendamine
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - self.start_time) / 1000.0
        custom_font = pygame.font.Font('PressStart2P-Regular.ttf', 16)
        self.timer_text = custom_font.render(f"Time: {int(elapsed_time)} s", True, (255, 255, 255))
        
        # Pausi ajakohastamine ja sündmuste kontrollimine
        afterPauseMethod = self.pause.update(dt)
        if afterPauseMethod is not None:
            afterPauseMethod()
        self.checkEvents()
        
        # Renderdamine
        self.render()


    def checkEvents(self):
        # Kontrolli Pygame'i sündmusi
        for event in pygame.event.get():
            if event.type == QUIT:
                # Kui mänguaken suletakse, lõpeta mäng
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_m:
                    if not self.m_key_pressed:  # Aktiveeri vallutamise režiim ainult siis, kui see pole veel aktiveeritud
                        self.invincibleMode = True  # Aktiveeri vallutamise režiim
                        self.m_key_pressed = True  # Märgi 'm' klahvi vajutatuks
                elif event.key == K_SPACE:
                    if self.pacman.alive:
                        # Kui pacman on elus, peata mäng
                        self.pause.setPause(playerPaused=True)
                        if not self.pause.paused:
                            self.textgroup.hideText()
                            self.showEntities()
                        else:
                            self.textgroup.showText(PAUSETXT)
            elif event.type == KEYUP:  # Käitle 'm' klahvi vabastamist
                if event.key == K_m:
                    self.m_key_pressed = False
                    
    def checkPelletEvents(self):
        # Kontrolli, kas pacman sööb punkte
        pellet = self.pacman.eatPellets(self.pellets.pelletList)
        if pellet:
            self.pellets.numEaten += 1
            self.updateScore(10)
            self.updateScore(pellet.points)
            self.beep_sound.play()
            if self.pellets.numEaten == 30:
                self.ghosts.inky.startNode.allowAccess(RIGHT, self.ghosts.inky)
            if self.pellets.numEaten == 70:
                self.ghosts.clyde.startNode.allowAccess(LEFT, self.ghosts.clyde)
            self.pellets.pelletList.remove(pellet)
            if pellet.name == POWERPELLET:
                self.ghosts.startFreight()  # Alusta vallutamise režiimi
            if self.pellets.isEmpty():
                # Kui punktid on otsas, alusta uut taset
                self.flashBG = True
                self.hideEntities()
                self.pause.setPause(pauseTime=3, func=self.nextLevel)

    def checkGhostEvents(self):
        # Kontrolli, kas pacman puutub kokku kummitustega
        for ghost in self.ghosts:
            if self.pacman.collideGhost(ghost) and not self.invincibleMode:
                if ghost.mode.current is FREIGHT:
                    # Kui kummitus on vallutamise režiimis
                    self.pacman.visible = False
                    ghost.visible = False
                    self.updateScore(ghost.points)                  
                    self.textgroup.addText(str(ghost.points), WHITE, ghost.position.x, ghost.position.y, 8, time=1)
                    self.ghosts.updatePoints()
                    self.pause.setPause(pauseTime=1, func=self.showEntities)
                    ghost.startSpawn()
                    self.nodes.allowHomeAccess(ghost)
                elif ghost.mode.current is not SPAWN:
                    # Kui kummitus pole algasukohas
                    if self.pacman.alive:
                        self.lives -=  1
                        self.lifesprites.removeImage()
                        self.pacman.die()               
                        self.ghosts.hide()
                        pygame.mixer.Sound("death-quack.wav").play()
                        if self.lives <= 0:
                            self.textgroup.showText(GAMEOVERTXT)
                            self.pause.setPause(pauseTime=3, func=self.restartGame)
                        else:
                            self.pause.setPause(pauseTime=3, func=self.resetLevel)
                            
                            
    def checkFruitEvents(self):
        # Kui Pacman on söönud 50 või 140 pelletit
        if self.pellets.numEaten == 50 or self.pellets.numEaten == 140:
            # Kui puuvilja pole veel loodud
            if self.fruit is None:
                # Loo uus puuvili kindlal asukohal ja praegusel tasemel
                self.fruit = Fruit(self.nodes.getNodeFromTiles(9, 20), self.level)
                print(self.fruit)
        # Kui puuvili on olemas
        if self.fruit is not None:
            # Kui Pacman põrkub puuviljaga
            if self.pacman.collideCheck(self.fruit):
                # Uuenda skoori puuvilja punktide võrra
                self.updateScore(self.fruit.points)
                # Lisa punktid ekraanile
                self.textgroup.addText(str(self.fruit.points), WHITE, self.fruit.position.x, self.fruit.position.y, 8, time=1)
                fruitCaptured = False
                # Kontrolli, kas sama puuvili on juba kogutud
                for fruit in self.fruitCaptured:
                    if fruit.get_offset() == self.fruit.image.get_offset():
                        fruitCaptured = True
                        break
                # Kui sama puuvili pole veel kogutud, lisa see kogutud puuviljade hulka
                if not fruitCaptured:
                    self.fruitCaptured.append(self.fruit.image)
                # Eemalda puuvili mängust
                self.fruit = None
            # Kui puuvili tuleb hävitada (nt aeg on otsas), eemalda see mängust
            elif self.fruit.destroy:
                self.fruit = None

    def showEntities(self):
        # Tee Pacman ja kummitused nähtavaks
        self.pacman.visible = True
        self.ghosts.show()

    def hideEntities(self):
        # Peida Pacman ja kummitused
        self.pacman.visible = False
        self.ghosts.hide()

    def nextLevel(self):
        # Tee Pacman ja kummitused nähtavaks
        self.showEntities()
        # Suurenda taset ühe võrra
        self.level += 1
        # Peata mäng
        self.pause.paused = True
        # Alusta uut mängu
        self.startGame()
        # Uuenda taset ekraanil
        self.textgroup.updateLevel(self.level)

    def restartGame(self):
        # Määra elude arvuks 5 ja taseme numbriga 0
        self.lives = 5
        self.level = 0
        # Peata mäng
        self.pause.paused = True
        # Eemalda puuvili
        self.fruit = None
        # Alusta uut mängu
        self.startGame()
        # Nulli skoor
        self.score = 0
        # Uuenda skoori ja taset ekraanil
        self.textgroup.updateScore(self.score)
        self.textgroup.updateLevel(self.level)
        # Näita "Valmis" teksti
        self.textgroup.showText(READYTXT)
        # Taasta elude arv
        self.lifesprites.resetLives(self.lives)
        # Tühjenda kogutud puuviljade list
        self.fruitCaptured = []

    def resetLevel(self):
        # Peata mäng
        self.pause.paused = True
        # Taasta Pacmani ja kummituste algseisund
        self.pacman.reset()
        self.ghosts.reset()
        # Eemalda puuvili
        self.fruit = None
        # Näita "Valmis" teksti
        self.textgroup.showText(READYTXT)

    def updateScore(self, points):
        # Uuenda skoori
        self.score += points
        # Uuenda skoori ekraanil
        self.textgroup.updateScore(self.score)

    def render(self):
        # Joonista taustapilt
        self.screen.blit(self.background, (0, 0))
        # Täida ekraan roosa värviga
        self.screen.fill(PINK)
        # Joonista sõlmed
        self.nodes.render(self.screen)
        # Loo fondi objekt
        custom_font = pygame.font.Font('PressStart2P-Regular.ttf', 14)
        # Loo kõrgeima skoori tekst
        highscore_text = custom_font.render(f"Highscore: {self.highscore}", True, (255, 255, 255))
        # Arvuta kõrgeima skoori teksti asukoht
        highscore_rect = highscore_text.get_rect(center=(SCREENWIDTH // 2, 40))
        # Joonista kõrgeima skoori tekst ekraanile
        self.screen.blit(highscore_text, highscore_rect.topleft)
        ...
        # Arvuta ajastusteksti asukoht
        timer_rect = self.timer_text.get_rect(center=(SCREENWIDTH // 2, 10))
        # Joonista ajastustekst ekraanile
        self.screen.blit(self.timer_text, timer_rect.topleft)

        # Joonista pelletid
        self.pellets.render(self.screen)
        # Kui puuvili on olemas, joonista see
        if self.fruit is not None:
            self.fruit.render(self.screen)
        # Joonista Pacman ja kummitused
        self.pacman.render(self.screen)
        self.ghosts.render(self.screen)
        # Joonista tekstid
        self.textgroup.render(self.screen)
        # Kui elusid pole, joonista "Game Over" tekst
        if self.lives <= 0:
            # Loo uuesti mängu menüü
            retry_menu = RetryMenu()
            # Loo "Game Over" tekst
            game_over_text = self.timer_font.render("Game Over", True, WHITE)
            # Arvuta "Game Over" teksti asukoht
            text_rect = game_over_text.get_rect(center=(SCREENWIDTH // 2, SCREENHEIGHT // 2))
            # Joonista "Game Over" tekst ekraanile
            self.screen.blit(game_over_text, text_rect)

        # Joonista elude ikoonid
        for i in range(len(self.lifesprites.images)):
            x = self.lifesprites.images[i].get_width() * i
            y = SCREENHEIGHT - self.lifesprites.images[i].get_height()
            self.screen.blit(self.lifesprites.images[i], (x, y))

        # Joonista kogutud puuviljad
        for i in range(len(self.fruitCaptured)):
            x = SCREENWIDTH - self.fruitCaptured[i].get_width() * (i+1)
            y = SCREENHEIGHT - self.fruitCaptured[i].get_height()
            self.screen.blit(self.fruitCaptured[i], (x, y))

        # Uuenda ekraani
        pygame.display.update()

def main():
    # Initsialiseeri pygame
    pygame.init()
    # Loo mängu menüü
    game_menu = StartMenu()
    # Loo mängu kontroller
    game = GameController()
    # Alusta mängu
    game.startGame()
    # Mängu põhitsükkel
    while True:
        # Uuenda mängu seisundit
        game.update()
        # Joonista mängu seisund ekraanile
        game.render()
        # Uuenda ekraani
        pygame.display.flip()

# Kui skripti käivitatakse otse (mitte impordituna), käivita mäng
if __name__ == "__main__":
    main()
