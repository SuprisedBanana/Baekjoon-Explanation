while 1:
    n = int(input())
    if n == -1:
        break
    factor = []
    for i in range(1, n):
        if n % i  == 0:
            factor.append(i)

    if sum(factor) == n:
        print(n, end=" = ")
        for i in range(len(factor)-1):
            print(factor[i], end=" + ")
        print(factor[-1])
    else:
        print(n, "is NOT perfect.")