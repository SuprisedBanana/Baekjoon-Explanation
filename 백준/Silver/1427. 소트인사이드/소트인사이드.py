N = input()

Nlist = []

for i in range(len(N)):
    Nlist.append(N[i])

Nlist.sort()
Nlist.reverse()

num="".join(Nlist)

print(num)