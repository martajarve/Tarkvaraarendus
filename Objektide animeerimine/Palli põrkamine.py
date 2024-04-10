import pygame, sys
# Impordime pygame'i ja sys moodulid, mida hiljem kasutame.

pygame.init()
# Initsialiseerime pygame'i, et saaksime kasutada selle pakutavaid funktsioone.

# Värvid
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
lBlue = [153, 204, 255]
# Määratleme erinevad värvid RGB (red, green, blue) väärtustena.

# Ekraani seaded
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Animeerimine")
screen.fill(lBlue)
clock = pygame.time.Clock()
# Seadistame ekraani suuruse, pealkirja, täidame ekraani helesinise värviga ning seadistame mängukella.

# Graafika laadimine
ball = pygame.image.load("pall.png")
ball = pygame.transform.scale(ball, [50, 40])
# Laeme pildi "pall.png" ning muudame selle suurust.

# Kiirus ja asukoht
posX, posY = 0, 0
speedX, speedY = 3, 4
# Määrame palli algasukoha ja selle kiirused x- ja y-telgedel.

gameover = False
while not gameover:
    # Loop, mis kestab seni kuni gameover muutuja väärtus on False.

    # FPS
    clock.tick(60)
    # Piirame värskenduste kiirust 60 kaadriga sekundis.

    # Mängu sulgemine ristist
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()
    # Käsitseme sündmusi, sealhulgas akna sulgemist (QUIT).

    # Pildi lisamine ekraanile
    screen.blit(ball, (posX, posY))

    posX += speedX
    posY += speedY
    # Lisame palli ekraanile ning uuendame palli x- ja y-koordinaate vastavalt kiirustele.

    # Kui pall jõuab äärteni, muudab suunda
    if posX > screenX - ball.get_rect().width or posX < 0:
        speedX = -speedX

    if posY > screenY - ball.get_rect().height or posY < 0:
        speedY = -speedY
    # Kontrollime, kas pall on ääristega põrkamas ja vajadusel muudame selle liikumissuunda.

    # Graafika kuvamine ekraanil
    pygame.display.flip()
    screen.fill(lBlue)
    # Värskendame ekraani ja täidame selle taustavärviga.

pygame.quit()
# Lõpetame pygame'i kasutamise korrektselt.
