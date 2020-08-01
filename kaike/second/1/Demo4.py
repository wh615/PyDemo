# 2、题⽬要求：
#  请使⽤requests请求百度logo图⽚ 并且使⽤open⽅法将图⽚保存下来
# 温馨提示：
# 1.结合open函数的使⽤将图⽚写⼊到本地（任意路径下都可以）
# 2.wb为⼆进制写⼊
# 地址为：https://www.baidu.com/img/bd_logo1.png
# # 运⾏代码后结果展示为
#pip install -i https://pypi.douban.com/simple  requestsr

import  requests

res=requests.get('https://www.baidu.com/img/bd_logo1.png');
pic=res.content
photo=open('d:\\banner.jpg','wb')
photo.write(pic)
photo.close()