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

# Alguskoordinaadid ja kiiruse
posX, posY = screenX / 2, screenY / 2  # Määrab alguskoordinaadid ekraani keskele
speedX, speedY = 0, 0  # Määrab algne kiiruse nulliks

gameover = False  # Mängu lõppu kontrolliv muutuja
while not gameover:  # Mängutsükkel
    clock.tick(60)  # Piirab tsüklit 60 kaadriga sekundis

    for event in pygame.event.get():  # Tsükkel kõigi sündmuste jaoks
        if event.type == pygame.QUIT:  # Kui kasutaja sulgeb mänguakna
            gameover = True  # Märgib mängu lõppu

        elif event.type == pygame.KEYDOWN:  # Kui kasutaja vajutab klahvi alla
            if event.key == pygame.K_RIGHT:  # Kui vajutatakse paremat noolt
                speedX = 3  # Määrab X-suuna kiiruse positiivseks
            elif event.key == pygame.K_LEFT:  # Kui vajutatakse vasakut noolt
                speedX = -3  # Määrab X-suuna kiiruse negatiivseks
            elif event.key == pygame.K_UP:  # Kui vajutatakse ülesnoolt
                speedY = -3  # Määrab Y-suuna kiiruse negatiivseks
            elif event.key == pygame.K_DOWN:  # Kui vajutatakse allanoolt
                speedY = 3  # Määrab Y-suuna kiiruse positiivseks
                
        elif event.type == pygame.KEYUP:  # Kui kasutaja vabastab klahvi
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:  # Kui vabastatakse parem või vasak nool
                speedX = 0  # Lülitab X-suuna kiiruse nulli
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:  # Kui vabastatakse üles või allanool
                speedY = 0  # Lülitab Y-suuna kiiruse nulli
        
    posX += speedX  # Uuendab X-koordinaati kiiruseega
    posY += speedY  # Uuendab Y-koordinaati kiiruseega
    ruut = pygame.draw.rect(screen, red, [posX, posY, 30, 30])  # Joonistab ruudu mänguaknale
    pygame.display.flip()  # Värskendab mänguakent
    screen.fill(lBlue)  # Täidab mänguakna uuesti helesinise värviga

pygame.quit()  # Lõpetab Pygame'i
