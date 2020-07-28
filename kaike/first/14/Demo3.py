# # 1:总结导入的模块的几种方式 并自定义一个计算器 延时一秒返回结果 实现计算程序执行的时间并打印计算结果，程序的运行时间（打印年月日）以及程序的运行花费的时间
#
# 模块就是.py类型的Python文件
# 导入时不需要.py后缀，直接导入文件名即可
# 利用import直接导入：
# 语法：import module_name
# 使用方式：module_name.class_name或者module.func_name
# 利用import导入模块并设置一个别名
# 语法：import module_name as XXX
# 使用方式：XXX.class_name或者XXX.funct_name
# 借助from复制模块的属性，可以实现只导入模块中的部分类或函数或变量
# 语法：from module_name import class_name， funct_name
# 使用方式：直接调用函数或实例化类即可
# 但要注意，from把变量从模块中导入后，会导致相同名称的变量被覆盖，也就是说不同模块的命名空间会在此处重叠。
# 借助from...import *导入模块全部内容
# 语法：from module_name import *
# 使用时直接调用函数或实例化类即可
# 借助importlib模块实现导入以数字开头的模块
# 语法：import importlib
# XXX = importlib.import_module("module_name")
# 使用时XXX.class_name或者XXX.func_name
#
#
# class Calu(object):
