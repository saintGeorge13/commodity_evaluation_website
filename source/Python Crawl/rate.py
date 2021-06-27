import pymysql

conn = pymysql.connect(
    host='siriusxiang.xyz',
    user='5g_admin',
    password='[8;mS(:Z?}m0uM%R',
    db="5g",
    charset='utf8',
    autocommit=True,
)

cursor = conn.cursor()
cursor.execute("select comment_id, prop, sentiment from evaluation_new where comment_id > 31223")
now_type = ""
dist = {}
dist_cal = {}
dist_cnt = {}
for comment in cursor.fetchall():
    comment_id = comment[0]
    prop = comment[1]
    sentiment = comment[2]
    cursor.execute("select phone_type from comment where id = {0}".format(comment_id))
    print(comment_id, prop, sentiment)
    phone_type = ""
    for phone_Type in cursor.fetchall():
        phone_type = phone_Type[0]
    if(now_type != phone_type):

        dist_cal = {}
        dist_cnt = sorted(dist_cnt.items(), key=lambda kv: (kv[1], kv[0]))
        dist_cnt.reverse()
        print(dist_cnt)
        if dist_cnt != [] and len(dist_cnt) >= 0:
            overview_id = 1
            cursor = conn.cursor()
            cursor.execute("select id from overview where name = '" + now_type + "' ")
            for name in cursor.fetchall():
                overview_id = name[0]
            for i in range(min(10, len(dist_cnt))):
                key = dist_cnt[i][0]
                dist_cal[key] = dist[key] / dist_cnt[i][1] * 5
                # 换成数据库
                statement = """INSERT INTO tag(priority, prop, sentiment, overview_id) VALUES ('{0}', '{1}', '{2}', '{3}')""".format(
                    i + 1, key, float('%.2f' % dist_cal[key]), int(overview_id))
                cursor.execute(statement)
                print(now_type, key, dist_cal[key])
        now_type = phone_type
        dist_cnt = {}
        dist = {}
    if prop != "手机" and prop != "效果" and prop != "能力" and prop != "种类" and prop != "种类":
        if prop not in dist.keys():
            dist[prop] = 0
            dist_cnt[prop] = 0
        dist[prop] += int(sentiment)
        dist_cnt[prop] += 1

dist_cnt = sorted(dist_cnt.items(), key=lambda kv: (kv[1], kv[0]))
dist_cnt.reverse()
print(dist_cnt)
overview_id = 1
cursor = conn.cursor()
cursor.execute("select id from overview where name = '" + now_type + "' ")
for name in cursor.fetchall():
    overview_id = name[0]
for i in range(min(10, len(dist_cnt))):
    key = dist_cnt[i][0]
    dist_cal[key] = dist[key] / dist_cnt[i][1] * 5
    # 换成数据库
    statement = """INSERT INTO tag(priority, prop, sentiment, overview_id) VALUES ('{0}', '{1}', '{2}', '{3}')""".format(
        i + 1, key, float('%.2f' % dist_cal[key]), int(overview_id))
    cursor.execute(statement)
    print(now_type, key, dist_cal[key])

