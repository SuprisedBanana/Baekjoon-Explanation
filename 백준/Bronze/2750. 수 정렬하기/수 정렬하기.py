N=int(input())

Nlist=[]
Slist=[]

for i in range(N):
    a=int(input())
    Nlist.append(a)

for i in range(len(Nlist)):
    if Nlist[i] not in Slist:
        Slist.append(Nlist[i])

def SList(array):
    n=len(array)

    if n<=1:
        return array

    mid=array[n//2]
    leftArray = []
    rightArray = []

    for i in array:
        if i<mid:
            leftArray.append(i)
        elif i>mid:
            rightArray.append(i)
    
    return SList(leftArray)+[mid]+SList(rightArray)

SLIST=SList(Slist)

for i in range(len(SLIST)):
    print(SLIST[i])
