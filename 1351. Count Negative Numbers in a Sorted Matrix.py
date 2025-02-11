grid = grid = [[3,2],[1,0]]

def countNegatives(grid):
    m_end = len(grid)
    m = 0   
    output = 0

    while m < m_end:
        n = len(grid[0]) - 1
        currEval = grid[m][n]
        while currEval < 0 and n >= 0 :
            output += 1
            n -= 1
            currEval = grid[m][n]
        m += 1
    return output

print(countNegatives(grid))