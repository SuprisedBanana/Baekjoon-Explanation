M = int(input())
N = int(input())
factor = []
count = 1
if M <= 2 and N >=2:
    factor.append(2)
for i in range(M, N+1):
    for j in range(2, i):
        count = 0
        if i % j == 0:
            count = 1
            break
    if count == 0:
        factor.append(i)
if len(factor) == 0:
    print(-1)
else:
    print(sum(factor))
    print(factor[0])