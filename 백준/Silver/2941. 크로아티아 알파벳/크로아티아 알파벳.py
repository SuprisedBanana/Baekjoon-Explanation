List = ["dz=", "d-", "c=", "c-", "lj", "nj", "s=", "z="]
word = input()

for i in range(len(List)):
    word = word.replace(List[i], "1")

print(len(word))