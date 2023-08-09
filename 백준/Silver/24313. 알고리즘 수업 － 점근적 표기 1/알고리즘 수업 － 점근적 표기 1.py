a = list(map(int, input().split()))
c = int(input())
n = int(input())

print(1) if a[0]-c<=0 and (a[0]-c)*n+a[1] <= 0 else print(0)