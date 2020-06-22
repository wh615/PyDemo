import scrapy
#导入scrapy

class BookDoubanItem(scrapy.Item):
#定义一个类BookDoubanItem，它继承自scrapy.Item
    title = scrapy.Field()
    #定义书名的数据属性
    publish = scrapy.Field()
    #定义出版信息的数据属性
    score = scrapy.Field()
    #定义评分的数据属性

book = BookDoubanItem()
# 实例化一个DoubanItem对象
book['title'] = '追风筝的人 '
book['publish'] = '[美] 卡勒德·胡赛尼 / 李继宏 / 上海人民出版社 / 2006-5 / 29.00元'
book['score'] = '8.9'
print(book)
print(type(book))