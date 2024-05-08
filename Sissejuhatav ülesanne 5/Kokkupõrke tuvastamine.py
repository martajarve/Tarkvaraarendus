import pygame, random  # Impordib Pygame'i mooduli ja random mooduli
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
clock = pygame.time.Clock()  # Loob ajakella objekti

# Mängija alguspositsioon ja kiirus
posX, posY = 0, 0
speedX, speedY = 3, 4

# Mängija loomine
player = pygame.Rect(posX, posY, 120, 140)  # Loob mängija ristküliku
playerImage = pygame.image.load("Muumi.png")  # Laeb mängija pildi
playerImage = pygame.transform.scale(playerImage, [player.width, player.height])  # Skaalab mängija pildi vastavalt ristküliku suurusele

# Vaenlase loomine
enemies = []  # Loob tühja listi vaenlaste jaoks
for i in range(5):  # Loob 5 suvalist vaenlast
    enemies.append(pygame.Rect(random.randint(0, screenX - 100), random.randint(0, screenY - 100), 60, 73))  # Lisab uue vaenlase listi
enemyImage = pygame.image.load('urr.png')  # Laeb vaenlase pildi
enemyImage = pygame.transform.scale(enemyImage, [enemies[0].width, enemies[0].height])  # Skaalab vaenlase pildi vastavalt esimese vaenlase suurusele

enemyCounter = 0  # Vaenlaste loendur
totalEnemies = 20  # Kokku vaenlasi mängus
score = 0  # Mängija skoor

gameover = False  # Mängu lõppu kontrolliv muutuja
while not gameover:  # Tsükkel kestab seni, kuni gameover muutuja väärtuseks saab True
    clock.tick(60)  # Seab mängu värskendussageduseks 60 kaadrit sekundis

    # Mängu sulgemine ristist
    event = pygame.event.poll()  # Küsib ja salvestab kasutaja sündmused
    if event.type == pygame.QUIT:  # Kui kasutaja vajutab sulgemisnuppu,
        break  # katkestatakse tsükkel

    # Mängija liikumine
    player = pygame.Rect(posX, posY, 120, 140)  # Määra mängija uus asukoht
    screen.blit(playerImage, player)  # Kuvab mängija pildi ekraanil

    posX += speedX  # Värskenda mängija X-koordinaati vastavalt kiirusele
    posY += speedY  # Värskenda mängija Y-koordinaati vastavalt kiirusele

    if posX > screenX - playerImage.get_rect().width or posX < 0:  # Kui mängija jõuab ekraani servale X-teljel,
        speedX = -speedX  # pööratakse tema liikumissuund vastupidiseks

    if posY > screenY - playerImage.get_rect().height or posY < 0:  # Kui mängija jõuab ekraani servale Y-teljel,
        speedY = -speedY  # pööratakse tema liikumissuund vastupidiseks

    # Vaenlaste loomine
    enemyCounter += 1  # Suurendab vaenlaste loendurit ühe võrra
    if enemyCounter >= totalEnemies:  # Kui vaenlaste loendur ületab maksimaalse vaenlaste arvu,
        enemyCounter = 0  # nullitakse loendur
        enemies.append(pygame.Rect(random.randint(0, screenX - 100), random.randint(0, screenY - 100), 60, 73))  # Lisatakse uus vaenlane listi

    for enemy in enemies[:]:  # Iga vaenlase jaoks
        if player.colliderect(enemy):  # Kui mängija puutub kokku vaenlasega,
            enemies.remove(enemy)  # eemaldatakse vaenlane listist
            score += 1  # suurendatakse mängija skoori

    for enemy in enemies:  # Iga vaenlase jaoks
        screen.blit(enemyImage, enemy)  # Kuvatakse vaenlane ekraanil

    pygame.display.flip()  # Värskendab ekraani
    screen.fill(lBlue)  # Täidab ekraani helesinise värviga

    print(score)  # Prindib mängija skoori
    if score == 20:  # Kui mängija skoor jõuab 20-ni,
        gameover = True  # mäng lõpetatakse

pygame.quit()  # Lõpetab Pygame'i
