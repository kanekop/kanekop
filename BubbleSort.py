def bs(a):
    lena = len(a)
    for i in range(lena):
        for j in range(lena-i-1):
            if a[j]>a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

A = list(map(int, input().split()))
B = bs(A)
print(*B)
print(*A)

# 9 1 2 3 4 5 6 7 2 11111 2 3 4 5 33 2 
