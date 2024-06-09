import pygame  # Impordi pygame moodul
import sys  # Impordi sys moodul
import constants as consts  # Impordi konstandid

from pygame.locals import *  # Impordi kõik pygame konstandid

class StartMenu(object):
    
    def __init__(self):

        self.screen = pygame.display.set_mode(consts.SCREENSIZE, 0, 32)  # Loo akna objekt
        self.screen.fill(consts.PINK)  # Täida aken roosa värviga
        
        # Fondi initsialiseerimine
        font = pygame.font.Font("PressStart2P-Regular.ttf", 36)

        # Loo pealkiri
        pacman_title = pygame.image.load("pyman_title4.png")  # Lae pealkirja pilt
        pacman_title_rect = pacman_title.get_rect()  # Saada pealkirja pildi ristkülik
        pacman_title_rect.centerx = consts.SCREENSIZE[0] / 2  # Seadista pealkirja pildi keskpunkt x-teljel
        pacman_title_rect.centery = 50  # Seadista pealkirja pildi keskpunkt y-teljel

        # Loo Start nupp
        start_button = pygame.Surface((192, 48))  # Loo uus pind Start nupu jaoks
        start_rect = start_button.get_rect()  # Saada Start nupu ristkülik
        start_rect.centerx = consts.SCREENSIZE[0] / 2  # Seadista Start nupu keskpunkt x-teljel
        start_rect.centery = 320  # Seadista Start nupu keskpunkt y-teljel

        # Loo Quit nupp
        quit_button = pygame.Surface((96, 48))  # Loo uus pind Quit nupu jaoks
        quit_rect = quit_button.get_rect()  # Saada Quit nupu ristkülik
        quit_rect.centerx = consts.SCREENSIZE[0] / 2  # Seadista Quit nupu keskpunkt x-teljel
        quit_rect.centery = 408  # Seadista Quit nupu keskpunkt y-teljel
        
        # Loo Start tekst
        start_text = font.render("START", True, consts.GREEN)  # Renderda Start tekst
        start_text_rect = start_text.get_rect()  # Saada Start teksti ristkülik
        start_text_rect.centerx = start_rect.centerx  # Seadista Start teksti keskpunkt x-teljel
        start_text_rect.centery = start_rect.centery  # Seadista Start teksti keskpunkt y-teljel
        
        # Loo Quit tekst
        quit_text = font.render("QUIT", True, consts.RED)  # Renderda Quit tekst
        quit_text_rect = quit_text.get_rect()  # Saada Quit teksti ristkülik
        quit_text_rect.centerx = quit_rect.centerx  # Seadista Quit teksti keskpunkt x-teljel
        quit_text_rect.centery = quit_rect.centery  # Seadista Quit teksti keskpunkt y-teljel
        
        # Joonista pealkiri, Start tekst ja Quit tekst ekraanile
        self.screen.blit(pacman_title, pacman_title_rect)
        self.screen.blit(start_text, start_text_rect)
        self.screen.blit(quit_text, quit_text_rect)

        # Uuenda ekraani
        pygame.display.update()

        # Loo menüümuusika objekt ja mängi seda
        menu_music = pygame.mixer.Sound("menu.wav")
        menu_music.play()

        # Menüü tsükkel
        while True:
            for event in pygame.event.get():  # Käi läbi kõik sündmused
                if event.type == QUIT:  # Kui sündmus on QUIT
                    pygame.quit()  # Lõpeta pygame
                    sys.exit()  # Lõpeta skript
                if event.type == MOUSEBUTTONDOWN:  # Kui sündmus on hiireklõps
                    x, y = event.pos  # Saada hiire asukoht
                    if quit_rect.collidepoint(x, y):  # Kui hiire asukoht on Quit nupu peal
                        pygame.quit()  # Lõpeta pygame
                        sys.exit()  # Lõpeta skript
                    elif start_rect.collidepoint(x, y):  # Kui hiire asukoht on Start nupu peal
                        menu_music.stop()  # Peata menüümuusika
                        return  # Lõpeta menüü

class RetryMenu(object):
    
    def __init__(self):        

        # Loo aken
        window = pygame.display.set_mode(consts.SCREENSIZE, 0, 32)
        window.fill(consts.PINK)  # Täida aken roosa värviga
        
        # Loo fondi objekt
        font = pygame.font.Font("PressStart2P-Regular.ttf", 36)
        # Loo pealkiri
        pacman_title = pygame.image.load("game_over1.jpg")  # Lae pealkirja pilt
        pacman_title_rect = pacman_title.get_rect()  # Saada pealkirja pildi ristkülik
        pacman_title_rect.centerx = consts.SCREENSIZE[0] / 2  # Seadista pealkirja pildi keskpunkt x-teljel
        pacman_title_rect.centery = 150  # Seadista pealkirja pildi keskpunkt y-teljel
        # Loo Retry nupp
        retry_button = pygame.Surface((192, 48))  # Loo uus pind Retry nupu jaoks
        retry_rect = retry_button.get_rect()  # Saada Retry nupu ristkülik
        retry_rect.centerx = 112  # Seadista Retry nupu keskpunkt x-teljel
        retry_rect.centery = 352  # Seadista Retry nupu keskpunkt y-teljel
        
        # Loo Quit nupp
        quit_button = pygame.Surface((192, 48))  # Loo uus pind Quit nupu jaoks
        quit_rect = quit_button.get_rect()  # Saada Quit nupu ristkülik
        quit_rect.centerx = 336  # Seadista Quit nupu keskpunkt x-teljel
        quit_rect.centery = 352  # Seadista Quit nupu keskpunkt y-teljel
        
        # Loo Retry tekst
        retry_text = font.render("RETRY", True, consts.GREEN)  # Renderda Retry tekst
        retry_text_rect = retry_text.get_rect()  # Saada Retry teksti ristkülik
        retry_text_rect.centerx = retry_rect.centerx  # Seadista Retry teksti keskpunkt x-teljel
        retry_text_rect.centery = retry_rect.centery  # Seadista Retry teksti keskpunkt y-teljel
        
        # Loo Quit tekst
        quit_text = font.render("QUIT", True, consts.RED)  # Renderda Quit tekst
        quit_text_rect = quit_text.get_rect()  # Saada Quit teksti ristkülik
        quit_text_rect.centerx = quit_rect.centerx  # Seadista Quit teksti keskpunkt x-teljel
        quit_text_rect.centery = quit_rect.centery  # Seadista Quit teksti keskpunkt y-teljel

        # Joonista Retry tekst, Quit tekst ja pealkiri ekraanile
        window.blit(retry_text, retry_text_rect)
        window.blit(quit_text, quit_text_rect)
        window.blit(pacman_title, pacman_title_rect)

        # Uuenda ekraani
        pygame.display.update()

        # Menüü tsükkel
        while True:
            for event in pygame.event.get():  # Käi läbi kõik sündmused
                if event.type == QUIT:  # Kui sündmus on QUIT
                    pygame.quit()  # Lõpeta pygame
                    sys.exit()  # Lõpeta skript
                if event.type == MOUSEBUTTONDOWN:  # Kui sündmus on hiireklõps
                    x, y = event.pos  # Saada hiire asukoht
                    if quit_rect.collidepoint(x, y):  # Kui hiire asukoht on Quit nupu peal
                        pygame.quit()  # Lõpeta pygame
                        sys.exit()  # Lõpeta skript
                    elif retry_rect.collidepoint(x, y):  # Kui hiire asukoht on Retry nupu peal
                        return  # Lõpeta menüü
