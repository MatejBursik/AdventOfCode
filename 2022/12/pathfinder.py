"""
input = heightmap of the surrounding area
elevation of each square of the grid is given by a single lowercase letter
"a" is the lowest elevation
highest elevation "z"
your current position (S) has elevation a
goal location (E) has elevation z
you can move exactly one square up, down, left, or right

few steps as possible
To avoid needing to get out your climbing gear, the elevation of the destination square can be at most one higher than the elevation of your current square
This also means that the elevation of the destination square can be much lower than the elevation of your current square

? least amount of steps to reach end

p2
start from any a square switch will result to the shortest path
"""
import numpy as np

# find the reachable neighbors in the grid
def reachable_neighbors(grid, y, x):
    neighbors = []
    grid_length, grid_width = grid.shape
    current_value = grid[y][x]
    if 0 < y and ord(grid[y-1][x]) <= ord(current_value) + 1:
        neighbors.append((y-1)*grid_width + x)

    if y + 1 < grid_length and ord(grid[y+1][x]) <= ord(current_value) + 1:
        neighbors.append((y+1)*grid_width + x)

    if 0 < x and ord(grid[y][x-1]) <= ord(current_value) + 1:
        neighbors.append(y*grid_width + x - 1)

    if x + 1 < grid_width and ord(grid[y][x+1]) <= ord(current_value) + 1:
        neighbors.append(y*grid_width + x + 1)
        
    return neighbors

def solve(part):
    with open("2022\\12\\input.txt","r") as f:
        lines = f.readlines()
        lines = [entry.strip() for entry in lines]

    grid = np.array([list(row) for row in lines])

    # get coordinates of S and E before replacing them
    start_coord = np.where(grid.flatten() == 'S')[0][0]
    end_coord = np.where(grid.flatten() == 'E')[0][0]

    # replace S with a and E with z
    grid[np.where(grid == 'S')] = 'a'
    grid[np.where(grid == 'E')] = 'z'

    # remove "a" for part 2
    if part==2:
        start_coord = np.where(grid.flatten() == 'a')[0]

    # calculate the number of elements in the adjacency matrix and initialize it with zeros
    adj_mtx_shape = grid.shape[0] * grid.shape[1]
    adj_matrix = np.zeros((adj_mtx_shape, adj_mtx_shape))

    # find the indixes of reachable neighbors and update the corresponding entries in the adjacency matrix to 1
    for y in np.arange(grid.shape[0]):
        for x in np.arange(grid.shape[1]):
            neighbors = reachable_neighbors(grid, y, x)
            np.put(adj_matrix[y*grid.shape[1] + x], neighbors, 1)

    # doing first step by creating target matrix
    trgt_matrix = np.array(list(adj_matrix))
    steps = 1

    # iterate through matrix multiplication until the element at (start_coord, end_coord) in the target matrix becomes non-zero for all entries
    # update the target matrix with the matrix multiplication result and increment the steps
    while (trgt_matrix[start_coord, end_coord] == 0).all():
        trgt_matrix = trgt_matrix @ adj_matrix
        steps += 1

    return steps

part = 2
print("Steps taken to reach the end for part", part, ":", solve(part))
