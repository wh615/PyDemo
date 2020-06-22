from pandas import Series,DataFrame
import pandas as pd
# 使用字典创建
dic={
    '姓名': ['小罗伯特·唐尼', '克里斯·埃文斯', '斯嘉丽·约翰逊', '克里斯·海姆斯沃斯'],
    '饰演': ['钢铁侠', '美国队长', '黑寡妇', '雷神'],
    '武器': ['钢铁战衣', '盾牌', '寡妇蜇', '雷神之锤'],
    '语录': ['和平,我热爱和平','最好的选择就是重新开始 ','嘿，大兄弟，太阳下山了','要用知识来打败无知']}
df=DataFrame(dic)
print(df)

from pandas import Series,DataFrame
import pandas as pd
print('##################################3')
# 使用字典创建
index_list = ['No1','No2','No3']
dic={
    '姓名': Series(['娜娜','淼淼','依依'],index=index_list),
    '类型': Series(['可爱单纯','风骚火辣','性感高冷'],index=index_list),
    '爱好': Series(['逛街、电影、爱吃甜','喝酒、蹦迪、爱吃辣','看书、烘焙、爱吃酸'],index=index_list),
    '时间': Series(['2019-2-14去看电影','2019-2-16去蹦迪','2019-2-18去烘焙'],index=index_list)
    }
df=DataFrame(dic)
print(df)