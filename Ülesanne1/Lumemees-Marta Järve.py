import pygame
pygame.init()

# Ekraani seaded
#Määrab ekraani suuruse
screen=pygame.display.set_mode([300,300])
#Paneb nime ekraanile
pygame.display.set_caption("Lumemees-Marta Järve")
screen.fill([0, 0, 0])

#joonistan alumise valge ringi
pygame.draw.circle(screen, [255, 255, 255], [150,220], 50, 0)
#joonistan keskmise valge ringi
pygame.draw.circle(screen, [255, 255, 255], [150,140], 40, 0)
#joonistan lumemehe pea
pygame.draw.circle(screen, [255, 255, 255], [150,75], 30, 0)
#joonistan ühe silma
pygame.draw.circle(screen, [0, 0, 0], [140,70], 5, 0)
#joonistan teise silma
pygame.draw.circle(screen, [0, 0, 0], [160,70], 5, 0)
#joonistan kolmnurkse nina lumemehele
pygame.draw.polygon(screen, [255 , 0, 0], [[155,80],[145,80],[150,95]],0 )

pygame.display.flip()
                     
while True:
    if pygame.event.wait().type == pygame.QUIT:
        break
pygame.quit()
