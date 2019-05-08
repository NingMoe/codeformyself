import pymysql

db = pymysql.connect("192.168.103.31", "root", "adminadmin", "test")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS COURSE")

# 使用预处理语句创建表
sql = """CREATE TABLE COURSE (
             ID char(24)  NOT NULL,
             diamondPrice  INT,
             studyUsersCount  INT,
             translatedTitle VARCHAR(200), 
             times DATE)CHARACTER SET utf8"""
cursor.execute(sql)
# 提交到数据库执行
db.commit()

# 关闭数据库连接
db.close()