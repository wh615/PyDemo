# 题目要求
    # 有一个徒弟厨师，跟着师父学做煎饼果子，师父教给徒弟做传统的煎饼果子，与台湾手抓饼；徒弟在学习后又出国深造了几年，不仅仅能做手抓饼，还可以做中西方口味融合的煎饼果子。
# 题目讲解
    # 创建一个师父类master，这个类中具有两个方法；一个方法叫cake，cake方法可以制作手抓饼，一个方法叫cook，cook方法可以制作传统的煎饼果子。
    # 而徒弟类继承了师父的cake方法，可以制作手抓饼，也继承了师父的cook方法，但是徒弟进行改进，可以制作中西方口味融合的煎饼果子。

class Master(object):
    status = "厨师"
    def cake(self):
        print('可以制作手抓饼')
    def cook(self):
        print('制作传统的煎饼果子')
class Apprentice(Master):
    def cook(self):
        print('制作中西方口味融合的煎饼果子')
print("师父")
shifu = Master()
print(shifu.status)
shifu.cake()
shifu.cook()
print("徒弟")
tudi = Apprentice()
print(tudi.status)
tudi.cake()
tudi.cook()
