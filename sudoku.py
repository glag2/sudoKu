import random


def num_possibile(grid, num, row=0, column=0):
    # Controllo se nella riga è presente il numero
    if num in grid[row]:
        return False
    # Controllo se nella colonna è presente il numero
    for i in range(9):
        if num == grid[i][column]:
            return False
    # Controllo se nel blocco è presente il numero

        # Queste due righe assegnano alle variabili la prima cella
        # del blocco arrotondando per difetto l'indice della riga e colonna
    block_row = (row // 3) * 3
    block_col = (column // 3) * 3
    # Controllo vero e proprio del blocco
    for i in range(3):
        for j in range(3):
            if num == grid[block_row + i][block_col + j]:
                return False
    return True


def riempimento(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                # Genero una lista casuale di numeri da 1 a 9
                for num in random.sample(range(1, 10), 9):
                    # Se possibile modifica il valore della cella della matrice assegnando il nuovo valore
                    if num_possibile(grid, num, row, col):
                        grid[row][col] = num
                        if riempimento(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True


grid = [[0 for _ in range(9)] for _ in range(9)]
riempimento(grid)
for i in range(len(grid)):
    print(grid[i])
