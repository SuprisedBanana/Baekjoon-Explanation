N, M = map(int, input().split())
num = list(map(int, input().split()))
number = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            Sum = (num[i]+num[j]+num[k])
            if M-Sum >= 0:
                if number < Sum:
                    number = Sum
print(number)