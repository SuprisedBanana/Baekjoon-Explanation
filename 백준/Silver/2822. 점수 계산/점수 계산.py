Score = []
Sorted = []

for i in range(8):
    a = int(input())
    Score.append(a)
    Sorted.append(a)

Sorted.sort()

for i in range(3):
    for j in range(8):
        if Score[j] == Sorted[i]:
            Score[j] = 0

print(sum(Score))

for i in range(8):
    if Score[i] != 0:
        print(i+1,end = " ")