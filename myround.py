def my_round(flt, digit):
    tmp = flt
    d = 10**-digit # d for divider
    q, v = divmod(tmp, d)
    print(q, v)
    if digit >= 0:
        digit2 = digit -1 
    else:
        digit2 = digit +1
    if v//10**(-digit2) >= 5:
        ret = (q + 1) * 10**(-digit)
    else:
        ret = (q + 0) * 10**(-digit)
    
    return ret

N, digit = map(int, input().split())
print(my_round(N, digit))
print(round(N, digit))
