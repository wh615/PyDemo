import requests;

res=requests.get('https://xiaoke.kaikeba.com/example/canteen/index.html');
print(res.text)
res.encoding='utf-8'
if res.status_code==200:
    with open('jd.html','a+',encoding='utf8') as jd:
        jd.write(res.text);


