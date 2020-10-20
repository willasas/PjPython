import sqlite3

# 1.创建与数据库的连接
conn = sqlite3.connect("test.db")
# 在内存中创建数据库
# conn = sqlite3.connect(':memory:')

# 2.创建一个游标 cursor
cur = conn.cursor()

# 3.建表的sql语句
sql_text_1 = '''CREATE TABLE scores
  ( 姓名 TEXT,
    班级 TEXT,
    性别 TEXT,
    语文 NUMBER,
    数学 NUMBER,
    英语 NUMBER);'''

# 4.执行sql语句
cur.execute(sql_text_1)

# 5.向表中插入数据
data = [('B', '一班', '女', 78, 87, 85), ('C', '一班', '男', 98, 84, 90), ]
cur.executemany('INSERT INTO scores VALUES (?,?,?,?,?,?)', data)

# OR 5.插入单条数据
#sql_text_2 = "INSERT INTO scores VALUES('A', '一班', '男', 96, 94, 98)"
# cur.execute(sql_text_2)

# 6.查询数学成绩大于90分的学生
sql_text_3 = "SELECT * FROM scores WHERE 数学 > 90"
cur.execute(sql_text_3)

# 7.获取查询结果,获取查询结果一般可用.fetchone()方法（获取第一条），或者用.fetchall()方法（获取所有条）
cur.fetchall()

# 8.提交改动的方法
conn.commit()

# 9.关闭游标和连接
cur.close()
conn.close()
