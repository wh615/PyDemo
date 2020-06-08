import json
from io import StringIO

import os

f=StringIO()
f.write("hello")
print(f)
print(f.write(" "))
print(f.write("world!"))
print(f.getvalue())


info=StringIO("学习Python,,,,,学习Python");
while True:
    s=info.readline();
    if s=='':
        break
    print(s.strip())


print(os.name)
print(os._Environ)
print(os._putenv)



d=dict(name='Bob',age=20,score=100,addr="广州");
temp=json.dumps(d)
print(temp);
print(json.loads(temp))