import pygame, os
pygame.init()

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
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Surface")
screen.fill(lBlue)

# Rect kasutamine
player = pygame.Rect(0, 0, 120, 140)  # Loob mängija ristküliku
pygame.draw.rect(screen, red, player)  # Joonistab mängija ristküliku
playerImage = pygame.image.load("Muumi.png")  # Laeb mängija pildi
playerImage = pygame.transform.scale(playerImage, [player.width, player.height])  # Skaalab mängija pildi vastavalt ristküliku suurusele
screen.blit(playerImage, player.center)  # Paigutab mängija pildi ristküliku keskele

gameover = False
while not gameover:
    # Mängu sulgemine ristist
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break  # Katkestab tsükli, kui sulgemissündmus tekib

    pygame.display.flip()  # Värskendab ekraani
pygame.quit()  # Lõpetab Pygame'i
