import pygame
pygame.init()
#ekraani seaded
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("Hulknurk-Marta Järve")
screen.fill([204, 255, 255])

pygame.draw.polygon(screen, [255, 200, 255], [[50,50],[100,50],[100,150],[250,50],[350,250],[50,250]], 2)
pygame.display.flip()                       #värskendame ekraani

while True:
    if pygame.event.wait().type == pygame.QUIT:
        break
pygame.quit()
