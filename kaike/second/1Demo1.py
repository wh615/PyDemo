
import requests
url='https://img.kaikeba.com/web/kkb_index/img_index_logo.png'
#发出请求，并把返回的结果放在变量res中
res = requests.get(url)
#把Reponse对象的内容以二进制数据的形式返回
pic=res.content
#新建了一个文件logo.png，这里的文件没加路径，它会被保存在程序运行的当前目录下。
#图片内容需要以二进制wb读写。你在学习open()函数时接触过它。
#photo = open('logo.png','wb')
#photo.write(pic)
#获取pic的二进制内容
#photo.close()
with open('logo.png','wb') as photo:
    photo.write(pic)
#关闭文件


import requests
#引用requests库
res = requests.get('https://xiaoke.kaikeba.com/example/gexu/tengwanggexu.txt')
#用request去下载《滕王阁序》，将返回的 response 对象保存到 res 变量中
print(res.status_code)
res.encoding='utf-8'
#定义Response对象的编码为utf-8
novel=res.text
#把Response对象的内容以字符串的形式返回
print(novel)
#打印



#总结爬虫请求地址加robots.txt后缀，判断哪些地址可以爬取
#举个例子，让我们看看豆瓣的Robots协议（ https://www.douban.com/robots.txt）
##Disallow: /forum/
##Disallow: /new_subject
##Disallow: /service/iframe
##Disallow: /j/
##Disallow: /link2/
##Disallow: /recommend/
##Disallow: /doubanapp/card
##Disallow: /update/topic/
##Allow: /ads.txt
##Sitemap: https://www.douban.com/sitemap_index.xml
##Sitemap: https://www.douban.com/sitemap_updated_index.xml
# Crawl-delay: 5

#可以看到协议里有很多英文，Allow和Disallow，Allow代表可以被访问，Disallow代表禁止被访问。

