import taobao
import filePreRegular
import configparser
import time
import random

cp = configparser.RawConfigParser()
cp.read('Infor.conf')

print('数据爬取开始')
print('-'*20)
for i in range(0,int(cp.get('taobao','pageNumber'))):
    filename = cp.get('taobao','name')+str(i)
    filePreRegular.fileInput(taobao.crawlerTaobao(i+1),cp.get('taobao','name'))
    print("已爬取第{}页评论".format(i))
    time.sleep(1)
list = filePreRegular.fileProcess(cp.get('taobao','name'))
filePreRegular.fileOutput(list,cp.get('taobao','name'))

