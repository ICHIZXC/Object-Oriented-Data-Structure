def water_flow(grid, r, c, R, C, current_height):
    if r < 0 or r >= R or c < 0 or c >= C:
        return
    if grid[r][c] > current_height or grid[r][c] == 0:
        return
    height_here = grid[r][c]
    grid[r][c] = 0
    water_flow(grid, r-1, c, R, C, height_here)
    water_flow(grid, r+1, c, R, C, height_here)
    water_flow(grid, r, c-1, R, C, height_here)
    water_flow(grid, r, c+1, R, C, height_here)


print(" *** Water Flow ***")
inp = input("Input rows,cols/data1,data2,.../start_row,start_col : ")

rc_no, num, water = inp.strip().split('/')
R, C = map(int, rc_no.split(','))
if R < 1 or R > 9 or C < 1 or C > 9:
    print("Error: Rows and columns must be between 1 and 9")
else:
    rows = num.split(',')
    start_row, start_column = map(int, water.split(','))
    if start_row < 0 or start_row >= R or start_column < 0 or start_column >= C:
        print("Error: Start coordinates are out of grid bounds")
    else:
        grid = [[int(ch) for ch in row] for row in rows]
        start_height = grid[start_row][start_column]
        water_flow(grid, start_row, start_column, R, C, start_height)
        for row in grid:
            print(''.join(str(x) for x in row))