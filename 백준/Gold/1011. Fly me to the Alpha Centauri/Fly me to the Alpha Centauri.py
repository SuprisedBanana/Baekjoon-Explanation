T = int(input())
List = []
for i in range(T):
    x, y = map(int, input().split())
    List.append([x, y])

for i in range(T):
    x = List[i][0]
    y = List[i][1]
    k=1
    past = 0
    remain = y-x-k
    count = 1
    while(remain > 0):
        if (remain - (k+1) >= past+k):
            past += k
            k += 1
            remain -= k
            count += 1
        elif ((remain - k) >= past):
            remain -=k
            count += 1
        else:
            if k>1:
                k-=1
            past -= k
            remain -= k
            count += 1
        
    print(count)