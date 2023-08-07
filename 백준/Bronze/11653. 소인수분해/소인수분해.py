N = int(input())
num = 2
while 1:
    if N == 1:
        break
    numbers = divmod(N, num)
    if numbers[1] == 0:
        N = numbers[0]
        print(num)
    else:
        num += 1