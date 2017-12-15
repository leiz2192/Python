#!/usr/bin/python
# -*- coding:utf-8 -*-

class Solution:
    """
    @param: matrix: An array of integers
    @return: An array of integers
    """
    def printZMatrix(self, matrix):
        # write your code here
        row = len(matrix)
        if row == 0: return
        col = len(matrix[0])
        if col == 0: return
        lines = row + col - 1
        i = 0
        j = 0
        result = []
        for n in range(lines):
            if n % 2 == 0:
                while i > 0 and j < col - 1:
                    result.append(matrix[i][j])
                    i -= 1
                    j += 1
                if j == col - 1:
                    result.append(matrix[i][j])
                    i += 1
                elif i == 0:
                    result.append(matrix[i][j])
                    j += 1
            else:
                while j > 0 and i < row - 1:
                    result.append(matrix[i][j])
                    i += 1
                    j -= 1
                if i == row - 1:
                    result.append(matrix[i][j])
                    j += 1
                elif j == 0:
                    result.append(matrix[i][j])
                    i += 1
        print(result)

if __name__ == '__main__':
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print("Hello :", matrix)
    solution = Solution()
    solution.printZMatrix(matrix)
