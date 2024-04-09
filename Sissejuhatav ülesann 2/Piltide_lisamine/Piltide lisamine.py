# Impordib Pygame mooduli, mis on populaarne teek multimeedia ja mängude arendamiseks Pythonis.
import pygame

# Alustab Pygame'i, et kasutada selle graafika ja sündmuste käitlemise funktsioone.
pygame.init()

# Loob uue akna mõõtmetega 1200x1200 pikslit.
screen=pygame.display.set_mode([1200,1200])

# Seab akna pealkirjaks "Harjutamine".
pygame.display.set_caption("Harjutamine")

# Värvib akna tausta roheliseks kasutades RGB värvikoodi [204, 255, 204].
screen.fill([204, 255, 204])

# Laeb pildifaili nimega "corgi.jpg" muutujasse `bg`. See on tõenäoliselt koerapilt.
bg = pygame.image.load("corgi.jpg")

# Asetab taustapildi `bg` ekraani ülemisse vasakusse nurka koordinaatidel [0,0].
screen.blit(bg,[0,0])

# Laeb teise pildifaili nimega "hello.png" muutujasse `tekst`. See võib olla mistahes pilt, mis sisaldab teksti.
tekst = pygame.image.load("hello.png")

# Muudab tekstipildi suurust 400x400 pikslile. See on kasulik, kui soovid pildi suurust ekraanil muuta.
tekst = pygame.transform.scale(tekst, [400, 400])

# Asetab suuruse muudetud tekstipildi ekraanile koordinaatidel [400,550].
# See tähendab, et pildi vasak ülemine nurk asub 400 pikslit ekraani vasakust servast
# ja 550 pikslit ekraani ülemisest servast.
screen.blit(tekst,[400,550])

# Uuendab ekraani sisu, et kuvada eelnevalt ekraanile lisatud pildid.
pygame.display.flip()

# Käivitab lõputu tsükli, mis ootab sündmust, nagu akna sulgemine.
while True:
    # Kontrollib sündmuseid. Kui avastatakse QUIT sündmus (akna sulgemine),
    # katkestatakse lõputu tsükkel.
    if pygame.event.wait().type == pygame.QUIT:
        break

# Lõpetab Pygame'i, vabastades kõik ressursid.
pygame.quit()
