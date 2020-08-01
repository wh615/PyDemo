# 题目要求
# 获取“开课吧食堂” banner 图片 （https://xiaoke.kaikeba.com/example/canteen/images/banner.png）
# 题目讲解
# 图片URL： https://xiaoke.kaikeba.com/example/canteen/images/banner.png 利用requests请求URL，实现图片下载
#pip install -i https://pypi.douban.com/simple  requests
import  requests

res=requests.get("https://xiaoke.kaikeba.com/example/canteen/images/banner.png")
pic=res.content
photo=open('d:\\banner.jpg','wb')
photo.write(pic)
photo.close()