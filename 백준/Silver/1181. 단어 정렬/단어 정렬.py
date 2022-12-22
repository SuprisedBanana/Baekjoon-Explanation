N = int(input())
Nlist = []
Slist = []
for i in range(N):
    word = input()
    Nlist.append(word)

for i in range(N):
    if Nlist[i] not in Slist:
        Slist.append(Nlist[i])

Slist.sort()

Slist.sort(key=len)

for i in range(len(Slist)):
    print(Slist[i])