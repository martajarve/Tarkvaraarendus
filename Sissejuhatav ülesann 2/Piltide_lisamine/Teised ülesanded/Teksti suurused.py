# Impordib pygame mooduli, mis sisaldab funktsioone ja klasse mängude ja muude multimeedia rakenduste loomiseks.
import pygame

# Initsialiseerib Pygame'i, mis on vajalik enne enamiku Pygame'i funktsioonide kasutamist.
pygame.init()

# Loob uue akna mõõtmetega 640x480 pikslit.
screen=pygame.display.set_mode([640,480])

# Seab loodud akna pealkirjaks "Harjutamine".
pygame.display.set_caption("Harjutamine")

# Värvib akna tausta kindla värviga, kasutades RGB värvikoodi [204, 255, 204] (hele roheline).
screen.fill([204, 255, 204])

# Loob fondi objekti, kasutades Ariali fonti suurusega 50.
# pygame.font.match_font('arial') otsib süsteemist Arial fonti, tagades fonti olemasolu.
font = pygame.font.Font(pygame.font.match_font('arial'), 50)

# Renderdab teksti "Hello PyGame" antud fondiga, musta värvi ([0,0,0]) ja läbipaistmatu taustaga.
# `True` argument lubab anti-aliasing'u, muutes teksti visuaalselt sujuvamaks.
text = font.render("Hello PyGame", True, [0,0,0])

# Arvutab tekstikasti laiuse ja kõrguse, et seda teavet hiljem kasutada.
# Siin seda infot otseselt ei kasutata, kuna teksti asukoht on fikseeritud.
text_width = text.get_rect().width
text_height = text.get_rect().height

# Asetab teksti ekraanile koordinaatidele [320,240].
# Erinevalt eelmisest näitest, kus tekst paigutati dünaamiliselt keskele, on siin teksti asukoht fikseeritud.
screen.blit(text, [320,240])

# Uuendab ekraani sisu, et kuvada eelnevalt ekraanile lisatud tekst.
pygame.display.flip()

# Käivitab lõputu sündmuste kuulamise tsükli.
while True:
    # Ootab sündmuste järjekorras uut sündmust. Kui sündmus on akna sulgemine (QUIT),
    # katkestatakse tsükkel ja programm lõpetatakse.
    if pygame.event.wait().type == pygame.QUIT:
        break

# Sulgeb Pygame'i ja vabastab kasutatud ressursid.
pygame.quit()

