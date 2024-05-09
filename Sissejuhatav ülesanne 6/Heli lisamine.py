import pygame, random  # Impordib Pygame'i ja random teegid

pygame.init()  # Initsialiseerib Pygame'i
pygame.mixer.init()  # Initsialiseerib Pygame'i segisti

sounds = ['lehm.wav', 'Lammas.wav', 'kana.wav', 'siga.wav', 'eesel.wav', 'hani.wav', 'part.wav' ]  # Loob listi helifailide nimedega

pygame.mixer.music.load(random.choice(sounds))  # Valib juhusliku helifaili listist ja laeb selle mängimiseks

pygame.mixer.music.play()  # Alustab helifaili esitamist

pygame.mixer.music.set_volume(0.5)  # Määrab heli tugevuseks 0.5 (pool maksimumist)
