#!/usr/bin/python
# -*- coding:utf-8 -*-


class Solution:
    """
    @param matrix: the given matrix
    @return: True if and only if the matrix is Toeplitz
    """
    def isToeplitzMatrix(self, matrix):
        # Write your code here
        row = len(matrix)
        if row == 0:
            return False
        col = len(matrix[0])
        if col == 0:
            return False

        for i in range(row - 1):
            for j in range(col - 1):
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
        return True


def main():
    print(Solution().isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))
    print(Solution().isToeplitzMatrix([[1,2],[2,2]]))


if __name__ == '__main__':
    main()
