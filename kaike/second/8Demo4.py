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
#确认这个response对象状态正确
articles=res.json()
#用json()方法去解析response对象，并赋值到变量articles上面，此时的articles是一个
data=articles['data']
#取出键为data的值。
for i in data:
    print(i['title'])
#遍历列表，拿到的是列表里的每一个元素，这些元素都是字典，再通过键把值取出来