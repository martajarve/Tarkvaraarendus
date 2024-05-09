import pygame  # Impordib Pygame'i mooduli
pygame.init()  # Initsialiseerib Pygame'i

# Värvid
red = [255, 0, 0]  # Punane värv
lBlue = [153, 204, 255]  # Helesinine värv

# Ekraani seaded
screenX = 640  # Ekraani laius
screenY = 480  # Ekraani kõrgus
screen = pygame.display.set_mode([screenX, screenY])  # Loob mänguakna antud mõõtmetega
pygame.display.set_caption("Klaviatuuriga juhtimine")  # Paneb mänguaknale pealkirja
screen.fill(lBlue)  # Täidab mänguakna helesinise värviga
clock = pygame.time.Clock()  # Loob mängu jaoks kella

# Alguskoordinaadid ja kiirus
posX, posY = screenX / 2, screenY / 2  # Määrab alguskoordinaadid ekraani keskele
speedX, speedY = 0, 0  # Määrab algne kiirus nulliks
directionX, directionY = 0, 0  # Määrab algne liikumissuuna nulliks

gameover = False  # Mängu lõppu kontrolliv muutuja
while not gameover:  # Mängutsükkel
    clock.tick(60)  # Piirab tsüklit 60 kaadriga sekundis

    for event in pygame.event.get():  # Tsükkel kõigi sündmuste jaoks
        if event.type == pygame.QUIT:  # Kui kasutaja sulgeb mänguakna
            gameover = True  # Märgib mängu lõppu

        # Klahvivajutus
        elif event.type == pygame.KEYDOWN:  # Kui kasutaja vajutab klahvi alla
            if event.key == pygame.K_RIGHT:  # Kui vajutatakse paremat noolt
                directionX = "move_right"  # Määrab liikumissuuna paremale
            elif event.key == pygame.K_LEFT:  # Kui vajutatakse vasakut noolt
                directionX = "move_left"  # Määrab liikumissuuna vasakule
            elif event.key == pygame.K_UP:  # Kui vajutatakse ülesnoolt
                directionY = "move_up"  # Määrab liikumissuuna ülespoole
            elif event.key == pygame.K_DOWN:  # Kui vajutatakse allanoolt
                directionY = "move_down"  # Määrab liikumissuuna allapoole

        # Klahvivajutuse vabastamine
        elif event.type == pygame.KEYUP:  # Kui kasutaja vabastab klahvi
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:  # Kui vabastatakse parem või vasak nool
                directionX = 0  # Lülita X-suuna liikumissuuna nulli
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:  # Kui vabastatakse üles või allanool
                directionY = 0  # Lülita Y-suuna liikumissuuna nulli

    # Mängu piirjoonte tuvastamine
    if directionX == "move_left":  # Kui liikumissuuna vasakule
        if posX > 0:  # Kui ruut ei ole vasakul ekraanipiiril
            posX -= 3  # Liiguta X-koordinaati 3 pikslit vasakule
    elif directionX == "move_right":  # Kui liikumissuuna paremale
        if posX + 30 < screenX:  # Kui ruut ei ole paremal ekraanipiiril
            posX += 3  # Liiguta X-koordinaati 3 pikslit paremale
    if directionY == "move_up":  # Kui liikumissuuna üles
        if posY > 0:  # Kui ruut ei ole üleval ekraanipiiril
            posY -= 3  # Liiguta Y-koordinaati 3 pikslit üles
    elif directionY == "move_down":  # Kui liikumissuuna alla
        if posY + 30 < screenY:  # Kui ruut ei ole all ekraanipiiril
            posY += 3  # Liiguta Y-koordinaati 3 pikslit alla

    ruut = pygame.draw.rect(screen, red, [posX, posY, 30, 30])  # Joonistab ruudu mänguaknale
    pygame.display.flip()  # Värskendab mänguakent
    screen.fill(lBlue)  # Täidab mänguakna uuesti helesinise värviga

pygame.quit()  # Lõpetab Pygame'i
