class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def rec(ind, row, col, temp):
            # print(temp)
            if(ind == len(word)):
                return True
            
            if(row+1 < len(board) and (row+1, col) not in temp and board[row+1][col] == word[ind]):
                temp.add((row+1, col))
                if rec(ind+1, row+1, col, temp):
                    return True
                temp.remove((row+1, col))
            
            if(row-1 >= 0 and (row-1, col) not in temp and board[row-1][col] == word[ind]):
                temp.add((row-1, col))
                if rec(ind+1, row-1, col, temp):
                    return True
                temp.remove((row-1, col))

            if(col+1 < len(board[0]) and (row, col+1) not in temp and board[row][col+1] == word[ind]):
                temp.add((row, col+1))
                if rec(ind+1, row, col+1, temp):
                    return True
                temp.remove((row, col+1))
                
            if(col-1 >= 0 and (row, col-1) not in temp and board[row][col-1] == word[ind]):
                temp.add((row, col-1))
                if rec(ind+1, row, col-1, temp):
                    return True
                temp.remove((row, col-1))
                
        
        for n in range(len(board)):
            for m in range(len(board[0])):
                if(board[n][m] == word[0]):
                    if rec(1, n, m, set([(n, m)])):
                        return True
        
        return False