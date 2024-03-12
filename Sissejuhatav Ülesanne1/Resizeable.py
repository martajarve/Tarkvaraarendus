import pygame
pygame.init()

screen=pygame.display.set_mode([640,480], pygame.RESIZABLE)
pygame.display.set_caption("My Screen")

while True:
    if pygame.event.wait().type == pygame.QUIT:
        break
pygame.quit()
