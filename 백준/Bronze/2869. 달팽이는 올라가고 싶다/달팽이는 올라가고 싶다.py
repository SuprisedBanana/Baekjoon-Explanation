A, B, V = map(int, input().split())

num = divmod(V-A, A-B)
if num[1] > 0:
    print(num[0] + 2)
else:
    print(num[0] + 1)