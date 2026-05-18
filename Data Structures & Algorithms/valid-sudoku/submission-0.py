class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [0]*9
        col = [0]*9
        box = [0]*9
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if row[int(board[i][j])-1] != 0:
                        print("row")
                        print(i,j)
                        return False
                    else:
                        row[int(board[i][j])-1] = 1
                if board[j][i] != ".":
                    if col[int(board[j][i])-1] != 0:
                        return False
                    else:
                        col[int(board[j][i])-1] = 1
                if board[int(i/3)*3+int(j/3)][(i%3)*3+j%3] != ".":
                    if box[int(board[int(i/3)*3+int(j/3)][(i%3)*3+j%3])-1] != 0:
                        return False
                    else:
                        box[int(board[int(i/3)*3+int(j/3)][(i%3)*3+j%3])-1] = 1
            row = [0]*9
            col = [0]*9
            box = [0]*9
        
        return True