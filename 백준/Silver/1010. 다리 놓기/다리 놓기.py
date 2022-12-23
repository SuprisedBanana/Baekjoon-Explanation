T = int(input())
List = []
for i in range(T):
    N, M = map(int, input().split())
    List.append([N, M])

for i in range(T):
    resultN = 1
    resultM = 1
    N = List[i][0]
    M = List[i][1]
    for j in range(M-N+1, M+1, 1):
        resultM *= j
    for j in range(1, N+1, 1):
        resultN *= j

    print(int(resultM/resultN))