class Solution(object):
    def setZeroes(self, matrix):
        r,c=len(matrix),len(matrix[0])
        first_r=any(matrix[0][i] == 0 for i in range(c))
        first_c=any(matrix[i][0] == 0 for i in range(r))
        for i in range(1,r):
            for j in range(1,c):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        for i in range(1,r):
            for j in range(1,c):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        if first_r:
            for j in range(c):
                matrix[0][j]=0
        if first_c:
            for i in range(r):
                matrix[i][0]=0
        return matrix
