#! /usr/bin/python2.7

# AUTHOR: WangQiang
# CREATE DATE:   20140528
# LAST UPDATE DATE: 20140603
# EMAIL:  cntqrxj@gmail.com

from numpy import *

def common_matrix_multiply(A, B):
    if (A.shape[1] != B.shape[0]):
        print "The width of matrix A not equal the height of matrix B.\nHence no matrix multiplication allowed"
        return
    shape = (A.shape[0], B.shape[1])
    C = zeros(shape, dtype = int64)
    A_width = A.shape[1]
    B_width = B.shape[1]
    A_height = A.shape[0]
    B_height = B.shape[0]
    half_A_width = A_width / 2
    half_A_height = A_height / 2
    half_B_width = B_width / 2
    half_B_height = B_height / 2
    if A_height == 1 or B_width == 1:
        C =    dot(A, B) 
#    else if 
    else:
        C[0:half_A_height, 0:half_B_width] = common_matrix_multiply(A[0:half_A_height, 0:half_A_width], B[0:half_B_height, 0:half_B_width]) + common_matrix_multiply(A[0:half_A_height, half_A_width:A_width], B[half_B_height:B_height, 0:half_B_width])
        C[0:half_A_height, half_B_width:B_width] = common_matrix_multiply(A[0:half_A_height, 0:half_A_width], B[0:half_B_height, half_B_width:B_width]) + common_matrix_multiply(A[0:half_A_height, half_A_width:A_width], B[half_B_height:B_height, half_B_width:B_width])
        C[half_A_height:A_height, 0:half_B_width] = common_matrix_multiply(A[half_A_height:A_height, 0:half_A_width], B[0:half_B_height, 0:half_B_width]) + common_matrix_multiply(A[half_A_height:A_height, half_A_width:A_width], B[half_B_height:B_height, 0:half_B_width])
        C[half_A_height:A_height, half_B_width:B_width] = common_matrix_multiply(A[half_A_height:A_height, 0:half_A_width], B[0:half_B_height,half_B_width:B_width]) + common_matrix_multiply(A[half_A_height:A_height, half_A_width:A_width], B[half_B_height:B_height, half_B_width:B_width])
    return C
    
A = array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
B = array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
#A = array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#B = array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#A = array([[1, 2, 3], [4, 5, 6]])
#B = array([[1, 2], [4, 5]])
print common_matrix_multiply(A, B)
#print dot(A, B)
