# 1：故事情节
# 煎饼果子老师傅在煎饼果子界摸滚打爬几十年 拥有一身的精湛的煎饼果子技术，并总结了一套"古法煎饼果子配方"，
# 可是老师傅已经年迈已久，在嗝屁之前希望把自己的配方传承下去，于是老师傅把配方传给他的的徒弟大猫

class Master(object):
    def __init__(self):
        self.kongfu="古法煎饼果子配方"
    def make_cake(self):
        print("[古法]按照<%s>制作了一份煎饼果子"%self.kongfu)

class School(object):
    def __init__(self):
        self.kongfu = "现代煎饼果子配方"

    def make_cake(self):
        print("[现代]按照<%s>制作了一份煎饼果子" % self.kongfu)
# 剧情发展第一阶段
# 大猫掌握了师傅的配方，可以制作古法煎饼果子
# 但是大猫是个爱学习的好孩子 也希望学到更多的煎饼果子的做法 于是通过百度搜索，找到了一家煎饼果子的培学校
#
# 剧情发展第二阶段
# 大猫掌握了师傅的配方和学校的配方，通过研究，大猫在两个配方的基础之上创建了一种全新的煎饼果子配方，称之为“毛氏煎饼果子”
# (子类重写父类的同名属性和方法）
#  题目要求
#  定义一个类 继承师傅的配方和学校的配方
#  让大猫在两个配方基础之上创建一种全新的煎饼果子配方 称之为毛氏煎饼果子配方
#
class MaoShi(Master,School):
    def __init__(self):
        self.kongfu='毛氏煎饼果子'
    def make_cake(self):
        print("[大猫]按照<%s>制作了一份煎饼果子" % self.kongfu)
maoshi=MaoShi();
print(maoshi.make_cake())



















