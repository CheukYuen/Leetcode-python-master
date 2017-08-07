# 2,5,7  -> 27
# end: f[27-2] + 1, f[27-5] + 1, f[27-7] + 1
# zi: f[i] = min(f[i-2]+1, f[], f[])

# f[i] = min(f[i-2]+1, f[i-5]+1, f[i-7]+1)
# not existed. like 3, less than 2. set to MAX_INT
# from 0 -> 27

def coin():
    f = [0] * 28
    MAX_INT = float('inf')
    for i in range(1, 28):
        f[i] = MAX_INT
        if i - 2 >= 0 and f[i - 2] + 1 < f[i]:
            f[i] = f[i - 2] + 1
        if i - 5 >= 0 and f[i - 5] + 1 < f[i]:
            f[i] = f[i - 5] + 1
        if i - 7 >= 0 and f[i - 7] + 1 < f[i]:
            f[i] = f[i - 7] + 1

    return f[27]


print coin()
