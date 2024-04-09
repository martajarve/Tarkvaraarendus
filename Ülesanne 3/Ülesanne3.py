# Impordime Pygame'i mooduli
import pygame

# Impordime sys mooduli, mis sisaldab funktsioone nagu sys.exit()
import sys

# Defineerime funktsiooni, mis joonistab ruudustiku ekraanile
def draw_grid(screen, square_size, rows, cols, line_color):
    # Läbime kõik read
    for i in range(rows):
        # Läbime kõik veerud
        for j in range(cols):
            # Määrame iga ruudu asukoha ja suuruse pygame.Rect objekti abil
            rect = pygame.Rect(j*square_size, i*square_size, square_size, square_size)
            # Joonistame ruudu ekraanile antud asukohas ja suuruses
            pygame.draw.rect(screen, line_color, rect, 1)

# Initsialiseerime Pygame'i
pygame.init()

# Määrake ekraani suurus
screen = pygame.display.set_mode((640, 480))

# Määrake ruudu suurus, ridade ja veergude arv ning joone värv
square_size = 20
rows = screen.get_height() // square_size
cols = screen.get_width() // square_size
line_color = (230, 0, 0)  # punane

while True:
    # Ootame sündmust (nt kasutaja akna sulgemist)
    if pygame.event.wait().type == pygame.QUIT:  
        # Katkestame tsükli, kui kasutaja sulgeb akna
        break  

    # Täidame ekraani heleda rohelise värviga
    screen.fill((153, 255, 153))  

    # Joonistame ruudustiku ekraanile
    draw_grid(screen, square_size, rows, cols, line_color)

    # Värskendame ekraani
    pygame.display.flip()

# Lõpetame Pygame'i kasutamise
pygame.quit()
