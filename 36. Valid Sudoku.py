
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

# initial idea, call for col and row
# board always same so 0 in range 9
# make 3 set.
# sub box number is {{1,2,3}, {4,5,6}, {7,8,9}}
def isValidSudoku(board):
    # 3 checks, vertical, horizontal, sub box
    horizontalSet = set()
    verticalSet = {0:set(), 1:set(), 2:set(), 3:set(), 4:set(), 5:set(), 6:set(), 7:set(), 8:set()}
    subBoxSet = {1:set(), 2:set(), 3:set(), 4:set(), 5:set(), 6:set(), 7:set(), 8:set(), 9:set()}

    # subbox = subverticaldict + subhoridict
    subBoxVerticalDict = {0:1, 1:1, 2:1, 3:2, 4:2, 5:2, 6:3, 7:3, 8:3}
    subBoxHorizontalDict = {0:0, 1:0, 2:0, 3:3, 4:3, 5:3, 6:6, 7:6, 8:6}

    for row in range(9):
        for col in range(9):
            num = board[row][col]
            # equation to get subBox number
            subBoxNum = subBoxVerticalDict[col] + subBoxHorizontalDict[row]
            # print(col)
            # print(row)
            # print(subBoxNum)
            # print('')

            # Pass empty box
            if num == '.':
                continue
            
            # immediately checks if num is passed or not in 3 conditions
            print(num, col, row)
            if num in horizontalSet or num in verticalSet[col] or num in subBoxSet[subBoxNum]:
                print(col)
                print(row)
                print(num)
                print(subBoxNum)
                print(horizontalSet)
                print(verticalSet)
                print(subBoxSet)
                return False
            else:
                horizontalSet.add(num)
                verticalSet[col].add(num)
                subBoxSet[subBoxNum].add(num)
        print(num)
        print(subBoxNum)
        print(horizontalSet)
        print(verticalSet)
        print(subBoxSet)
        # resets vertical set for each loop for column
        horizontalSet = set()
    return True

print(isValidSudoku(board))


            

            



