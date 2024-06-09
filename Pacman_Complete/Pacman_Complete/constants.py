# Mängulaua mõõtmed ja suuruse arvutamine vastavalt plaatidele
TILEWIDTH = 16
TILEHEIGHT = 16
NROWS = 36
NCOLS = 28
SCREENWIDTH = NCOLS*TILEWIDTH
SCREENHEIGHT = NROWS*TILEHEIGHT
SCREENSIZE = (SCREENWIDTH, SCREENHEIGHT)

# Värvide defineerimine RGB kujul
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PINK = (255,100,150)
TEAL = (100,255,255)
ORANGE = (230,190,40)
GREEN = (0, 255, 0)

# Suunakoodid
STOP = 0
UP = 1
DOWN = -1
LEFT = 2
RIGHT = -2
PORTAL = 3

# Objektide tüüpide määramine
PACMAN = 0
PELLET = 1
POWERPELLET = 2
GHOST = 3
BLINKY = 4
PINKY = 5
INKY = 6
CLYDE = 7
FRUIT = 8

# Kummituste käitumise olekud
SCATTER = 0
CHASE = 1
FREIGHT = 2
SPAWN = 3

# Tekstitüüpide määramine
SCORETXT = 0
LEVELTXT = 1
READYTXT = 2
PAUSETXT = 3
GAMEOVERTXT = 4
