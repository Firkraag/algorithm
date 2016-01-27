#! /usr/bin/python2.7

# AUTHOR: WangQiang
# CREATE DATE:   20140803
# LAST UPDATE DATE: 20140803
# EMAIL:  cntqrxj@gmail.com

from numpy import *

def common_matrix_multiply(A, B):
    if (A.shape[1] != B.shape[0]):
        print "The width of matrix A not equal the height of matrix B.\nHence no matrix multiplication allowed"
        return
    shape = (A.shape[0], B.shape[1])
    #shape = A.shape
    #length = shape[0]
    #half = length / 2
    A_width = A.shape[1]
    B_width = B.shape[1]
    A_height = A.shape[0]
    B_height = B.shape[0]
    half_A_width = A_width / 2
    half_A_height = A_height / 2
    half_B_width = B_width / 2
    half_B_height = B_height / 2
    
    C = zeros(shape, dtype = int64) 
    if A_height == 1 or B_width == 1:
        C =    dot(A, B) 
    #if length == 1:
    #    C[0, 0] = A[0, 0] * B[0, 0]
    #    return C
     
    S1 = zeros((half, half), dtype = int64) 
    S2 = zeros((half, half), dtype = int64) 
    S3 = zeros((half, half), dtype = int64) 
    S4 = zeros((half, half), dtype = int64) 
    S5 = zeros((half, half), dtype = int64) 
    S6 = zeros((half, half), dtype = int64) 
    S7 = zeros((half, half), dtype = int64) 
    S8 = zeros((half, half), dtype = int64) 
    S9 = zeros((half, half), dtype = int64) 
    S10 = zeros((half, half), dtype = int64) 

    P1 = zeros((half, half), dtype = int64)
    P2 = zeros((half, half), dtype = int64)
    P3 = zeros((half, half), dtype = int64)
    P4 = zeros((half, half), dtype = int64)
    P5 = zeros((half, half), dtype = int64)
    P6 = zeros((half, half), dtype = int64)
    P7 = zeros((half, half), dtype = int64)

    S1 = B[0:half, half:length] - B[half:length, half:length]
    S2 = A[0:half, 0:half] + A[0:half, half:length]
    S3 = A[half:length, 0:half] + A[half:length, half:length]
    S4 = B[half:length, 0:half] - B[0:half, 0:half]
    S5 = A[0:half, 0:half] + A[half:length, half:length]
    S6 = B[0:half, 0:half] + B[half:length, half:length]
    S7 = A[0:half, half:length] - A[half:length, half:length]
    S8 = B[half:length, 0:half] + B[half:length, half:length]
    S9 = A[0:half, 0:half] - A[half:length, 0:half]
    S10 = B[0:half, 0:half] + B[0:half, half:length]

    P1 = square_matrix_multiply(A[0:half, 0:half], S1)
    P2 = square_matrix_multiply(S2, B[half:length, half:length])
    P3 = square_matrix_multiply(S3, B[0:half, 0:half])
    P4 = square_matrix_multiply(A[half:length, half:length], S4)
    P5 = square_matrix_multiply(S5, S6)
    P6 = square_matrix_multiply(S7, S8)
    P7 = square_matrix_multiply(S9, S10)
    
    C[0:half, 0:half] = P5 + P4 - P2 + P6
    C[0:half, half:length] = P1 + P2
    C[half:length, 0:half] = P3 + P4
    C[half:length, half:length] = P5 + P1 - P3 - P7
    
    return C    

#A = array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
#B = array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
#A = array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#B = array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
A = array([[1, 3], [7, 5]])
B = array([[6, 8], [4, 2]])
#A = array([[1, 2, 3], [4, 5, 6]])
#B = array([[1, 2], [4, 5]])
print square_matrix_multiply(A, B)
#print dot(A, B)

