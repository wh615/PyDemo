# 题⽬要求
#  根据已给的⽹址分析⽹站特征，将最新发布的岗位第⼀⻚的标题例如（28297-（⾼级）
# 海外战略分析经理）爬取到本地。
# 使⽤技术点引导
#  requests库
#  json()
#  for循环
# 地址为：https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=158
# 5450579819&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId
# =&attrId=&keyword=&pageIndex=1&pageSize=10&language=zh-cn&area=cn
import json
import requests
res=requests.get("https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1585450579819&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex=1&pageSize=10&language=zh-cn&area=cn")
content=res.json()
print(type(content))
gangwei=content['Data']['Posts']
print(len(gangwei))
for msg in gangwei:
    print(msg['RecruitPostName'])