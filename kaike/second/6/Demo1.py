# 题目要求
# 对课程中的代码进行修改，实现爬取五月天前三页歌曲的歌词
# 题目讲解
# 作为一个粉丝，肯定要学会唱偶像的歌，所以我们要把歌词弄到手~ 让爬虫来为我们做这件事吧！
import requests
url_song = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
for x in range(1,4):
    params_song = {'ct': '24','qqmusic_ver': '1298','new_json': '1','remoteplace': 'sizer.yqq.song_next','searchid': '64405487069162918','t': '0','aggr': '1',
'cr': '1','catZhida': '1','lossless': '0','flag_qc': '0','p': x,'n': '10','w': '五月天','g_tk': '5381','loginUin': '0','hostUin': '0','format': 'json','inCharset': 'utf8','outCharset': 'utf-8',
'notice': '0','platform': 'yqq.json','needNewCode': '0'}
# 将参数封装为字典
    headers_song = {'origin': 'https://y.qq.com','referer': 'https://y.qq.com/n/yqq/song/004Z8Ihr0JIu5s.html','user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',}
    res_music = requests.get(url_song, params=params_song, headers=headers_song)
# 调用get方法，下载这个列表
    json_music = res_music.json()
# 使用json()方法，将response对象，转为列表/字典
    list_music = json_music['data']['song']['list']
# 一层一层地取字典，获取歌单列表
    url_lyric = 'https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_yqq.fcg'
    for music in list_music:
        name = music['name']
# 以name为键，查找歌曲名，把歌曲名赋值给name
        params_lyric = {'nobase64': '1','musicid': str(music['id']),'-': 'jsonp1','g_tk': '5381','loginUin': '0','hostUin': '0',
'format': 'json','inCharset': 'utf8','outCharset': 'utf-8','notice': '0','platform': 'yqq.json','needNewCode': '0'}
        headers_lyric = {'origin': 'https://y.qq.com','referer': 'https://y.qq.com/n/yqq/song/{0}.html'.format(music['mid']),
'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
        res_lyric = requests.get(url_lyric, params=params_lyric, headers=headers_lyric)
# 调用get方法，下载这个列表
        json_lyric = res_lyric.json()
# 使用json()方法，将response对象，转为列表/字典
        lyric = json_lyric['lyric']
# 查找播放链接，把链接赋值给link
        print([name,lyric])