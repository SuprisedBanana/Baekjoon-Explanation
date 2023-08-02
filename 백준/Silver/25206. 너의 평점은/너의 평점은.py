dic = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0,
       'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
score = []
for _ in range(20):
    score.append(input().split())

score_num = 0.0
count = 0.0
for i in range(20):
    if score[i][2] == "P":
        continue
    score_num += float(score[i][1])*dic[score[i][2]]
    count += float(score[i][1])

print(score_num/count)