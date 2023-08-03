N, M =map(int, input().split())
AB = []
for _ in range(2*N):
    AB.append(input().split())

for i in range(N):
    for j in range(M):
        AB[i][j] = str(int(AB[i][j]) + int(AB[i+N][j]))

for i in range(N):
    print(' '.join(AB[i]))