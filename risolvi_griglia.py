def riempi_griglia_sudoku(lista):
    def riga_valida(griglia, riga, num):
        for colonna in range(9):
            if griglia[riga][colonna] == num:
                return False
        return True

    def colonna_valida(griglia, colonna, num):
        for riga in range(9):
            if griglia[riga][colonna] == num:
                return False
        return True

    def blocco_valido(griglia, riga, colonna, num):
        blocco_riga_inizio = (riga // 3) * 3
        blocco_colonna_inizio = (colonna // 3) * 3
        for i in range(3):
            for j in range(3):
                if griglia[blocco_riga_inizio + i][blocco_colonna_inizio + j] == num:
                    return False
        return True

    def posizione_valida(griglia, riga, colonna, num):
        return (
            riga_valida(griglia, riga, num)
            and colonna_valida(griglia, colonna, num)
            and blocco_valido(griglia, riga, colonna, num)
        )

    def trova_prossima_cella_vuota(griglia):
        for riga in range(9):
            for colonna in range(9):
                if griglia[riga][colonna] == 0:
                    return riga, colonna
        return None, None

    def risolvi_sudoku(griglia):
        riga, colonna = trova_prossima_cella_vuota(griglia)
        if riga is None and colonna is None:
            return True

        for num in range(1, 10):
            if posizione_valida(griglia, riga, colonna, num):
                griglia[riga][colonna] = num
                if risolvi_sudoku(griglia):
                    return True
                griglia[riga][colonna] = 0

        return False

    risolvi_sudoku(lista)
    return lista
