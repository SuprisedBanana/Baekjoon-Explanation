X = int(input())
number = 1
i = 1
while X > number:
  i += 1
  number += i
T = X - number
T=abs(T)
if i % 2 != 0: 
  List = [1,i]
  for _ in range(T):
    List[0] += 1
    List[1] -= 1
else:
  List = [i,1]
  for _ in range(T):
    List[0] -= 1
    List[1] += 1

print(str(List[0])+'/'+str(List[1]))