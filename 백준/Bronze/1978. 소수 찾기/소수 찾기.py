def prime(factor, count):
    if factor == 1:
        return count
    for i in range(2, factor):
        if factor % i == 0:
            return count
    count += 1
    return count

n = int(input())
nList = list(map(int, input().split()))

count = 0
for i in range(n):
    count = prime(nList[i], count)

print(count)