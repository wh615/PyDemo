
###连接sqlite3数据库
import sqlite3
conn=sqlite3.connect("test.db");
cursor=conn.cursor();
cursor.execute('drop table user1')
cursor.execute('CREATE table user1(id varchar(20) primary key, name varchar(20))')
cursor.execute('insert INTO user1(id,name) VALUES (\'1\', \'Michael\')')
print(cursor.rowcount)

cursor.execute('select * from user1 where id=?', ('1',))
values=cursor.fetchall()
print(values)
cursor.close()
conn.commit()
conn.close()