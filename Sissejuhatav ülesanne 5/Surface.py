import pygame  # Impordib Pygame'i mooduli

pygame.init()  # Initsialiseerib Pygame'i

# Värvid
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
lBlue = [153, 204, 255]

# Ekraani seaded
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])  # Loob ekraani
pygame.display.set_caption("Surface")  # Paneb ekraanile pealkirja "Surface"
screen.fill(lBlue)  # Täidab ekraani helesinise värviga

# Surface'i kasutamine
surf = pygame.Surface((200, 200))  # Loob uue pinnakujunduse (Surface) mõõtudega 200x200 pikslit
surf.set_colorkey((0, 0, 0))  # Määrab läbipaistvuseks musta värvi
pygame.draw.circle(surf, blue, (140, 100), 100)  # Joonistab sinise ringi Surface'ile
pygame.draw.circle(surf, green, (100, 160), 80)  # Joonistab rohelise ringi Surface'ile
pygame.draw.circle(surf, pink, (50, 100), 60)  # Joonistab roosa ringi Surface'ile
screen.blit(surf, (0, 0))  # Kuvab esimese Surface'i ekraanil (0, 0) koordinaatidele
screen.blit(surf, (100, 100))  # Kuvab teise Surface'i ekraanil (100, 100) koordinaatidele
screen.blit(surf, (400, 300))  # Kuvab kolmanda Surface'i ekraanil (400, 300) koordinaatidele

gameover = False  # Mängu lõppu kontrolliv muutuja
while not gameover:  # Tsükkel kestab seni, kuni gameover muutuja väärtuseks saab True
    # Mängu sulgemine ristist
    event = pygame.event.poll()  # Küsib ja salvestab kasutaja sündmused
    if event.type == pygame.QUIT:  # Kui kasutaja vajutab sulgemisnuppu,
        break  # katkestatakse tsükkel

    pygame.display.flip()  # Värskendab ekraani

pygame.quit()  # Lõpetab Pygame'i
