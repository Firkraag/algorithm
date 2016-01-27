def counting_sort(A, B, k):
    C = []
    for i in range(0, k + 1):
        C.append(0)
    for j in range(0, len(A)):
        C[A[j]] = C[A[j]] + 1
    for i in range(1, k + 1):
        C[i] = C[i] + C[i - 1]
    for j in range(len(A) - 1, -1, -1):
        B[C[A[j]] - 1] = A[j]
        C[A[j]] = C[A[j]] - 1
