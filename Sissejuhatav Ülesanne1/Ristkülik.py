import pygame
pygame.init()
#ekraani seaded
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("Ristkülik-Marta Järve")
screen.fill([204, 255, 255])

pygame.draw.rect(screen, [92, 225, 0], [50, 80, 200, 300], 2)
pygame.display.flip()                       #värskendame ekraani

while True:
    if pygame.event.wait().type == pygame.QUIT:
        break
pygame.quit()
