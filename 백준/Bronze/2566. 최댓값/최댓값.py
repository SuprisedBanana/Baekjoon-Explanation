num = 0
loc = ""
mat = [list(map(int, input().split())) for _ in range(9)]

for i in range(9):
    for j in range(9):
        if mat[i][j] >= num:
            num = mat[i][j]
            loc = str(i+1)+" "+str(j+1)

print(num)
print(loc)