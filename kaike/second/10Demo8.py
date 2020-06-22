# 这段代码在本地执行

from selenium import webdriver #从selenium库中调用webdriver模块
import time
driver = webdriver.Chrome() # 设置引擎为Chrome，从本地打开一个Chrome浏览器
driver.get('https://y.qq.com/n/yqq/song/001qvvgF38HVc4.html') # 访问页面
time.sleep(2)
clickformore = driver.find_element_by_class_name('js_get_more_hot')
time.sleep(0.5)
clickformore.click()
comments = driver.find_element_by_class_name('js_hot_list').find_elements_by_class_name('js_cmt_li') # 使用class_name找到评论
print(len(comments))
for i in range(len(comments)): # 循环
    comment = comments[i].find_element_by_tag_name('p') # 找到评论
    print ('评论'+str(i)+':'+comment.text + '\n-------------------------------------------------') # 打印评论
driver.close() # 关闭浏览器

#https://selenium-python-zh.readthedocs.io/en/latest/

# 本地Chrome浏览器的静默默模式设置：
# from selenium import  webdriver #从selenium库中调用webdriver模块
# from selenium.webdriver.chrome.options import Options # 从options模块中调用Options类
# chrome_options = Options() # 实例化Option对象
# chrome_options.add_argument('--headless') # 把Chrome浏览器设置为静默模式
# driver = webdriver.Chrome(options = chrome_options) # 设置引擎为Chrome，在后台默默运行