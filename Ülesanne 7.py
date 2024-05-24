import pygame  # Impordib pygame mooduli, mida kasutatakse mängude loomiseks ja graafika haldamiseks
import random  # Impordib random mooduli, mida kasutatakse juhuslike arvude genereerimiseks

# Pygame'i algus
pygame.init()  # Initsialiseerib kõik pygame mooduli sees olevad moodulid

# Mänguakna suurus
ekraan = pygame.display.set_mode((600, 480))  # Loo ekraan määratud laiuse (600) ja kõrgusega (480) pikslit
pygame.display.set_caption("Ringid")  # Seab akna pealkirjaks "Ringid"
ekraan.fill([0, 103, 205])  # Täidab ekraani sinise värviga (RGB väärtused)

# Ringide loend
circles = []  # Loob tühja loendi, kuhu lisatakse ringid

# Maksimaalne ringide arv
max_circles = 10  # Seab ringide maksimaalse arvu kümneks

# Mängu tsükkel
running = True  # Määrab mängu tsükli muutujaks True, et tsükkel käivituks
while running:  # Peamine mängu tsükkel, mis kestab kuni running muutub False-ks
    pygame.time.delay(100)  # Lisab 100 millisekundilise viivituse iga tsükli iteratsiooni vahel

    for event in pygame.event.get():  # Kontrollib kõiki pygame sündmusi
        if event.type == pygame.QUIT:  # Kui sündmus on akna sulgemine
            running = False  # Määrab running False-ks, lõpetades tsükli
        if event.type == pygame.MOUSEBUTTONDOWN:  # Kui sündmus on hiireklõps
            if len(circles) >= max_circles:  # Kui ringide arv ületab maksimaalse arvu
                circles.pop(0)  # Eemaldab esimese ringi loendist
            # Lisab uue ringi loendisse: asukoht (event.pos), raadius (10) ja juhuslik värv
            circles.append([event.pos, 10, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))])

    ekraan.fill((153, 204, 255))  # Täidab ekraani helesinise värviga, et joonistada järgmine kaader
    for circle in circles:  # Läbib kõik ringid loendis
        circle[1] += 1  # Suurendab ringi raadiust ühe võrra
        # Joonistab ringi ekraanile: värv (circle[2]), asukoht (circle[0]), raadius (circle[1]), joone paksus (1)
        pygame.draw.circle(ekraan, circle[2], circle[0], circle[1], 1)

    pygame.display.update()  # Uuendab ekraani, et kuvada joonistatud pildid

pygame.quit()  # Lõpetab pygame ja sulgeb akna
