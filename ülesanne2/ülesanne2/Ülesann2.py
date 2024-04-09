import pygame  # Importib pygame mooduli, mis võimaldab luua mänge ja graafikat.

pygame.init()  # Initsialiseerib pygame'i, et saaks kasutada selle funktsioone.

# Ekraani seaded
screen = pygame.display.set_mode([640, 480])  # Loob uue akna suurusega 640x480 pikslit.
pygame.display.set_caption("2")  # Määrab akna pealkirjaks "Ülesanne 2".

# Lisame pildi
bg = pygame.image.load("bg.jpg")  # Laadib taustapildi nimega "bg.jpg" mälusse.
screen.blit(bg, [0, 0])  # Asetab taustapildi akna vasakusse ülanurka (x=0, y=0).

mehike = pygame.image.load("seller.jpg")  # Laadib pildi "seller.jpg" mälusse.
mehike = pygame.transform.scale(mehike, [260, 308])  # Muudab laetud pildi suurust 260x308 pikslile.
screen.blit(mehike, [103, 158])  # Asetab suuruse muudetud pildi ekraanile koordinaatidel (x=103, y=158).

chat = pygame.image.load("chat.jpg")  # Laadib pildi "chat.jpg" mälusse.
chat = pygame.transform.scale(chat, [257, 210])  # Muudab laetud pildi suurust 257x210 pikslile.
screen.blit(chat, [245, 65])  # Asetab suuruse muudetud pildi ekraanile koordinaatidel (x=245, y=65).

# Lisame teksti
font = pygame.font.Font(None, 35)  # Loob fondi suurusega 35.
text = font.render("Tere, olen Marta", True, [255, 255, 255])  # Loob teksti "Tere, olen Marta" valge värviga.
screen.blit(text, [280, 140])  # Asetab teksti ekraanile koordinaatidel (x=280, y=140).

pygame.display.flip()  # Värskendab ekraani, et kuvada kõik muudatused.

# Lõputu tsükkel, mis kestab seni, kuni kasutaja sulgeb akna.
while True:
    if pygame.event.wait().type == pygame.QUIT:  # Ootab, kuni kasutaja genereerib QUIT sündmuse (akna sulgemine).
        break  # Katkestab tsükli, kui kasutaja sulgeb akna.

pygame.quit()  # Lõpetab pygame'i, vabastades kõik ressursid.
