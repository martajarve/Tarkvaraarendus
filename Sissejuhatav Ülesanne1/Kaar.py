import pygame
pygame.init()
#ekraani seaded
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("Kaar-Marta Järve")
screen.fill([204, 255, 255])

pygame.draw.arc(screen,[0,0,0], [100,100,250,200], 0, 3.14*1.5, 1)
pygame.display.flip()                      #värskendame ekraani

while True:
    if pygame.event.wait().type == pygame.QUIT:
        break
pygame.quit()
