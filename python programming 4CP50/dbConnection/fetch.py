import pymysql
db=pymysql.connect(password="",host="localhost",user="root",db="logindata");

cursor=db.cursor()
sql="insert into temp values(%d,'%s')"%(4,"asdf");
try:
    cursor.execute(sql);
    db.commit();
except:
    db.rollback()

db.close();