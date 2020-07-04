#1：利用函数完成，请输入成绩的分值，如果学习成绩》=90分的同学用A表示，
# 60-89之间的用B表示60分以一下的用C表示

def culaScore(score):
    if score>=90:
       scoreMsg='A'
       return scoreMsg
    elif 60<=score<=89:
        scoreMsg='B'
        return scoreMsg
    else:
        scoreMsg = 'C'
        return scoreMsg
msg=int(input('请输入成绩分值:'))
print(culaScore(msg))


