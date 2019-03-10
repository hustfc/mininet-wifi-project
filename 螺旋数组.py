class Solution:
    def __init__(self):
        self.num = 1
        self.m = 0
        self.n = 0
    def Recursion(self, matrix, row, col, mode):
        if matrix[row][col] != 0:
            return
        matrix[row][col] = self.num
        self.num += 1
        if mode == 1:
            if col + 1 < self.n and matrix[row][col + 1] == 0:
                self.Recursion(matrix, row, col + 1, 1)
            elif row + 1 < self.m:
                self.Recursion(matrix, row + 1, col, 2)
        elif mode == 2:
            if row + 1 < self.m and matrix[row + 1][col] == 0:
                self.Recursion(matrix, row + 1, col, 2)
            elif col - 1 >= 0:
                self.Recursion(matrix, row, col - 1, 3)
        elif mode == 3:
            if col - 1 >= 0 and matrix[row][col - 1] == 0:
                self.Recursion(matrix, row, col - 1, 3)
            elif row - 1 >= 0:
                self.Recursion(matrix, row - 1, col, 4)
        else:
            if row - 1 >= 0 and matrix[row - 1][col] == 0:
                self.Recursion(matrix, row - 1, col, 4)
            elif col + 1 < self.n:
                self.Recursion(matrix, row, col + 1, 1)
    def RotationMatrix(self, m, n):
        if m < 0 or n < 0:
            raise Exception('input error')
        matrix = [([0] * n) for i in range(m)]
        self.m = m
        self.n = n
        self.Recursion(matrix, 0, 0, 1)
        return matrix