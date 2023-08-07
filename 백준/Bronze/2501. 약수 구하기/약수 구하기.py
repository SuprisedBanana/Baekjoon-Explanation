N, K = map(int, input().split())
count = 0
num = 1
while 1:
    if N % num == 0:
        count += 1
    if count == K:
        print(num)
        break
    elif num == N:
        print(0)
        break
    num += 1