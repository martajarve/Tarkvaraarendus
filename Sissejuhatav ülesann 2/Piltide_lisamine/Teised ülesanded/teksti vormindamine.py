# Impordib pygame mooduli, mis on komplekt funktsioone ja klasse, mida saab kasutada mängude loomiseks.
import pygame

# Initsialiseerib Pygame'i, mis on vajalik enne Pygame'i teiste osade kasutamist.
pygame.init()

# Määrab ekraani seaded, loob uue akna mõõtmetega 640x480 pikslit.
screen=pygame.display.set_mode([640,480])

# Seab akna pealkirjaks "Harjutamine".
pygame.display.set_caption("Harjutamine")

# Värvib ekraani tausta roheliseks RGB värvikoodiga [204, 255, 204].
screen.fill([204, 255, 204])

# Loob fondi objekti, kasutades süsteemis olevat Arial fonti suurusega 50. 
# Kui Arial fonti ei leita, valib Pygame automaatselt lähima vastava fondi.
font = pygame.font.Font(pygame.font.match_font('arial'), 50)

# Määrab loodud fondile alakriipsu.
font.set_underline(True)

# Loob tekstiobjekti, mille sisuks on "Hello PyGame". Teksti värv on must ([0,0,0]).
# Teine argument (True) määrab, et tekst renderdatakse anti-aliased, muutes selle visuaalselt sujuvamaks.
text = font.render("Hello PyGame", True, [0,0,0])

# Saadab tekstiobjekti laiuse.
text_width = text.get_rect().width

# Saadab tekstiobjekti kõrguse.
text_height = text.get_rect().height

# Asetab teksti ekraani keskele. 
# Ekraani laiuse ja kõrguse poolest lahutatakse teksti laiuse ja kõrguse pool, 
# et teksti keskpunkt langeks akna keskpunktiga kokku.
screen.blit(text, [320-text_width/2,240-text_height/2])

# Uuendab kogu ekraani sisu, et kuvada tehtud muudatusi.
pygame.display.flip()

# Jooksutab mängutsüklit lõpmatult, kuni kasutaja otsustab akna sulgeda.
while True:
    # Ootab sündmuste järjekorras uut sündmust. 
    # Kui saabub QUIT sündmus (akna sulgemine), katkestatakse tsükkel.
    if pygame.event.wait().type == pygame.QUIT:
        break

# Sulgeb Pygame'i, vabastades kasutatud ressursid.
pygame.quit()
