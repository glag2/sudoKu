import copy

import pygame
import generatore
import funzione_check
import risolvi_griglia
from Graphic import gui, ins

# <editor-fold, Inizializzazione schermata e definizione costanti>
pygame.init()
pygame.display.set_caption("Sudoku")
win = pygame.display.set_mode((550, 550))
BUFFER = 5
BG_COLOR = (251, 247, 245)
win.fill(BG_COLOR)
ORIG_DIGIT_COLOR = (52, 31, 151)
FONT = pygame.font.SysFont("Comic Sans MS", 35)
# </editor-fold>

try:
    while True:
        grid = generatore.generate(mask_rate=0.1)
        grid_empty = copy.deepcopy(grid)
        solution = copy.deepcopy(grid)
        risolvi_griglia.riempi_griglia_sudoku(solution)

        if not funzione_check.is_valid_sudoku(solution):
            raise ChildProcessError
        else:
            break

except ChildProcessError:
    print("err")

while True:
    gui(grid=grid, win=win, FONT=FONT, ORIG_DIGIT_COLOR=ORIG_DIGIT_COLOR)
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
        if events.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            ins(window=win, pos=(pos[0]//50, pos[1]//50), grid=grid, grid_empty=grid_empty, BUFFER=BUFFER)
    if grid == solution:
        font = pygame.font.SysFont("Comic Sans MS", 24)
        value = font.render("Vobra hai ntovi", True, (0, 0, 0))
        win.blit(value, (0, 510))
        pygame.display.update()
        input("press 'enter'")
        break

pygame.quit()
