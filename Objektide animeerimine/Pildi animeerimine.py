import pygame, sys
# Impordime vajalikud moodulid: pygame ja sys.
pygame.init()
# Initsialiseerime pygame'i, et saaksime kasutada selle pakutavaid funktsioone.

# Värvid
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
lBlue = [153, 204, 255]
# Defineerime erinevad värvid RGB (red, green, blue) väärtustena.

# Ekraani seaded
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Animeerimine")
screen.fill(lBlue)
clock = pygame.time.Clock()
# Määrame ekraani suuruse, pealkirja, täidame ekraani helesinise värviga ning seadistame mängukella.

# Graafika laadimine
ball = pygame.image.load("pall.png")
ball = pygame.transform.scale(ball, [50, 40])
# Laadime pildi "pall.png" ning muudame selle suurust.

# Kiirus ja asukoht
posX, posY = 0, 0
speedX = 4
# Määratleme palli algasukoha ja selle kiiruse.

gameover = False
while not gameover:
    # Loop, mis kestab seni kuni gameover muutuja väärtus on False.
    clock.tick(60)
    # Piirame värskenduste kiirust 60 kaadriga sekundis.
    
    # Mängu sulgemine ristist
    events = pygame.event.get()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
    # Käsitseme sündmusi, sealhulgas akna sulgemist (QUIT).

    # Pildi lisamine ekraanile
    screen.blit(ball, (posX, posY))
    posX += speedX
    # Lisame palli ekraanile ning uuendame palli x-koordinaati vastavalt kiirusele.
    
    # Graafika kuvamine ekraanil
    pygame.display.flip()
    screen.fill(lBlue)
    # Värskendame ekraani ja täidame selle taustavärviga.

while True:
    # Tsükkel, mis kestab lõpmatuseni.
    
    # Ootame sündmust (nt kasutaja akna sulgemist)
    if pygame.event.wait().type == pygame.QUIT:  
        # Kui kasutaja sulgeb akna, katkestame tsükli.
        break  

pygame.quit()
# Lõpetame pygame'i kasutamise korrektselt.
