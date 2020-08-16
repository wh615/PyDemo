# 题目要求
# 用json记录自己的日记
# 题目讲解
# 我们可以用json来记录自己的日记，一篇日记可以用一个字典来表示，有一个主题 title，
# 一个日期 date，一个内容 content。 {"title": "今天是学习爬虫的第1天！", "date":"2019.10.1", "content":"今天是学习爬虫的第1天！我学习了爬虫基础啦！"}

import json;
a = {"title": "今天是学习爬虫的第1天！", "date":"2019.10.1", "content":"今天是学习爬虫的第1天！我学习了爬虫基础啦！"}
print(type(a))
b=json.dumps(a)
c=json.loads(b)
print(c)
print(type(c))