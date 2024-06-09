import pygame # Importib pygame'i mooduli.
from pygame.locals import * # Importib pygame'i konstandid.
from vector import Vector2 # Impordib Vector2 klassi.
from constants import * # Importib konstandid.
from entity import Entity # Impordib Entity klassi.
from modes import ModeController # Impordib ModeController klassi.
from sprites import GhostSprites # Impordib GhostSprites klassi.

class Ghost(Entity): # Määratleb Ghost klassi, mis pärib Entity klassist.
    def __init__(self, node, pacman=None, blinky=None): # Konstruktor, mis initsialiseerib Ghost objekti.
        Entity.__init__(self, node) # Kutsutakse välja Entity klassi konstruktor.
        self.name = GHOST # Määrab Ghost objekti nimeks GHOST.
        self.points = 200 # Määrab punktide arvu.
        self.goal = Vector2() # Initsialiseerib eesmärgi.
        self.directionMethod = self.goalDirection # Määrab suunamise meetodi.
        self.pacman = pacman # Seab pacmani.
        self.mode = ModeController(self) # Loob režiimikontrolleri objekti.
        self.blinky = blinky # Seab blinky.
        self.homeNode = node # Seab kodunode.

    def reset(self): # Funktsioon Ghost objekti lähtestamiseks.
        Entity.reset(self) # Kutsutakse välja Entity klassi reset meetod.
        self.points = 200 # Lähtestab punktide arvu.
        self.directionMethod = self.goalDirection # Lähtestab suunamise meetodi.

    def update(self, dt): # Funktsioon Ghost objekti uuendamiseks.
        self.sprites.update(dt) # Uuendab sprite'e.
        self.mode.update(dt) # Uuendab režiimi.
        if self.mode.current is SCATTER: # Kui režiim on SCATTER.
            self.scatter() # Käivitab scatter meetodi.
        elif self.mode.current is CHASE: # Kui režiim on CHASE.
            self.chase() # Käivitab chase meetodi.
        Entity.update(self, dt) # Kutsutakse välja Entity klassi update meetod.

    def scatter(self): # Funktsioon scatter meetodi jaoks.
        self.goal = Vector2() # Lähtestab eesmärgi.

    def chase(self): # Funktsioon chase meetodi jaoks.
        self.goal = self.pacman.position # Seab eesmärgiks pacmani positsiooni.

    def spawn(self): # Funktsioon spawn meetodi jaoks.
        self.goal = self.spawnNode.position # Seab eesmärgiks spawni positsiooni.

    def setSpawnNode(self, node): # Funktsioon spawn node'i määramiseks.
        self.spawnNode = node # Määrab spawn node'i.

    def startSpawn(self): # Funktsioon spawn režiimi käivitamiseks.
        self.mode.setSpawnMode() # Seab spawn režiimi.
        if self.mode.current == SPAWN: # Kui režiimiks on SPAWN.
            self.setSpeed(150) # Seab kiiruseks 150.
            self.directionMethod = self.goalDirection # Seab suunamise meetodi.
            self.spawn() # Käivitab spawn meetodi.

    def startFreight(self): # Funktsioon freight režiimi käivitamiseks.
        self.mode.setFreightMode() # Seab freight režiimi.
        if self.mode.current == FREIGHT: # Kui režiimiks on FREIGHT.
            self.setSpeed(50) # Seab kiiruseks 50.
            self.directionMethod = self.randomDirection # Seab suunamise meetodi.

    def normalMode(self): # Funktsioon normaalse režiimi jaoks.
        self.setSpeed(100) # Seab kiiruseks 100.
        self.directionMethod = self.goalDirection # Seab suunamise meetodi.
        self.homeNode.denyAccess(DOWN, self) # Keelab alla liikumise kodunodes.


class Blinky(Ghost):
    def __init__(self, node, pacman=None, blinky=None):
        Ghost.__init__(self, node, pacman, blinky)
        self.name = BLINKY
        self.color = RED
        self.sprites = GhostSprites(self)


class Blinky(Ghost): # Määratleb Blinky klassi, mis pärib Ghost klassist.
    def __init__(self, node, pacman=None, blinky=None): # Konstruktor, mis initsialiseerib Blinky objekti.
        Ghost.__init__(self, node, pacman, blinky) # Kutsutakse välja Ghost klassi konstruktor.
        self.name = BLINKY # Määrab Blinky objekti nimeks BLINKY.
        self.color = RED # Määrab värvi punaseks.
        self.sprites = GhostSprites(self) # Loob GhostSprites objekti.

class Pinky(Ghost): # Määratleb Pinky klassi, mis pärib Ghost klassist.
    def __init__(self, node, pacman=None, blinky=None): # Konstruktor, mis initsialiseerib Pinky objekti.
        Ghost.__init__(self, node, pacman, blinky) # Kutsutakse välja Ghost klassi konstruktor.
        self.name = PINKY # Määrab Pinky objekti nimeks PINKY.
        self.color = PINK # Määrab värvi roosaks.
        self.sprites = GhostSprites(self) # Loob GhostSprites objekti.
        
    def scatter(self): # Funktsioon scatter meetodi jaoks.
        self.goal = Vector2(TILEWIDTH*NCOLS, 0) # Seab eesmärgiks mänguvälja parema ülanurga.

    def chase(self): # Funktsioon chase meetodi jaoks.
        self.goal = self.pacman.position + self.pacman.directions[self.pacman.direction] * TILEWIDTH * 4 # Seab eesmärgiks pacmani positsiooni pluss mõned ühikud tema liikumissuunas.

class Inky(Ghost): # Määratleb Inky klassi, mis pärib Ghost klassist.
    def __init__(self, node, pacman=None, blinky=None): # Konstruktor, mis initsialiseerib Inky objekti.
        Ghost.__init__(self, node, pacman, blinky) # Kutsutakse välja Ghost klassi konstruktor.
        self.name = INKY # Määrab Inky objekti nimeks INKY.
        self.color = TEAL # Määrab värvi tealseks.
        self.sprites = GhostSprites(self) # Loob GhostSprites objekti.

    def scatter(self): # Funktsioon scatter meetodi jaoks.
        self.goal = Vector2(TILEWIDTH*NCOLS, TILEHEIGHT*NROWS) # Seab eesmärgiks mänguvälja parema alumise nurga.

    def chase(self): # Funktsioon chase meetodi jaoks.
        vec1 = self.pacman.position + self.pacman.directions[self.pacman.direction] * TILEWIDTH * 2 # Leiab vektori pacmani ja tema liikumissuuna põhjal.
        vec2 = (vec1 - self.blinky.position) * 2 # Leiab teise vektori blinky positsiooni põhjal.
        self.goal = self.blinky.position + vec2 # Seab eesmärgiks blinky positsiooni pluss teine vektor.

class Clyde(Ghost): # Määratleb Clyde klassi, mis pärib Ghost klassist.
    def __init__(self, node, pacman=None, blinky=None): # Konstruktor, mis initsialiseerib Clyde objekti.
        Ghost.__init__(self, node, pacman, blinky) # Kutsutakse välja Ghost klassi konstruktor.
        self.name = CLYDE # Määrab Clyde objekti nimeks CLYDE.
        self.color = ORANGE # Määrab värvi oranžiks.
        self.sprites = GhostSprites(self) # Loob GhostSprites objekti.

    def scatter(self): # Funktsioon scatter meetodi jaoks.
        self.goal = Vector2(0, TILEHEIGHT*NROWS) # Seab eesmärgiks mänguvälja vasaku alumise nurga.

    def chase(self): # Funktsioon chase meetodi jaoks.
        d = self.pacman.position - self.position # Leiab vektori pacmani ja oma positsiooni vahel.
        ds = d.magnitudeSquared() # Leiab vektori pikkuse ruudu.
        if ds <= (TILEWIDTH * 8)**2: # Kui vektori pikkuse ruut on väiksem või võrdne 8 mänguvälja ruuduga.
            self.scatter() # Käivitab scatter meetodi.
        else:
            self.goal = self.pacman.position + self.pacman.directions[self.pacman.direction] * TILEWIDTH * 4 # Seab eesmärgiks pacmani positsiooni pluss mõned ühikud tema liikumissuunas.

class GhostGroup(object): # Määratleb GhostGroup klassi.
    def __init__(self, node, pacman): # Konstruktor, mis initsialiseerib GhostGroup objekti.
        self.blinky = Blinky(node, pacman) # Loob Blinky objekti.
        self.pinky = Pinky(node, pacman) # Loob Pinky objekti.
        self.inky = Inky(node, pacman, self.blinky) # Loob Inky objekti.
        self.clyde = Clyde(node, pacman) # Loob Clyde objekti.
        self.ghosts = [self.blinky, self.pinky, self.inky, self.clyde] # Loob listi kõikidest kummitustest.

    def __iter__(self): # Funktsioon, mis lubab GhostGroup objekti itereerida.
        return iter(self.ghosts) # Tagastab itereeritava objekti.

    def update(self, dt): # Funktsioon, mis uuendab kõiki kummitusi.
        for ghost in self: # Iterateerib kõikide kummituste üle.
            ghost.update(dt) # Käivitab kummituse uuendamise.

    def startFreight(self): # Funktsioon, mis käivitab kõikidel kummitustel freight režiimi.
        for ghost in self: # Iterateerib kõikide kummituste üle.
            ghost.startFreight() # Käivitab kummituse freight režiimi.
        self.resetPoints() # Lähtestab punktid.


    def setSpawnNode(self, node): # Funktsioon, mis seab kõikide kummituste spawn node'i.
        for ghost in self: # Iterateerib kõikide kummituste üle.
            ghost.setSpawnNode(node) # Käivitab kummituse setSpawnNode funktsiooni.

    def updatePoints(self): # Funktsioon, mis uuendab kõikide kummituste punktisummat.
        for ghost in self: # Iterateerib kõikide kummituste üle.
            ghost.points *= 2 # Uuendab kummituse punktisummat, kahekordistades selle.

    def resetPoints(self): # Funktsioon, mis lähtestab kõikide kummituste punktisumma algväärtuseks.
        for ghost in self: # Iterateerib kõikide kummituste üle.
            ghost.points = 200 # Lähtestab kummituse punktisumma väärtuseks 200.

    def hide(self): # Funktsioon, mis peidab kõikide kummituste sprite'id.
        for ghost in self: # Iterateerib kõikide kummituste üle.
            ghost.visible = False # Seab kummituse sprite'i nähtavuse väärtuseks väär.

    def show(self): # Funktsioon, mis näitab kõikide kummituste sprite'id.
        for ghost in self: # Iterateerib kõikide kummituste üle.
            ghost.visible = True # Seab kummituse sprite'i nähtavuse väärtuseks tõene.

    def reset(self): # Funktsioon, mis lähtestab kõikide kummituste oleku algväärtuseks.
        for ghost in self: # Iterateerib kõikide kummituste üle.
            ghost.reset() # Käivitab kummituse reset funktsiooni.

    def render(self, screen): # Funktsioon, mis renderdab kõikide kummituste sprite'id ekraanile.
        for ghost in self: # Iterateerib kõikide kummituste üle.
            ghost.render(screen) # Käivitab kummituse render funktsiooni, et sprite'i ekraanile joonistada.
