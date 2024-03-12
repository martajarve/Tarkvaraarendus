import pygame
pygame.init()
#ekraani seaded
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("Joon-Marta Järve")
screen.fill([204, 255, 255])

#joonistamine
pygame.draw.line(screen, [255,0,0], [100,100], [200,200], 2)

pygame.display.flip()
while True:
    if pygame.event.wait().type == pygame.QUIT:
        break
pygame.quit()

