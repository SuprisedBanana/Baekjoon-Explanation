A, B = input().split()
new_A = ""
new_B = ""

for i in range(len(A)):
    new_A += A[-1*(i+1)]

for i in range(len(B)):
    new_B += B[-1*(i+1)]

if new_A < new_B:
    print(new_B)
else:
    print(new_A)