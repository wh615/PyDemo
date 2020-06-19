#第一步:明确目标
#在QQ音乐的歌曲界面中爬取歌曲评论

#第二步:分析过程
#通过对歌曲界面的 Network 分析，可以知道 https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg 这个URL是用来获取歌曲评论的请求。让我们去抓取喜欢的歌曲的评论吧！

import requests
# 引用requests模块
url = 'https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg'

for i in range(5):
    params = {
'g_tk':'5381',
'loginUin':'0',
'hostUin':'0',
'format':'json',
'inCharset':'utf8',
'outCharset':'GB2312',
'notice':'0',
'platform':'yqq.json',
'needNewCode':'0',
'cid':'205360772',
'reqtype':'2',
'biztype':'1',
'topid':'102065756',
'cmd':'6',
'needmusiccrit':'0',
'pagenum':str(i),
'pagesize':'15',
'lasthotcommentid':'song_102065756_3202544866_44059185',
'domain':'qq.com',
'ct':'24',
'cv':'10101010'
}
res_comments = requests.get(url,params=params)
json_comments = res_comments.json()
list_comments = json_comments['comment']['commentlist']
for comment in list_comments:
    print(comment['rootcommentcontent'])
print('-----------------------------------')