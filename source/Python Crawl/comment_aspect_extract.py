import sys
import json
import base64
import time
from urllib.request import urlopen
from urllib.request import Request
from urllib.error import URLError
from urllib.parse import urlencode
from urllib.parse import quote_plus
import pymysql
import os
import re
import csv

# import requests
# host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=3bsRvZUlbcFjG36FqVy8iCao&client_secret=vGPR5CI5W4H9NS8Mvdi2Oz5lSCZuyGQO'
# response = requests.get(host)
# if response:
#     print(response.json()['access_token'])
#
# url = 'https://aip.baidubce.com/rpc/2.0/nlp/v2/comment_tag?charset=UTF-8&access_token=24.601b3f4fbc22a8c5c764e274c2ee75c1.2592000.1626081288.282335-24362389&text=很好&type=13'
# response = requests.get(url)
# print(response.json())
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

API_KEY = '3bsRvZUlbcFjG36FqVy8iCao'

SECRET_KEY = 'vGPR5CI5W4H9NS8Mvdi2Oz5lSCZuyGQO'

COMMENT_TAG_URL = "https://aip.baidubce.com/rpc/2.0/nlp/v2/comment_tag"

TOKEN_URL = 'https://aip.baidubce.com/oauth/2.0/token'

def fetch_token():
    params = {'grant_type': 'client_credentials',
              'client_id': API_KEY,
              'client_secret': SECRET_KEY}
    post_data = urlencode(params)

    post_data = post_data.encode('utf-8')
    req = Request(TOKEN_URL, post_data)
    try:
        f = urlopen(req, timeout=5)
        result_str = f.read()
    except URLError as err:
        print(err)
    result_str = result_str.decode()
    result = json.loads(result_str)

    if ('access_token' in result.keys() and 'scope' in result.keys()):
        if not 'brain_all_scope' in result['scope'].split(' '):
            print ('please ensure has check the ability')
            exit()
        return result['access_token']
    else:
        print ('please overwrite the correct API_KEY and SECRET_KEY')
        exit()

def make_request(url, comment, phone_type, id):
    print("---------------------------------------------------")
    print(id, "评论文本：")
    print("    " + comment)
    print("\n评论观点：")

    response = request(url, json.dumps(
    {
        "text": comment,
        "type": 13
    }))

    data = json.loads(response)

    if "error_code" not in data or data["error_code"] == 0:
        print(data)
        with open("特点2.csv", "a", newline="") as f:
            writer = csv.writer(f)
            for item in data["items"]:
                # 积极的评论观点
                if item["prop"].find("不错") != -1:
                    item["prop"] = re.sub("不错", "", item["prop"])
                    item["adj"] += "不错"
                if item["prop"].find("一般") != -1:
                    item["prop"] = re.sub("一般", "", item["prop"])
                    item["adj"] += "一般"
                writer.writerow(list((id, phone_type, item["prop"], item["adj"], item["prop"] + item["adj"], item["sentiment"])))
                if item["sentiment"] == 2:
                    print(u"    积极的评论观点: " + item["prop"] + item["adj"])
                # 中性的评论观点
                if item["sentiment"] == 1:
                    print(u"    中性的评论观点: " + item["prop"] + item["adj"])
                # 消极的评论观点
                if item["sentiment"] == 0:
                    print(u"    消极的评论观点: " + item["prop"] + item["adj"])
    else:
        print(response)
    time.sleep(0.5)

"""
    call remote http server
"""
def request(url, data):
    req = Request(url, data.encode('utf-8'))
    has_error = False
    try:
        f = urlopen(req)
        result_str = f.read()

        result_str = result_str.decode()
        return result_str
    except  URLError as err:
        print(err)


def execute(statement):
    cur = conn.cursor()
    try:
        comment = cur.execute(statement)
        return comment
        cur.close()
    except Exception as e:
        print("执行语句失败:", e)
    else:
        print("执行语句成功")
    cur.close()
import time
if __name__ == '__main__':

    conn = pymysql.connect(
        host='siriusxiang.xyz',
        user='5g_admin',
        password='[8;mS(:Z?}m0uM%R',
        db="5g",
        charset='utf8',
        autocommit=True,
    )
    token = fetch_token()
    url = COMMENT_TAG_URL + "?charset=UTF-8&access_token=" + token
    cursor = conn.cursor()
    cursor.execute("show tables")

    statement = "select id, content, phone_type from {0}".format("comment")
    cursor.execute(statement)
    for id, comment, phone_type in cursor.fetchall():

        make_request(url, comment, phone_type, id)


    # comment1 = "手机已经收到，非常完美超出自己的想象，外观惊艳 黑色高端加外形时尚融为一体比较喜欢的类型。系统流畅优化的很好，操作界面简洁大方好上手。电池用量很满意，快充很不错。相机拍人拍物都美。总而言之一句话很喜欢的宝贝。"
    # comment2 = "外观精美大小正合适，做工精细，线条流畅，拍照完美，吃鸡最高画质无压力。连续玩了三个小时掉电百分之二十，电池强劲持久，无明显发热，操作流畅，准备再买一台给老婆生日礼物！"
    # comment3 = "大家千万不要在上当了，耗电特别快，手机激活后不支持7天无理由退货，请大家小心购买"
    #
    # token = fetch_token()
    #
    # url = COMMENT_TAG_URL + "?charset=UTF-8&access_token=" + token
    #
    # make_request(url, comment1)
    # make_request(url, comment2)
    # make_request(url, comment3)