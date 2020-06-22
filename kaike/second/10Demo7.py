# 本地Chrome浏览器设置方法

from selenium import  webdriver # 从selenium库中调用webdriver模块

import time # 调用time模块



driver = webdriver.Chrome() # 设置引擎为Chrome，真实地打开一个Chrome浏览器

driver.get('https://xiaoke.kaikeba.com/example/X-Man/') # 访问页面

time.sleep(2) # 暂停两秒，等待浏览器缓冲



teacher = driver.find_element_by_id('teacher') # 找到【请输入你喜欢的老师】下面的输入框位置

teacher.send_keys('开课吧') # 输入文字

assistant = driver.find_element_by_name('assist') # 找到【请输入你喜欢的助教】下面的输入框位置

assistant.send_keys('全都喜欢') # 输入文字

time.sleep(2)

button = driver.find_element_by_tag_name('button') # 找到【提交】按钮

time.sleep(1)

button.click()

time.sleep(5)

driver.close()