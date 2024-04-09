# Defineerime funktsiooni drawHouse, mis joonistab maja antud koordinaatidele ja suurustele
def drawHouse(x, y, width, height, screen, color):
    # Määratleme punktid, mis moodustavad maja jooned. Punktid on esitatud listina.
    points = [(x,y- ((3/4.0) * height)), (x,y), (x+width,y), (x+width,y-(3/4.0) * height), 
        (x,y- ((3/4.0) * height)), (x + width/2.0,y-height), (x+width,y-(3/4.0)*height)]
    # Määrame joonte paksuse
    lineThickness = 2
    # Joonistame maja punktide järgi kasutades draw.lines meetodit
    pygame.draw.lines(screen, color, False, points, lineThickness)

import pygame
import sys
import random 
pygame.init()

#värvid
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]

#ekraani seaded
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("Harjutamine")
screen.fill(lGreen)

#funktsioonid
def drawHouse(x, y, width, height, screen, color):
    points = [(x,y- ((3/4.0) * height)), (x,y), (x+width,y), (x+width,y-(3/4.0) * height), 
        (x,y- ((3/4.0) * height)), (x + width/2.0,y-height), (x+width,y-(3/4.0)*height)]
    lineThickness = 2
    pygame.draw.lines(screen, color, False, points, lineThickness)

#kutsun funktsiooni välja
drawHouse(100,400,300,200,screen, blue)
    
pygame.display.flip()

# Loop, mis töötab seni, kuni kasutaja sulgeb akna
while True:
    if pygame.event.wait().type == pygame.QUIT:  # Oodake, kuni kasutaja sulgeb akna
        break  # Katkesta tsükkel, kui kasutaja sulgeb akna


pygame.quit()