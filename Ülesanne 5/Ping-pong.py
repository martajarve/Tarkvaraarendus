import pygame  # Impordib Pygame'i teeki

pygame.init()  # Initsialiseerib kõik Pygame'i moodulid

screenX = 640  # Määrab mänguakna laiuse
screenY = 480  # Määrab mänguakna kõrguse
screen = pygame.display.set_mode((screenX, screenY))  # Loob mänguakna määratud suurusega

taust = (153, 204, 255)  # Määrab taustavärvi RGB väärtusega

pygame.display.set_caption("Ping-Pong")  # Määrab mänguakna pealkirja

pall_suurus = 20  # Määrab palli suuruse
pall_kiirusX = 5  # Määrab palli horisontaalse kiiruse
pall_kiirusY = 3  # Määrab palli vertikaalse kiiruse
pall = pygame.Rect(screenX/2 - pall_suurus/2, screenY/2 - pall_suurus/2, pall_suurus, pall_suurus)  # Loob palli, määrates selle asukoha ja suuruse

alus_laius = 120  # Määrab aluse laiuse
alus_kõrgus = 20  # Määrab aluse kõrguse
alus_kiirus = 3  # Määrab aluse kiiruse
alus = pygame.Rect(screenX/2 - alus_laius/2, screenY/1.5, alus_laius, alus_kõrgus)  # Loob aluse, määrates selle asukoha ja suuruse

pall_img = pygame.image.load("ball.png")  # Laeb palli pildi
alus_img = pygame.image.load("pad.png")  # Laeb aluse pildi
pall_img = pygame.transform.scale(pall_img, (pall_suurus, pall_suurus))  # Muudab palli pildi suurust vastavalt palli suurusele
alus_img = pygame.transform.scale(alus_img, (alus_laius, alus_kõrgus))  # Muudab aluse pildi suurust vastavalt aluse suurusele

score = 0  # Alustab skoori nullist

alus_suund = 1  # Määrab aluse liikumise suuna (1 tähendab paremale, -1 tähendab vasakule)

running = True  # Määrab, et mäng on käimas
clock = pygame.time.Clock()  # Loob kella objekti, mida kasutatakse mängu kiiruse kontrollimiseks
while running:  # Mängu põhitsükkel
    for event in pygame.event.get():  # Käib läbi kõik sündmused
        if event.type == pygame.QUIT:  # Kui sündmus on akna sulgemine
            running = False  # Lõpetab mängu

    pall.x += pall_kiirusX  # Liigutab palli horisontaalselt
    pall.y += pall_kiirusY  # Liigutab palli vertikaalselt

    if pall.left <= 0 or pall.right >= screenX:  # Kui pall puudutab ekraani vasakut või paremat serva
        pall_kiirusX = -pall_kiirusX  # Muudab palli horisontaalse suuna vastupidiseks
    if pall.top <= 0:  # Kui pall puudutab ekraani ülemist serva
        pall_kiirusY = -pall_kiirusY  # Muudab palli vertikaalse suuna vastupidiseks

    if pall.colliderect(alus) and pall_kiirusY > 0:  # Kui pall puudutab alust ja liigub allapoole
        pall_kiirusY = -pall_kiirusY  # Muudab palli vertikaalse suuna vastupidiseks
        score += 1  # Suurendab skoori

    if pall.bottom >= screenY:  # Kui pall puudutab ekraani alumist serva
        score -= 1  # Vähendab skoori
        pall.y = screenY - pall_suurus  # Seab palli asukoha ekraani alumise serva kohale
        pall_kiirusY = -pall_kiirusY  # Muudab palli vertikaalse suuna vastupidiseks

    if alus.left <= 0 or alus.right >= screenX:  # Kui alus puudutab ekraani vasakut või paremat serva
        alus_suund *= -1  # Muudab aluse liikumise suuna vastupidiseks
    alus.x += alus_kiirus * alus_suund  # Liigutab alust

    screen.fill(taust)  # Täidab ekraani taustavärviga

    screen.blit(pall_img, (pall.x, pall.y))  # Kuvab palli pildi palli asukohas
    screen.blit(alus_img, (alus.x, alus.y))  # Kuvab aluse pildi aluse asukohas

    font = pygame.font.Font(None, 36)  # Loob fondi skoori kuvamiseks
    skoor = font.render("Skoor: " + str(score), True, (0, 0, 0))  # Loob tekstiobjekti skoori kuvamiseks
    screen.blit(skoor, (10, 10))  # Kuvab skoori ekraani ülemises vasakus nurgas

    pygame.display.flip()  # Värskendab ekraani
    clock.tick(60)  # Piirab mängu kiirust 60 kaadrit sekundis

pygame.quit()  # Lõpetab Pygame'i
