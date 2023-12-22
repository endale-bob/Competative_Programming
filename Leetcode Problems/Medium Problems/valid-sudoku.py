class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        three1 = defaultdict(int)
        three2 = defaultdict(int)
        three3 = defaultdict(int)
        for i in range(9):
            if(i%3 == 0):
                three1 = defaultdict(int)
                three2 = defaultdict(int)
                three3 = defaultdict(int)
            row = defaultdict(int)
            col = defaultdict(int)
            for j in range(9):
                col[board[j][i]] += 1
                if(col[board[j][i]] > 1 and board[j][i] != "."):
                    return False
                if(board[i][j] == "."):
                    continue
                row[board[i][j]] += 1
                if(row[board[i][j]] > 1):
                    return False
                if(j < 3): 
                    three1[board[i][j]] += 1
                    if(three1[board[i][j]] > 1):
                        return False
                elif(j < 6): 
                    three2[board[i][j]] += 1
                    if(three2[board[i][j]] > 1):
                        return False
                else: 
                    three3[board[i][j]] += 1
                    if(three3[board[i][j]] > 1):
                        return False
        
        return True

