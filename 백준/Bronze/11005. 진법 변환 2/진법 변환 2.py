N, B = map(int, input().split())
result = ""

if N == 0:
    result = "0"
else:
    while 1:
        if N == 0:
            break
        m = divmod(N, B)
        N = m[0]
        T = m[1]
        if T < 10:
            result += str(T)
        else:
            result += str(chr(T+55))

print(result[::-1])