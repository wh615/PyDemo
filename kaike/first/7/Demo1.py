# 题目要求
# 现在KFC餐厅的奖金激励政策变了，变成如下：
# 1.工作时间＜1年的，发放1000元
# 2.工作年限≥1年但<3年的，发放奖金3000*年数（年数四舍五入，输入时只输入整数）如1年半为 3000*2 = 6000
# 3.工作年限≥3年的，发放奖金5000*年数（年数四舍五入，输入时只输入整数） 如3年为 5000*3 = 15000
# 题目讲解
# 定义两个函数第一个函数功能为根据工作年数返回奖金额，第二个函数功能为打印出'XX员工来了X年，获得奖金XXX元'。
# 比如输入姓名 ‘老王’，年限‘3’；就会打印出“老王来了3年，获得奖金15000元”。

name = input('请输入姓名:')
year = int(input('请输入工作年限，数字:'))
money=0
def bonus(year):
   if year<1:
     money = 1000
   elif 1<=year<3:
     money = 3000*year
   else:
     money = 5000*year
   return money

def res(name,year):
   cash = bonus(year)
   print('%s来了 %d年,获得奖金 %d元' %(name,year,cash))
res(name,year)