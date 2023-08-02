word = input().upper()
word_dic = {}

for i in range(len(word)):
    if word[i] not in word_dic:
        word_dic[word[i]] = 1
    else:
        word_dic[word[i]] += 1

max_value = max(word_dic.values())
count = 0
for i in word_dic:
    if max_value == word_dic[i]:
        count += 1

if count > 1:
    print("?")
else:
    print([k for k, v in word_dic.items() if v == max_value][0])