class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        row = -1
        line = -1
        num = 0
        row_num = len(board)
        line_num = len(board[0])
        for i in range(row_num):
            for j in range(line_num):
                if board[i][j] == 'R':
                    row, line = i, j
        for i in range(row,row_num,1):
            if board[i][line] == 'p':
                num+=1
                break
            elif board[i][line] == 'B':
                break
        for i in range(row,-1,-1):
            if board[i][line] == 'p':
                num+=1
                break
            elif board[i][line] == 'B':
                break
        for j in range(line,line_num,1):
            if board[row][j] == 'p':
                num+=1
                break
            elif board[row][j] == 'B':
                break
        for j in range(line,-1,-1):
            if board[row][j] == 'p':
                num+=1
                break
            elif board[row][j] == 'B':
                break
        return num