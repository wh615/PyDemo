import requests

# 引入requests
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
# 封装headers
url = 'https://www.zhihu.com/api/v4/members/lisanshui1230/articles'
# 写入网址
params = {
    'include': 'data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,voting,review_info,is_labeled,label_info;data[*].author.badge[?(type=best_answerer)].topics',
    'offset': '0',
    'limit': '20',
    'sort_by': 'created',
}
# 封装参数
res = requests.get(url, headers=headers, params=params)
# 发送请求，并把响应内容赋值到变量res里面
print(res.status_code)
# 确认请求成功



import requests
#引入requests
headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
#封装headers
url='https://www.zhihu.com/api/v4/members/lisanshui1230/articles'
#写入网址
params={
'include':'data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,voting,review_info,is_labeled,label_info;data[*].author.badge[?(type=best_answerer)].topics',
'offset':'0',
'limit':'20',
'sort_by':'created',
}
#封装参数
res=requests.get(url,headers=headers,params=params)
#发送请求，并把响应内容赋值到变量res里面
print(res.status_code)
#确认请求成功
json_article = res.json()
print(json_article)