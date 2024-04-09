import pygame
import random 
pygame.init()

#värvid
red = [255, 0, 0]
lGreen = [153, 255, 153]

#ekraani seaded
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("Harjutamine")
screen.fill(lGreen)

for i in range (1,10):
    x = random.randint(0, 620)
    y = random.randint(0, 460) 
    pygame.draw.rect(screen, red, [x, y, 20, 20])

    pygame.display.flip()


# Loop, mis töötab seni, kuni kasutaja sulgeb akna
while True:
    if pygame.event.wait().type == pygame.QUIT:  # Oodake, kuni kasutaja sulgeb akna
        break  # Katkesta tsükkel, kui kasutaja sulgeb akna


pygame.quit()a# Impordime Pygame'i mooduli
import pygame

# Impordime random mooduli, mis võimaldab meil genereerida juhuslikke arve
import random 

# Initsialiseerime Pygame'i
pygame.init()

# Määrame mõned värvid RGB kujul nimega red ja lGreen
red = [255, 0, 0]
lGreen = [153, 255, 153]

# Seame ekraani suuruse
screen = pygame.display.set_mode([640, 480])

# Seame ekraanile pealkirja
pygame.display.set_caption("Harjutamine")

# Täidame ekraani hele rohelise värviga
screen.fill(lGreen)

# Tsükkel, mis joonistab ekraanile 9 punast ruutu juhuslikes kohtades
for i in range(1, 10):
    # Genereerime juhuslikud x- ja y-koordinaadid
    x = random.randint(0, 620)
    y = random.randint(0, 460) 
    # Joonistame punase ruudu ekraanile antud koordinaatidega ja mõõtmetega 20x20
    pygame.draw.rect(screen, red, [x, y, 20, 20])

    # Värskendame ekraani
    pygame.display.flip()

# Loop, mis töötab seni, kuni kasutaja sulgeb akna
while True:
    # Ootame sündmust (nt kasutaja akna sulgemist)
    if pygame.event.wait().type == pygame.QUIT:  
        break  # Katkestame tsükli, kui kasutaja sulgeb akna

# Lõpetame Pygame'i kasutamise
pygame.quit()
