cent_type = [25, 10, 5, 1]
T = int(input())
for _ in range(T):
    cent = []
    C = int(input())
    for i in cent_type:
        count = divmod(C, i)
        cent.append(str(count[0]))
        C = count[1]
    print(' '.join(cent))