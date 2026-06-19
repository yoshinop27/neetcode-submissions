class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = matrix[self.indexSearch(matrix, target)]
        return self.binarySearchH(row, target, 0, len(row)-1)

    def indexSearch(self, matrix, target):
        for i in range(len(matrix)):
            print(matrix[i])
            if matrix[i][0] > target:
                return i - 1
        return -1

    def binarySearchH(self, row, target, start, end):
        print(f'row:{row}')
        print(f'start:${start}, end:${end}')
        if start > end:
            return False

        mid = (start + end) // 2
        print(mid)
        if target == row[mid]:
            return True
        elif target < row[mid]:
            print(f"target:{target}")
            print(f"mid val:{row[mid]}")
            return self.binarySearchH(row, target, start, mid-1)
        elif target > row[mid]:
            return self.binarySearchH(row, target, mid+1, end)
        