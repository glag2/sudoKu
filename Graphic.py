import pygame
import copy

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


def gui(grid):
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


def ins(window, pos, grid):
    grid_empty = copy.deepcopy(grid)
    i, j = pos[1], pos[0]
    try:
        if i <= 0 or j <= 0:
            raise IndexError

        if grid_empty[i - 1][j - 1] == 0:
            pygame.draw.rect(window,
                             (200, 219, 219),
                             (j * 50 + BUFFER, i * 50 + BUFFER, 50 - 2 * BUFFER, 50 - 2 * BUFFER)
                             )

            inserting = True
            while inserting:
                for events in pygame.event.get():
                    if events.type == pygame.QUIT:
                        pygame.quit()
                        inserting = False
                    key = events.dict
                    try:
                        # Se si inserisce un numero tra 0 e 10 printarlo a schermo
                        if 0 < int(key['unicode']) < 10:
                            grid[i-1][j-1] = int(key['unicode'])
                            return grid

                        else:
                            print("Value out of range")
                            raise ValueError
                    except (ValueError, KeyError):
                        pass
    except IndexError:
        pass
