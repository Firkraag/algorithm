def extended_bottom_up_cut_rod(p, n):
    r = [0] * (n + 1)
    s = [0] * (n + 1)
    for j in range(1, n + 1):
        q = float("-Inf")
        for i in range(1, j + 1):
            if q < p[i - 1] + r[j - i]:
                q = p[i - 1] + r[j - i]
                s[j] = i
        r[j] = q
    return r, s    

def print_cut_rod_solution(p, n):
    r,s = extended_bottom_up_cut_rod(p, n)
    while n > 0:
        print s[n]
        n = n - s[n]
