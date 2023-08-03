AList = []
for _ in range(5):
    alpha = list(input())
    alpha += [""]*(15-len(alpha))
    AList.append(alpha)

for i in range(15):
    for j in range(5):
        print(AList[j][i], end="")