#重要提示：课程的终端已经安装好了Scrapy，如果你想着自己本地的电脑使用Scrapy，需要提前安装好它。
# （安装方法：Windows：在终端输入命令：pip install scrapy；mac：在终端输入命令：pip3 install scrapy，按下enter键）

#假设你想跳转到D盘里名为Python文件夹中的scrapy_project子文件夹。你需要再命令行输入d:，就会跳转到D盘，再输入cd Python，就能跳转到Python文件夹。接着输入，就能跳转到Python文件夹里的scrapy_project子文件夹。在mac系统中的终端里，也是使用cd命令来跳转到你要的文件夹位置

#然后，再输入一行能帮我们创建Scrapy项目的命令：scrapy startproject douban，douban就是Scrapy项目的名字。按下enter键，一个Scrapy项目就创建成功了。
import scrapy


class DoubanSpider(scrapy.Spider):

    name = 'book_douban'

    allowed_domains = ['book.douban.com']

    start_urls = ['https://book.douban.com/top250?start=0']



    def parse(self, response):

        print(response.text)


info=DoubanSpider();
print(info.parse())