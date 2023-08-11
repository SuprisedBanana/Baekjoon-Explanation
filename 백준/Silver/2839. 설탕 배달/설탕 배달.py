N = int(input())

x = 0
y = (N-3*x)/5
while(y != int(y)):
    x+=1
    y = (N-3*x)/5

sum = int(y)+int(x)
if(y<0):
    print(-1)
else:
    print(sum)