import requests
import re
import os
#from kkb_tools import open_file


def get_parse_page():
    url = 'https://tieba.baidu.com/p/5059180075?pn=2'
    headers = {
        'User-Agent': 'Mozilla/5.0(Windows NT 6.1;WOW64;rv:52.0)Gecko/20100101 Firefox/52.0'}
    response = requests.get(url, headers=headers)
    html = response.content.decode('utf-8')
    results = re.findall(r'<img class="BDE_Image" src="(.*?)"', html)[:30]  # 返回一个列表
    save_to_txt(results)


def save_to_txt(results):
    j = 0
    if not os.path.exists('./' + 'assets'):
        os.makedirs('./' + 'assets')
    for result in results:
        import sys

        sys.stdout.write("\r 正在保存第\t%s/%s\t张图片 " % (str(j + 1), str(len(results))))
        sys.stdout.flush()
        try:
            pic = requests.get(result, timeout=2)
        except:
            print('当前图片无法下载')
            j += 1
            continue
        file_full_name = './' + 'assets' + '/' + '-' + str(j) + '.jpg'
        with open(file_full_name, 'wb') as f:
            f.write(pic.content)
        j += 1


if __name__ == '__main__':
    get_parse_page()
import zipfile

z = zipfile.ZipFile('assets.zip', 'w', zipfile.ZIP_DEFLATED)
startdir = "assets"
for dirpath, dirnames, filenames in os.walk(startdir):
    for filename in filenames:
        z.write(os.path.join(dirpath, filename))
z.close()
##open_file('assets.zip')