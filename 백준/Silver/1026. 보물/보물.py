N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

SortA = []
for i in range(N):
    SortA.append(A[i])

SortA.sort()
indexList = []
for i in range(N):
    num = 0
    index = 0
    for j in range(N):
        if j in indexList:
            continue
        elif B[j] >= num:
            num = B[j]
            index = j
            A[j] = SortA[i]
    indexList.append(index)
        

result = 0
for i in range(N):
    result += A[i]*B[i]

print(result)