grid = grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]

# non decreasing order in column and row
#  so if ada negatif, bawahnya fix negatif jg

def countNegatives(grid):
    m_end = len(grid)
    n_end =len(grid[0]) - 1
    m = 0   
    n = len(grid[0]) - 1
    output = 0

    # traverse column m
    while m < m_end:
        # traverse row right to left until positive num
        while grid[m][n] < 0 and n >= 0 :
            n -= 1
        # add number of negative numbers found
        output += n_end - n
        m += 1
        # start next iteration with current n because decreasing also in vertical
    return output

print(countNegatives(grid))




    # while m < m_end:
    #     n = len(grid[0]) - 1
    #     currEval = grid[m][n]
    #     while currEval < 0 and n >= 0 :
    #         output += 1
    #         n -= 1
    #         currEval = grid[m][n]
    #     m += 1
