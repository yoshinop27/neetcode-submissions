from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[0])):
                cur = board[i][j]
                if cur == '.':
                    continue
                ## check row
                if cur in rows[i]:
                    return False
                else:
                    rows[i].add(cur)
                ## check col
                if cur in cols[j]:
                    return False
                else:
                    cols[j].add(cur)
                if cur in boxes[(i//3, j//3)]:
                    return False
                else:
                    boxes[(i//3,j//3)].add(cur)
        return True