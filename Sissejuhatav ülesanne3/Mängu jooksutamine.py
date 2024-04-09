# Impordime Pygame'i mooduli
import pygame

# Impordime sys mooduli, mis sisaldab funktsioone nagu sys.exit()
import sys

# Initsialiseerime Pygame'i
pygame.init()

# Määrame mõned värvid RGB kujul nimega lGreen ja lBlue
lGreen = [120, 200, 113]
lBlue = [153, 204, 255]

# Seame ekraani suuruse
screen = pygame.display.set_mode([640,480])

# Seame ekraanile pealkirja
pygame.display.set_caption("Harjutamine")

# Täidame ekraani rohelise värviga
screen.fill(lGreen)

# Algseisus pole mäng veel lõppenud
gameover = False

# Seni kuni mäng pole lõppenud
while not gameover:
    # Lisame pildi nimega "corgi.jpg"
    corgi = pygame.image.load("corgi.jpg")
    # Muudame pildi suurust
    corgi = pygame.transform.scale(corgi, [300, 250])
    # Lisame pildi ekraanile konkreetsele positsioonile
    screen.blit(corgi, [180,100])

    # Värskendame ekraani
    pygame.display.flip()

    # Käsitleme sündmusi, näiteks mängu sulgemist
    for event in pygame.event.get():
        # Kui sündmus on mängu sulgemine (risti vajutamine)
        if event.type == pygame.QUIT:
            # Väljume programmist
            sys.exit()

# Lõpetame Pygame'i kasutamise
pygame.quit()
