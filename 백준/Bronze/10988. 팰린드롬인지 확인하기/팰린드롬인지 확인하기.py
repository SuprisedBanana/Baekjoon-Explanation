def pa(word):
    for i in range(len(word)//2):
        if word[i] != word[-(i+1)]:
            return print(0)
    return print(1)

word = input()

pa(word)