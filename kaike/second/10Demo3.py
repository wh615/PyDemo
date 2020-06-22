# 这段代码在本地运行
from selenium import webdriver #从selenium库中调用webdriver模块
import time

driver = webdriver.Chrome() # 设置引擎为Chrome，从本地打开一个Chrome浏览器
driver.get('https://xiaoke.kaikeba.com/example/X-Man/') # 访问页面
time.sleep(6) # 等待3秒
label = driver.find_element_by_tag_name('label') # 解析网页并提取第一个<label>标签
print(label.text) # 打印label的文本
print(driver.find_element_by_id('teacher').text)
driver.close() # 关闭浏览器


# 以下方法都可以从网页中提取出'你好，X战警'这段文字
#find_element_by_tag_name：通过元素的名称选择
# 如<h1>你好，X战警</h1>
# 可以使用find_element_by_tag_name('h1')

#find_element_by_class_name：通过元素的class属性选择
# 如<h1 class="title">你好，X战警</h1>
# 可以使用find_element_by_class_name('title')

#find_element_by_id：通过元素的id选择
# 如<h1 id="title">你好，X战警</h1>
# 可以使用find_element_by_id('title')

#find_element_by_name：通过元素的name属性选择
# 如<h1 name="hello">你好，X战警</h1>
# 可以使用find_element_by_name('hello')

#以下两个方法可以提取出超链接
#find_element_by_link_text：通过链接文本获取超链接
# 如<a href="spidermen.html">你好，X战警</a>
# 可以使用find_element_by_link_text('你好，X战警')

#find_element_by_partial_link_text：通过链接的部分文本获取超链接
# 如<a href="https://xiaoke.kaikeba.com/example/X-Man/">你好，X战警</a>
# 可以使用find_element_by_partial_link_text('你好')