# 这段代码在本地运行

from selenium import webdriver #从selenium库中调用webdriver模块

import time



driver = webdriver.Chrome() # 设置引擎为Chrome，从本地打开一个Chrome浏览器

driver.get('https://xiaoke.kaikeba.com/example/X-Man/') # 访问页面

time.sleep(3) # 等待3秒

label = driver.find_element_by_tag_name('label') # 解析网页并提取第一个<label>标签

print(type(label)) # 打印label的数据类型

print(label.text) # 打印label的文本

print(label) # 打印label

driver.close() # 关闭浏览器

