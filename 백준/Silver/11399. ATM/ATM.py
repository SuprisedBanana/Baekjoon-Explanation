N = int(input())
Nlist = list(map(int, input().split()))
Sum = 0
Nlist.sort()

for i in range(N):
    Sum+=Nlist[i]*N
    N-=1

print(Sum)