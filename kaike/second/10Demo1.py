# pip install selenium -i https://pypi.douban.com/simple # Windows电脑安装selenium

# pip3 install selenium -i https://pypi.douban.com/simple # Mac电脑安装selenium
# selenium的脚本可以控制所有常见浏览器的操作，在使用之前，需要安装浏览器的驱动。
# 我推荐的是Chrome浏览器，打开下面的链接，就可以下载Chrome的安装包了，Windows和Mac都有。
# http://npm.taobao.org/mirrors/chromedriver/
# 提醒一下，chromewebdriver需要chrome以及python的待执行文件在同一目录下，如果这两步完成后你还是不能使用webdriver，那么你需要将它添加到环境变量中。

# 教学系统的浏览器设置方法，你不需要记住它
# from selenium.webdriver.chrome.webdriver import RemoteWebDriver # 从selenium库中调用RemoteWebDriver模块
# from selenium.webdriver.chrome.options import Options # 从options模块中调用Options类
# chrome_options = Options() # 实例化Option对象
# chrome_options.add_argument('--headless') # 对浏览器的设置
# driver = RemoteWebDriver("http://chromedriver-hub-server:4444/wd/hub", chrome_options.to_capabilities()) # 设置浏览器引擎

# 本地Chrome浏览器设置方法


# 资源文档：https://selenium-python-zh.readthedocs.io/en/latest/
# 本地Chrome浏览器的静默默模式设置：
# from selenium import  webdriver #从selenium库中调用webdriver模块
# from selenium.webdriver.chrome.options import Options # 从options模块中调用Options类
# chrome_options = Options() # 实例化Option对象
# chrome_options.add_argument('--headless') # 把Chrome浏览器设置为静默模式
# driver = webdriver.Chrome(options = chrome_options) # 设置引擎为Chrome，在后台默默运行



from selenium import webdriver

import time
driver = webdriver.Chrome()
driver.get('https://xiaoke.kaikeba.com/example/X-Man/')
time.sleep(2)
teacher = driver.find_element_by_id('teacher')
teacher.send_keys('开课吧')
assistant = driver.find_element_by_name('assist')
assistant.send_keys('全都喜欢')
time.sleep(2)
button = driver.find_element_by_tag_name('button')
time.sleep(1)
button.click()
time.sleep(5)
driver.close()
