"""

    练习：
        创建一个数据库 dict
        创建一个表 words
        将单词本中的单词插入表中
        id Word mean
"""

import pymysql
import re

db=pymysql.connect(host='localhost',
                   port=3306,
                   user='root',
                   password='123456',
                   database='dict',
                   charset='utf8')

cur=db.cursor()

# sql='create table words (id smallint primary key auto_increment , word varchar(32) not null,mean text'
# cur.execute(sql)
# db.commit()

f=open('dict.txt')

sql = "insert into words (word,mean) values(%s,%s)"

for line in f:
    # word=line.split(' ',1)
    # mean=line
    tup=re.findall(r'(\S+)\s+(.*)',line)[0]
    print(tup)

    try:
        cur.execute(sql,tup)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)



f.close()
cur.close()
db.close()


