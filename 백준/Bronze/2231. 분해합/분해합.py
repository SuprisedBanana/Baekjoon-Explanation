N = int(input())
def asd(N):
    for i in range(1, N+1):
        num = i
        for j in range(len(str(i))):
            num += int(str(i)[j])
        if num == N:
            return print(i)
    return print(0)

asd(N)