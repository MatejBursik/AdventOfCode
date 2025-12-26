import re

def parse_line(line):
    diagram = re.search(r"\[([.#]+)\]", line).group(1)
    buttons = re.findall(r"\(([^)]+)\)", line)
    
    n = len(diagram)
    target = [1 if c == '#' else 0 for c in diagram]
    
    button_masks = []
    for b in buttons:
        idxs = list(map(int, b.split(','))) if b.strip() else []
        mask = 0
        for i in idxs:
            mask ^= (1 << i)
        button_masks.append(mask)
    
    return n, target, button_masks

def solve_machine(n, target, button_masks):
    m = len(button_masks)
    mat = []

    for row in range(n):
        mask = 0
        for col in range(m):
            if (button_masks[col] >> row) & 1:
                mask |= (1 << col)
        mat.append(mask)

    rows = [[mat[i], target[i]] for i in range(n)] # Augmented matrix rows: [bitmask_of_row, rhs]
    pivot_col_for_row = [-1] * n
    r = 0

    # Gaussian elimination + brute force over free variables
    # Forward elimination
    for c in range(m):
        pivot = None
        for i in range(r, n):
            if (rows[i][0] >> c) & 1:
                pivot = i
                break

        if pivot == None:
            continue

        # Swap
        rows[r], rows[pivot] = rows[pivot], rows[r]
        pivot_col_for_row[r] = c

        # Eliminate below
        for i in range(r + 1, n):
            if (rows[i][0] >> c) & 1:
                rows[i][0] ^= rows[r][0]
                rows[i][1] ^= rows[r][1]

        r += 1

    pivot_cols = [pivot_col_for_row[i] for i in range(r)]
    free_cols = [c for c in range(m) if c not in pivot_cols]

    best = None

    # Try all combinations of free variables
    for mask in range(1 << len(free_cols)):
        x = [0] * m

        # Set free variables
        for i, col in enumerate(free_cols):
            x[col] = (mask >> i) & 1

        # Back substitution
        for i in range(r - 1, -1, -1):
            col = pivot_col_for_row[i]
            row_mask, rhs = rows[i]

            s = rhs
            for j in range(col + 1, m):
                if (row_mask >> j) & 1:
                    s ^= x[j]

            x[col] = s

        presses = sum(x)
        
        if best == None or presses < best:
            best = presses

    return best

total = 0

with open("input.txt", "r") as f:
    for line in f:
        n, target, button_masks = parse_line(line)
        total += solve_machine(n, target, button_masks)

print(total)
