# Impordime Pygame'i mooduli
import pygame

# Impordime sys mooduli, mis sisaldab funktsioone nagu sys.exit()
import sys

# Defineerime funktsiooni, mis joonistab ruudustiku ekraanile
def ruudustik(ekraan, ruudu_suurus, read, veerud, joone_värv):
    # Läbime kõik read
    for rida in range(read):
        # Läbime kõik veerud
        for veerg in range(veerud):
            # Määrame iga ruudu asukoha ja suuruse pygame.Rect objekti abil
            ruut = pygame.Rect(veerg*ruudu_suurus, rida*ruudu_suurus, ruudu_suurus, ruudu_suurus)
            # Joonistame ruudu ekraanile antud asukohas ja suuruses
            pygame.draw.rect(ekraan, joone_värv, ruut, 1)

# Initsialiseerime Pygame'i
pygame.init()

# Määrake ekraani suurus
ekraan = pygame.display.set_mode((640, 480))

# Määrab ruudu suuruse, ridade ja veergude arvu ning joone värvi
ruudu_suurus = 20
read = ekraan.get_height() // ruudu_suurus
veerud = ekraan.get_width() // ruudu_suurus
joone_värv = (230, 0, 0)  # punane

while True:
    # Ootame sündmust (nt kasutaja akna sulgemist)
    if pygame.event.wait().type == pygame.QUIT:  
        # Katkestame tsükli, kui kasutaja sulgeb akna
        break  

    # Täidame ekraani heleda rohelise värviga
    ekraan.fill((153, 255, 153))  

    # Joonistame ruudustiku ekraanile
    ruudustik(ekraan, ruudu_suurus, read, veerud, joone_värv)

    # Värskendame ekraani
    pygame.display.flip()

# Lõpetame Pygame'i kasutamise
pygame.quit()
