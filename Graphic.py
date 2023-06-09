import pygame

grid = [[0, 0, 2, 0, 4, 0, 1, 9, 8],
    [7, 0, 0, 0, 0, 0, 4, 5, 3],
    [4, 1, 5, 8, 9, 0, 0, 0, 0],
    [0, 2, 6, 7, 0, 0, 3, 4, 0],
    [0, 4, 0, 0, 0, 2, 0, 1, 7],
    [1, 0, 0, 0, 8, 0, 2, 6, 0],
    [3, 8, 0, 0, 7, 0, 9, 2, 0],
    [0, 6, 0, 0, 2, 8, 5, 3, 0],
    [2, 0, 1, 0, 0, 0, 7, 8, 0]]

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


def GUI():
    while True:
        # <editor-fold, Disegno griglia>
        for i in range(10):
            if i % 3 == 0:
                pygame.draw.line(win, (0, 0, 0), (50 + 50*i, 50), (50 + 50*i, 500), 4)
                pygame.draw.line(win, (0, 0, 0), (50, 50 + 50*i), (500, 50 + 50*i), 4)

            pygame.draw.line(win, (0, 0, 0), (50 + 50*i, 50), (50 + 50*i, 500), 2)
            pygame.draw.line(win, (0, 0, 0), (50, 50 + 50*i), (500, 50 + 50*i), 2)

        # Scrivo i valori dentro la griglia
        for i in range(len(grid[0])):
            for j in range(len(grid[0])):
                if 0 < grid[i][j] < 10:
                    value = FONT.render(str(grid[i][j]), True, ORIG_DIGIT_COLOR)
                    win.blit(value, ((j+1)*50 + 15, (i+1)*50))
        pygame.display.update()
        # </editor-fold>

GUI()
