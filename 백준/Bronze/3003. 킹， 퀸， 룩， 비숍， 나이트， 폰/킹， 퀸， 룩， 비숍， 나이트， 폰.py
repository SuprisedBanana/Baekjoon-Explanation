chess = [1, 1, 2, 2, 2, 8]

T = input().split()

for i in range(len(chess)):
    T[i] = str(chess[i]-int(T[i]))
print(' '.join(T))