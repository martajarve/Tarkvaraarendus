import pygame
pygame.init()

# Ekraani seaded
#Määrab ekraani suuruse
screen=pygame.display.set_mode([300,300])
#Paneb nime ekraanile
pygame.display.set_caption("Foor-Marta Järve")
screen.fill([0, 0, 0])
# Joonistab halli ristküliku
pygame.draw.rect(screen, [153, 153, 153], [100, 10, 100, 270], 2)
# joonistab punase palli
pygame.draw.circle(screen, [255, 0, 0], [150,60], 40, 0)
# Joonistab Kollase ringi
pygame.draw.circle(screen, [255, 255, 0], [150,145], 40, 0)
# Joonistan rohelise ringi
pygame.draw.circle(screen, [102, 255, 51], [150,230], 40, 0)
pygame.display.flip()
                     
while True:
    if pygame.event.wait().type == pygame.QUIT:
        break
pygame.quit()
