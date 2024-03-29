# 题目要求
# 金刚狼拥有快速自愈能力，他想把这个能力赋予给其他人。根据他的条件，他制定了如下规则。
# 1、如果身体体能指数energy大于等于80，就是容易改造，在此前提下：
# a) 如果身体体能指数大于等于90，1小时改造完毕。
# b) 如果身体体能指数大于等于80，1天改造完毕。
# 2、如果身体体能指数小于80，就是不易改造，在此前提下：
# a) 如果身体体能指数小于60， 改造不了。
# b) 如果身体体能指数大于等于60小于80，希望渺茫。
# 那么像魔女，她的身体体能指数有65，能否改造呢？
# 题目讲解
# 1、如果身体体能指数energy大于等于80，就是容易改造，在此前提下：
# a) 如果身体体能指数大于等于90，1小时改造完毕。
# b) 如果身体体能指数大于等于80，1天改造完毕。
# 2、如果身体体能指数小于80，就是不易改造，在此前提下：
# a) 如果身体体能指数小于60， 改造不了。
# b) 如果身体体能指数大于等于60小于80，希望渺茫。

energy = 65

if energy >= 80:
    print('容易改造')

    if energy >= 90:
        print('1小时改造完毕')

    else:
        print('1天改造完毕')

else:
    print('不易改造')

    if energy < 60:
        print('改造不了')

    else:
        print('希望渺茫')

print('结束')

print("=======扩展题=====")
# 一、题目：
# 小明在做数学题
# 如果作对4道及以上，就可以继续学习第二课
# 如果作对1-3道，就要查漏补缺
# 如果作对0道题，就要从新学习第一课
# 用if 、elif、else条件关系输出小明一道题也没有作对
# （赋值：小明一道题都没作对subject赋值为0）
print('一、题目：输出结果如下')
subject = 0
if subject >= 4:
    print('可以继续学习第二课');
elif subject >= 1:
    print('查漏补缺');
else:
    print('要从新学习第一课');
# 二、题目：
# 李峰参与英语考试
# 考试成绩规则：
# 1．如果成绩大于等于60分，就是及格
# 如果大于等于80分，属于优秀
# 如果大于等于60而小于80分，属于一般
# 2．如果成绩小于60分，就不及格
# 如果小于30分，就是学渣
# 如果小于60分而大于等于30分，还可以辅导一下
# 结果李峰考试得了28分，请用if、else 的条件关系输出
# （赋值：李峰考试得了28分historyscore赋值为28）
print('二、题目：输出结果如下')
historyscore = 28;
if historyscore >= 60:
    print('及格');
    if historyscore >= 80:
        print('优秀');
    else:
        print('一般');
else:
    print('不及格');
    if historyscore < 30:
        print('学渣');
    else:
        print('还可以辅导一下');

