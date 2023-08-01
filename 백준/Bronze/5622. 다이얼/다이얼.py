alpha = input()
time = 0
for i in  alpha:
    if i < "S":
        time += (ord(i)-56)//3
    elif i < "Z":
        time += (ord(i)-57)//3
    else:
        time += 10

print(time)