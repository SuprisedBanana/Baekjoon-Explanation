N = int(input())
Name_List = []
for i in range(N):
    file_name = input()
    Name_List.append(file_name)

Str = []
name_len = len(Name_List[0])
for i in range(name_len):
    cha = Name_List[0][i]
    for j in range(1, N):
        if Name_List[j][i] != cha:
            cha = "?"
    Str.append(cha)

Str = "".join(Str)
print(Str)