# 本地执行这段代码

from selenium import webdriver #从selenium库中调用webdriver模块
import time
driver = webdriver.Chrome() # 设置引擎为Chrome，从本地打开一个Chrome浏览器
driver.get('https://xiaoke.kaikeba.com/example/X-Man/') # 访问页面
time.sleep(2) # 等待两秒
labels = driver.find_elements_by_tag_name('label') # 根据标签名提取所有元素
print(type(labels)) # 打印labels的数据类型
print(labels) # 打印labels

HTML = driver.page_source
print(type(HTML))
driver.close() # 关闭浏览器