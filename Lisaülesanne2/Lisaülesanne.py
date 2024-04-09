import pygame  # Importib pygame mooduli, mis võimaldab luua mänge ja graafikat.
import math
pygame.init()  # Initsialiseerib pygame'i, et saaks kasutada selle funktsioone.

# Ekraani seaded
screen = pygame.display.set_mode([640, 480])  # Loob uue akna suurusega 640x480 pikslit.
pygame.display.set_caption("2")  # Määrab akna pealkirjaks "Ülesanne 2".

# Lisame pildi
bg = pygame.image.load("bg.png")  # Laadib taustapildi nimega "bg.jpg" mälusse.
screen.blit(bg, [0, 0])  # Asetab taustapildi akna vasakusse ülanurka (x=0, y=0).

mehike = pygame.image.load("seller.png")  # Laadib pildi "seller.jpg" mälusse.
mehike = pygame.transform.scale(mehike, [260, 308])  # Muudab laetud pildi suurust 260x308 pikslile.
screen.blit(mehike, [103, 158])  # Asetab suuruse muudetud pildi ekraanile koordinaatidel (x=103, y=158).

chat = pygame.image.load("chat.png")  # Laadib pildi "chat.jpg" mälusse.
chat = pygame.transform.scale(chat, [257, 210])  # Muudab laetud pildi suurust 257x210 pikslile.
screen.blit(chat, [245, 65])  # Asetab suuruse muudetud pildi ekraanile koordinaatidel (x=245, y=65).

mook = pygame.image.load("Mõõk.png")  # Laadib pildi "chat.jpg" mälusse.
mook = pygame.transform.scale(mook, [60, 100])  # Muudab laetud pildi suurust 257x210 pikslile.
screen.blit(mook, [550, 150])  # Asetab suuruse muudetud pildi ekraanile koordinaatidel (x=245, y=65).

logo = pygame.image.load("VIKK logo.png")  # Laadib pildi "chat.jpg" mälusse.
logo = pygame.transform.scale(logo, [285, 80])  # Muudab laetud pildi suurust 257x210 pikslile.
screen.blit(logo, [10, 00])  # Asetab suuruse muudetud pildi ekraanile koordinaatidel (x=245, y=65).

kook = pygame.image.load("cake.png")  # Laadib pildi "chat.jpg" mälusse.
kook = pygame.transform.scale(kook, [130, 140])  # Muudab laetud pildi suurust 257x210 pikslile.
screen.blit(kook, [460, 150])  # Asetab suuruse muudetud pildi ekraanile koordinaatidel (x=245, y=65).


# Lisame teksti
font = pygame.font.Font(None, 30)  # Loob fondi suurusega 50.
tekst = font.render("Tere, olen Marta", True, [255, 255, 255])  # Loob teksti "Tere, olen Marta" valge värviga.
screen.blit(tekst, [280, 145])  # Asetab teksti ekraanile koordinaatidel (x=280, y=140).

font = pygame.font.Font(None, 13)  # Loob fondi suurusega 13.
# Teksti ja kaare seaded
text = "2050 KIVELUT"
radius = 30
angle = 178  # poolkaare jaoks
# Kaare keskpunkt ja algusnurk
center_x = 300
center_y = 48
start_angle = 280  # Pöörake kaart 90 kraadi paremale

# Arvuta iga tähe asukoht kaarel
for i in range(len(text)):
    offset_angle = start_angle + angle - (angle / (len(text)-1)) * i  # Muuda nurkade arvutamist
    x = center_x + radius * math.cos(math.radians(offset_angle))
    y = center_y + radius * math.sin(math.radians(offset_angle))

    # Loo tekst
    text_surface = font.render(text[i], True, (255, 255, 255))

    # Kuvage tekst ekraanil
    screen.blit(text_surface, (x, y))

pygame.display.flip()  # Värskendab ekraani, et kuvada kõik muudatused.


# Lõputu tsükkel, mis kestab seni, kuni kasutaja sulgeb akna.
while True:
    if pygame.event.wait().type == pygame.QUIT:  # Ootab, kuni kasutaja genereerib QUIT sündmuse (akna sulgemine).
        break  # Katkestab tsükli, kui kasutaja sulgeb akna.

pygame.quit()  # Lõpetab pygame'i, vabastades kõik ressursid.
