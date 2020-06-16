transformers = ['擎天柱','大黄蜂','救护车','巨无霸福特','红蜘蛛']

del transformers[2]
transformers.pop();
print(transformers)

print(type(transformers))
print(transformers[::2])

transformers1 = {'擎天柱':190,'大黄蜂':100,'救护车':100,'巨无霸福特':100,'红蜘蛛':100}
print(type(transformers1))

print(transformers1)
print(transformers1['红蜘蛛'],transformers1.get('红蜘蛛'));
transformers1["zhagnsan"]=100
print(transformers1)
transformers1['擎天柱']=100
print(transformers1)
del  transformers1['zhagnsan']
print(transformers1)

print(type(1>2))

print('开课吧'.encode("UTF-8"))
print('开课吧'.encode("GBk"))


print(b'\xe5\xbc\x80\xe8\xaf\xbe\xe5\x90\xa7'.decode("UTF-8"))
print(b'\xbf\xaa\xbf\xce\xb0\xc9'.decode('GBk'))