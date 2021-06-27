import pymysql
import os
import re
import filePreRegular


# path = "D:/桌面/软件工程课设/Main/Input/review"
path = "C:/Users/DELL/Desktop/Main/Input/review"
database = "5g_phone"
datanames = os.listdir(path)

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    db=database,
    charset='utf8',
    autocommit=True,
)


def create_table():
    i = "phone_comments"
    statement = """create table if not exists {0}(id INT primary key NOT NULL AUTO_INCREMENT, comment nvarchar(512), phone_type nvarchar(20) , rate_date nvarchar(20), sku nvarchar(256), source nvarchar(5), user_nick nvarchar(10), pic_urls nvarchar(512));""".format(i)
    execute(statement)


def modify_attribute():
    for i in datanames:
        i = os.path.splitext(i)[0]
        statement = """ALTER TABLE {0} MODIFY COLUMN sku nvarchar(256)""".format(i)
        execute(statement)


def execute(statement):
    cur = conn.cursor()
    try:
        cur.execute(statement)
        cur.close()
    except Exception as e:
        print("执行语句失败:", e)
    else:
        print("执行语句成功")
    cur.close()


def update():
    # i = "Xiaomi_11"
    # info = filePreRegular.fileProcess(i)
    #
    # print(len(info[0]))
    # print(len(info[1]))
    # print(len(info[2]))
    # print(len(info[3]))
    # print(len(info[4]))
    # print(len(info[5]))
    #
    #
    # for j in range(0, len(info[0])):
    #     # print("{0},{1},{2},{3},{4},{5}".format(info[0][j], info[1][j], info[2][j], info[3][j], info[4][j], info[5][j]))
    #     statement = """INSERT INTO phone_comments(comment, phone_type, rate_date, sku, source, user_nick, pic_urls) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}')""".format(info[0][j], i, info[1][j], info[2][j], info[3][j], info[4][j], info[5][j])
    #     execute(statement)

    for i in datanames:
        i = os.path.splitext(i)[0]
        print(i)
        info = filePreRegular.fileProcess(i)
        for j in range(0, len(info[0])):
            statement = """INSERT INTO phone_comments(comment, phone_type, rate_date, sku, source, user_nick, pic_urls) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}')""".format(
                info[0][j], i, info[1][j], info[2][j], info[3][j], info[4][j], info[5][j])
            execute(statement)

# modify_attribute()
create_table()
update()