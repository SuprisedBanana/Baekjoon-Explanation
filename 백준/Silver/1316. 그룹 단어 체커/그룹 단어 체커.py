N = int(input())
count = 0
for _ in range(N):
    List = []
    word = list(input())
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            word[i] = ""
    for i in range(len(word)):
        if word[i] not in List:
            List.append(word[i])
        else:
            if word[i] == '':
                continue
            count += 1
            break
    
print(N-count)