a = input()
t = 0
for i in  a:
    if i < "S":
        t += (ord(i)-56)//3
    elif i < "Z":
        t += (ord(i)-57)//3
    else:
        t += 10
print(t)