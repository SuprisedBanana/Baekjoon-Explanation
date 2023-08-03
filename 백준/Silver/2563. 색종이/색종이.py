N = int(input())
List = []
for _ in range(N):
    List.append(list(map(int, input().split())))

paper = [[0] * 100 for _ in range(100)]

for i in range(N):
    for j in range(List[i][0], List[i][0]+10):
        for k in range(List[i][1], List[i][1]+10):
            paper[j][k] = 1

count = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            count+=1

print(count)