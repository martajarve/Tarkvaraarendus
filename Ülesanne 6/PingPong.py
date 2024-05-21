import pygame  # Impordib Pygame'i teeki

pygame.init()  # Initsialiseerib kõik Pygame'i moodulid

screenX = 640  # Määrab mänguakna laiuse
screenY = 480  # Määrab mänguakna kõrguse
screen = pygame.display.set_mode((screenX, screenY))  # Loob mänguakna määratud suurusega

taust = (153, 204, 255)  # Määrab taustavärvi RGB väärtusega

pygame.display.set_caption("PingPong")  # Määrab mänguakna pealkirja

pall_suurus = 20  # Määrab palli suuruse
pall_kiirusX = 2  # Määrab palli horisontaalse kiiruse
pall_kiirusY = 2  # Määrab palli vertikaalse kiiruse
pall = pygame.Rect(screenX/2 - pall_suurus/2, screenY/2 - pall_suurus/2, pall_suurus, pall_suurus)  # Loob palli, määrates selle asukoha ja suuruse

alus_laius = 120  # Määrab aluse laiuse
alus_kõrgus = 20  # Määrab aluse kõrguse
alus_kiirus = 5  # Määrab aluse kiiruse
alus = pygame.Rect(screenX/2 - alus_laius/2, screenY/1.5, alus_laius, alus_kõrgus)  # Loob aluse, määrates selle asukoha ja suuruse

pall_img = pygame.image.load("ball.png")  # Laeb palli pildi
alus_img = pygame.image.load("pad.png")  # Laeb aluse pildi
pall_img = pygame.transform.scale(pall_img, (pall_suurus, pall_suurus))  # Muudab palli pildi suurust vastavalt palli suurusele
alus_img = pygame.transform.scale(alus_img, (alus_laius, alus_kõrgus))  # Muudab aluse pildi suurust vastavalt aluse suurusele
pygame.mixer.music.load('music.wav')
pygame.mixer.music.play(-1)

alus_suund = 0  # Määrab aluse liikumise suuna (1 tähendab paremale, -1 tähendab vasakule)
score = 0  # Alustab skoori nullist

running = True  # Määrab, et mäng on käimas
clock = pygame.time.Clock()  # Loob kella objekti, mida kasutatakse mängu kiiruse kontrollimiseks
while running:  # Mängu põhitsükkel
    for event in pygame.event.get():  # Käsitseb kõiki sündmusi, mis on järjekorras
        if event.type == pygame.QUIT:  # Kui sündmus on QUIT (akna sulgemine)
            running = False  # Lõpetab mängu
        elif event.type == pygame.KEYDOWN:  # Kui sündmus on KEYDOWN (klahvi vajutamine)
            if event.key == pygame.K_RIGHT:  # Kui vajutatud klahv on parem nooleklahv
                alus_suund = 1  # Liigutab alust paremale
            elif event.key == pygame.K_LEFT:  # Kui vajutatud klahv on vasak nooleklahv
                alus_suund = -1  # Liigutab alust vasakule
        elif event.type == pygame.KEYUP:  # Kui sündmus on KEYUP (klahvi vabastamine)
            if event.key == pygame.K_RIGHT and alus_suund == 1:  # Kui vabastatud klahv on parem nooleklahv ja alus liigub paremale
                alus_suund = 0  # Peatab aluse liikumise
            elif event.key == pygame.K_LEFT and alus_suund == -1:  # Kui vabastatud klahv on vasak nooleklahv ja alus liigub vasakule
                alus_suund = 0  # Peatab aluse liikumise
    # Toimub aluse liikumise juhtimine
    alus.x += alus_suund * alus_kiirus   # Aluse x-koordinaat muutub vastavalt aluse suunale ja kiirusele.

    # Siin on palli ja aluse liikumise määratlemine
    pall.x += pall_kiirusX  # Liigutab palli horisontaalselt
    pall.y += pall_kiirusY  # Liigutab palli vertikaalselt

    if pall.left <= 0 or pall.right >= screenX:  # Kui pall puudutab ekraani vasakut või paremat serva
        pall_kiirusX = -pall_kiirusX  # Muudab palli horisontaalse suuna vastupidiseks

    if pall.top <= 0:  # Kui pall puudutab ekraani ülemist serva
        pall_kiirusY = -pall_kiirusY  # Muudab palli vertikaalse suuna vastupidiseks

    if pall.colliderect(alus) and pall_kiirusY > 0:  # Kui pall puudutab alust ja liigub allapoole
        pall_kiirusY = -pall_kiirusY  # Muudab palli vertikaalse suuna vastupidiseks
        score += 1  # Suurendab skoori

# Pall puudutab alumist äärt
    if pall.bottom >= screenY:
        running = False  # Lõpetame mängu

 # Aluse piirangud
    if alus.left <= 0:  # Kui alus läheb vasakust servast välja
        alus.left = 0  # Seab alus vasakule piirile
    elif alus.right >= screenX:  # Kui alus läheb paremast servast välja
        alus.right = screenX  # Seab aluse paremale piirile

    screen.fill(taust)  # Täidab ekraani taustavärviga

    screen.blit(pall_img, (pall.x, pall.y))  # Kuvab palli pildi palli asukohas
    screen.blit(alus_img, (alus.x, alus.y))  # Kuvab aluse pildi aluse asukohas

    font = pygame.font.Font(None, 36)  # Loob fondi skoori kuvamiseks
    skoor = font.render("Skoor: " + str(score), True, (0, 0, 0))  # Loob tekstiobjekti skoori kuvamiseks
    screen.blit(skoor, (10, 10))  # Kuvab skoori ekraani ülemises vasakus nurgas

    pygame.display.flip()  # Värskendab ekraani
    clock.tick(60)  # Piirab mängu kiirust 60 kaadrit sekundis

pygame.quit()  # Lõpetab Pygame'i