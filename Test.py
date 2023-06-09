import pygame
import generatore
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

grid = generatore.generate()

while True:
    gui(grid=grid, win=win, FONT=FONT, ORIG_DIGIT_COLOR=ORIG_DIGIT_COLOR)
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
        if events.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            ins(window=win, pos=(pos[0]//50, pos[1]//50), grid=grid, BUFFER=BUFFER)
