import pygame, random  # Impordib pygame ja random moodulid, mida kasutatakse mängu ja juhuslike arvude genereerimiseks
pygame.init()  # Initsialiseerib kõik pygame mooduli sees olevad moodulid

#värvid
red = [255, 0, 0]  # Defineerib punase värvi RGB väärtustega
green = [0, 255, 0]  # Defineerib rohelise värvi RGB väärtustega
blue = [0, 0, 255]  # Defineerib sinise värvi RGB väärtustega
pink = [255, 153, 255]  # Defineerib roosa värvi RGB väärtustega
lGreen = [153, 255, 153]  # Defineerib heledama rohelise värvi RGB väärtustega
lBlue = [153, 204, 255]  # Defineerib heledama sinise värvi RGB väärtustega

#ekraani seaded
screenX = 640  # Seab ekraani laiuseks 640 pikslit
screenY = 480  # Seab ekraani kõrguseks 480 pikslit
screen = pygame.display.set_mode([screenX, screenY])  # Loo ekraan määratud laiuse ja kõrgusega
pygame.display.set_caption("Hiir")  # Seab akna pealkirjaks "Hiir"
screen.fill(lBlue)  # Täidab ekraani helesinise värviga
clock = pygame.time.Clock()  # Loob kella, et hallata mängu kiirust
gameover = False  # Seab mängu oleku muutujaks esialgu False

while not gameover:  # Peamine mängu tsükkel, mis kestab kuni gameover muutub True-ks
    clock.tick(10)  # Seab mängu kiiruse 10 kaadrit sekundis
    #mängu sulgemine ristist
    for event in pygame.event.get():  # Kontrollib kõiki pygame sündmusi
        if event.type == pygame.QUIT:  # Kui sündmus on akna sulgemine (ristist)
            gameover = True  # Määrab gameover True-ks, lõpetades tsükli

    mousePos = pygame.mouse.get_pos()  # Saab hiire kursori asukoha ekraanil
    print("						   Mouse position:", mousePos)  # Prindib hiire kursori asukoha (x, y) koordinaadid

    click = pygame.mouse.get_pressed()  # Kontrollib hiire nuppe (vasak, parem, keskmine)
    print("Mouse click state:", click)  # Prindib hiirenupu vajutuse oleku (True või False iga nupu jaoks)

    pygame.display.flip()  # Uuendab ekraani, et kuvada joonistatud pildid
    screen.fill(lBlue)  # Täidab ekraani uuesti helesinise värviga, et joonistada järgmine kaader

pygame.quit()  # Lõpetab pygame ja sulgeb akna
