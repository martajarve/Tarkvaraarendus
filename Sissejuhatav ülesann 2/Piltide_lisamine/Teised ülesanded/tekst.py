# Impordib pygame mooduli. Pygame pakub mängude ja multimeedia rakenduste loomiseks vajalikke funktsioone ja klasse.
import pygame

# Initsialiseerib Pygame'i. See rida on vajalik enne Pygame'i teiste funktsioonide kasutamist.
pygame.init()

# Loob uue akna mõõtmetega 640x480 pikslit ja seab selle muutuja `screen` väärtuseks.
screen=pygame.display.set_mode([640,480])

# Määrab loodud akna pealkirjaks "Harjutamine".
pygame.display.set_caption("Harjutamine")

# Värvib akna tausta kindla värviga, antud juhul heleda rohelisega, kasutades RGB värvikoodi [204, 255, 204].
screen.fill([204, 255, 204])

# Loob uue fondi objekti. Kuna `Font` esimene argument on `None`, kasutab Pygame vaikimisi süsteemifonti.
# Teine argument `30` määrab fondi suuruseks 30 punkti.
font = pygame.font.Font(None, 30)

# Kasutab fondi objekti, et luua uus tekstipilt. See renderdab antud sõne "Hello PyGame"
# antialiasinguga (True), musta värvi ([0,0,0]) ja läbipaistmatu taustaga.
text = font.render("Hello PyGame", True, [0,0,0])

# Asetab tekstipildi ekraanile koordinaatidele [200,200]. 
# See tähendab, et teksti vasak ülemine nurk asetseb 200 pikslit paremale ja 200 pikslit allapoole akna vasakust ülanurgast.
screen.blit(text, [200,200])

# Uuendab ekraani sisu, et kuvada eelnevalt ekraanile blititud tekst.
pygame.display.flip()

# Jooksutab mängutsüklit lõpmatult. See osa koodist tagab, et programm jookseb,
# kuni kasutaja sulgeb akna.
while True:
    # Ootab sündmuste järjekorras uut sündmust. Kui sündmus on QUIT tüüpi (akna sulgemine),
    # katkestatakse tsükkel.
    if pygame.event.wait().type == pygame.QUIT:
        break

# Kutsutakse välja, et korralikult lõpetada Pygame'i töö ja vabastada ressursid.
pygame.quit()
