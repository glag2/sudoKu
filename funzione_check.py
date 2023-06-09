# Ogni riga contiene tutti i numeri da 1 a 9 esattamente una volta.
# Ogni colonna contiene tutti i numeri da 1 a 9 esattamente una volta.
# Ogni sottogriglia 3x3 contiene tutti i numeri da 1 a 9 esattamente una volta.



def is_valid_sudoku(grid):
    def is_valid_unit(unit):
        unit = [i for i in unit if i != "."]
        return len(unit) == len(set(unit))

    # Check rows
    for row in grid:
        if not is_valid_unit(row):
            return False

    # Check columns
    for col in zip(*grid):
        if not is_valid_unit(col):
            return False

    # Check subgrids
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = [
                grid[x][y]
                for x in range(i, i + 3)
                for y in range(j, j + 3)
            ]
            if not is_valid_unit(subgrid):
                return False

    return True
