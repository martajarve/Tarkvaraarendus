import pygame
pygame.init()

# Ekraani seaded
#Määrab ekraani suuruse
screen=pygame.display.set_mode([300,300])
#Paneb nime ekraanile
pygame.display.set_caption("Lumemees-Marta Järve")
screen.fill([153, 204, 255])

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

#Joonistan käe
pygame.draw.line(screen, [102,51,0], [115,120], [40,140], 2)
#Joonistan teise käe
pygame.draw.line(screen, [102,51,0], [185,120], [255,140], 2)

# Joonistan nööbi
pygame.draw.circle(screen, [0, 0, 0], [150,115], 5, 0)
#joonistan teise nööbi
pygame.draw.circle(screen, [0, 0, 0], [150,140], 5, 0)
# Joonistan kolmanda nööbi
pygame.draw.circle(screen, [0, 0, 0], [150,165], 5, 0)

# Joonistan mütsi
pygame.draw.polygon(screen, [255 , 0, 255], [[170,50],[130,50],[150,10]],0 )

# Joonistan Päikese
pygame.draw.circle(screen, [255, 255, 0], [250,30], 20, 0)

# Joonistan päikesekiired
pygame.draw.line(screen, [255,255,0], [243,60], [240,80], 2)
# Joonistan päikesekiired
pygame.draw.line(screen, [255,255,0], [263,55], [280,75], 2)
# Joonistan päikesekiired
pygame.draw.line(screen, [255,255,0], [230,50], [215,65], 2)
# Joonistan päikesekiired
pygame.draw.line(screen, [255,255,0], [280,40], [350,85], 2)
# Joonistan päikesekiired
pygame.draw.line(screen, [255,255,0], [280,20], [370,10], 2)

# Joonistan pilve
pygame.draw.circle(screen, [255, 255, 255], [230,30], 15, 0)
# Joonistan pilve
pygame.draw.circle(screen, [255, 255, 255], [220,20], 15, 0)
# Joonistan pilve
pygame.draw.circle(screen, [255, 255, 255], [240,10], 15, 0)
# Joonistan pilve
pygame.draw.circle(screen, [255, 255, 255], [210,35], 15, 0)
# Joonistan pilve
pygame.draw.circle(screen, [255, 255, 255], [210,10], 15, 0)
# Joonistan pilve
pygame.draw.circle(screen, [255, 255, 255], [190,20], 15, 0)

# Joonistan pilve 2
pygame.draw.circle(screen, [255, 255, 255], [130,30], 15, 0)
# Joonistan pilve 2
pygame.draw.circle(screen, [255, 255, 255], [120,20], 15, 0)
# Joonistan pilve 2
pygame.draw.circle(screen, [255, 255, 255], [140,10], 15, 0)
# Joonistan pilve 2
pygame.draw.circle(screen, [255, 255, 255], [110,35], 15, 0)
# Joonistan pilve 2
pygame.draw.circle(screen, [255, 255, 255], [110,10], 15, 0)
# Joonistan pilve 2
pygame.draw.circle(screen, [255, 255, 255], [90,20], 15, 0)

# Joonistan mütsi
pygame.draw.polygon(screen, [255 , 0, 255], [[170,50],[130,50],[150,10]],0 )

# Joonistan pilve 3
pygame.draw.circle(screen, [255, 255, 255], [30,40], 15, 0)
# Joonistan pilve 3
pygame.draw.circle(screen, [255, 255, 255], [20,30], 15, 0)
# Joonistan pilve 3
pygame.draw.circle(screen, [255, 255, 255], [40,30], 15, 0)
# Joonistan pilve 3
pygame.draw.circle(screen, [255, 255, 255], [10,45], 15, 0)
# Joonistan pilve 3
pygame.draw.circle(screen, [255, 255, 255], [10,20], 15, 0)
# Joonistan pilve 3
pygame.draw.circle(screen, [255, 255, 255], [9,20], 15, 0)

# Teen harjavarre
pygame.draw.line(screen, [102,51,0], [40,30], [50,240], 4)
# Joonistan harjaotsa
pygame.draw.polygon(screen, [255, 217, 102], [[30,25],[10,25],[40,70],[50,60],[70,15]], 0)


pygame.display.flip()


while True:
    if pygame.event.wait().type == pygame.QUIT:
        break
pygame.quit()
