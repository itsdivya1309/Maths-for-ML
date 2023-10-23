# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 14:08:08 2023

@author: Divya Tiwari

LU Decomposition of matix

LU decomposition factors a matrix as the product of a lower 
triangular matrix and an upper triangular matrix.
Computers usually solve square systems of linear equations using 
the LU decomposition, and it is also a key step when inverting a 
matrix, or computing the determinant of a matrix. The LU 
decomposition was introduced by mathematician Tadeusz Banachiewicz 
in 1938.

Doolittle’s method provides an alternative way to factor A into an 
LU decomposition without going through the hassle of Gaussian 
Elimination.
"""


# Python3 Program to decompose a matrix into lower and upper triangular matrix
MAX = 100
 
 
def luDecomposition(mat, n):
 
    lower = [[0 for x in range(n)]
             for y in range(n)]
    upper = [[0 for x in range(n)]
             for y in range(n)]
    
    # Decomposing matrix into Upper and Lower triangular matrix
    for i in range(n):
 
        # Upper Triangular
        for k in range(i, n):
 
            # Summation of L(i, j) * U(j, k)
            sum = 0
            for j in range(i):
                sum += (lower[i][j] * upper[j][k])
 
            # Evaluating U(i, k)
            upper[i][k] = mat[i][k] - sum
 
        # Lower Triangular
        for k in range(i, n):
            if (i == k):
                lower[i][i] = 1  # Diagonal as 1
            else:
 
                # Summation of L(k, j) * U(j, i)
                sum = 0
                for j in range(i):
                    sum += (lower[k][j] * upper[j][i])
 
                # Evaluating L(k, i)
                lower[k][i] = int((mat[k][i] - sum) /
                                  upper[i][i])
 
    # setw is for displaying nicely
    print("Lower Triangular\tUpper Triangular")
 
    # Displaying the result :
    for i in range(n):
 
        # Lower
        for j in range(n):
            print(lower[i][j], end="\t")
        print("", end="\t\t")
 
        # Upper
        for j in range(n):
            print(upper[i][j], end="\t")
        print("")
 
 
# Driver code
mat = [[2, 4, -2],
       [4, 9, -3],
       [-2, -3, 7]]
 
luDecomposition(mat, 3)