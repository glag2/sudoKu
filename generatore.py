import logging
import random
import numpy as np
import copy
import typing as tp

ListGrid = tp.List[tp.List[int]]


def mask(grid: ListGrid, rate: float = 0.5) -> ListGrid:
    if rate > 1.:
        raise ValueError("mask rate should less or equal to 1")
    grid = copy.deepcopy(grid)
    if rate <= 0.:
        return grid

    h = len(grid)
    w = len(grid[0])
    n = h * w
    masked_n = int(n * rate)
    mask_array = [True] * masked_n + [False] * (n - masked_n)
    random.shuffle(mask_array)
    for r in range(h):
        for c in range(w):
            if mask_array[r * w + c]:
                grid[r][c] = 0
    return grid


def generate(mask_rate=0.5) -> ListGrid:
    attempt = 1
    while True:
        n = 9
        g = np.zeros((n, n), np.uint)
        rg = np.arange(1, n + 1)
        g[0, :] = np.random.choice(rg, n, replace=False)
        try:
            for r in range(1, n):
                for c in range(n):
                    col_rest = np.setdiff1d(rg, g[:r, c])
                    row_rest = np.setdiff1d(rg, g[r, :c])
                    avb1 = np.intersect1d(col_rest, row_rest)
                    sub_r, sub_c = r // 3, c // 3
                    avb2 = np.setdiff1d(np.arange(0, n + 1),
                                        g[sub_r * 3:(sub_r + 1) * 3, sub_c * 3:(sub_c + 1) * 3].ravel())
                    avb = np.intersect1d(avb1, avb2)
                    g[r, c] = np.random.choice(avb, size=1)
            break
        except ValueError:
            attempt += 1
    g_list: ListGrid = g.tolist()
    if attempt > 1:
        logging.debug(f"generate by np_union attempt {attempt}")
    return mask(g_list, mask_rate)

if __name__ == '__main__':
    grid = generate()
    for i in range(len(grid)):
        print(grid[i])
