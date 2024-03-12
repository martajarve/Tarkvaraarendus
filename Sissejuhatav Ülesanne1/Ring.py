import pygame
pygame.init()
#ekraani seaded
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("Ring-Marta Järve")
screen.fill([204, 255, 255])

pygame.draw.circle(screen, [70, 200, 255], [300,150], 100, 1)
pygame.display.flip()                       #värskendame ekraani

while True:
    if pygame.event.wait().type == pygame.QUIT:
        break
pygame.quit()
