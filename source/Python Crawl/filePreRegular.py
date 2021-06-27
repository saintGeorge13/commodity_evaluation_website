import re
import xlwt
import os

def fileInput(file,name):
    try:
        with open('Input\\'+name+'.txt','a+',encoding='utf-8') as f:
            f.write(file)
        return 1
    except:
        print('原始数据写入出现问题')
        return 0

def fileProcess(name):
    try:
        with open('Input\\'+name+'.txt', 'r', encoding='utf-8') as f:
            #天猫的规则
            commentList = re.findall(r'(?<="rateContent":").*?(?=")', f.read())
            f.seek(0, 0)
            timeList = re.findall(r'(?<="rateDate":").*?(?=")', f.read())
            f.seek(0, 0)
            skuList = re.findall(r'(?<="auctionSku":").*?(?=")', f.read())
            f.seek(0, 0)
            sourceList = re.findall(r'(?<="cmsSource":").*?(?=")', f.read())
            f.seek(0, 0)
            userNickList = re.findall(r'(?<="displayUserNick":").*?(?=")', f.read())
            f.seek(0, 0)

            s = f.read()
            appen = re.findall(r'(?<=videoList":\[\{).*?(?=\])', s)
            for i in appen:
                s = s.replace(i, "")

            append = re.findall(r'(?<=appendComment":\{).*?(?=\})', s)
            for i in append:
                s = s.replace(i, "")

            picList = re.findall(r'(?<=pics":).*?(?=\],"buyCount")', s)

            # 淘宝的规则
            # commentList = re.findall(r'(?<="content":").*?(?=")', f.read())
            # f.seek(0,0)
            # timeList = re.findall(r'(?<="date":").*?(?=")', f.read())
            
            List = []
            List.append(commentList)
            List.append(timeList)
            List.append(skuList)
            List.append(sourceList)
            List.append(userNickList)
            List.append(picList)
        return List
    except:
        print('数据清洗出现问题')
        return None

def fileOutput(list,name):
    if list is None:return 0
    try:
        with open('Output\\comment\\'+name+'.txt', 'a+', encoding='utf-8') as f1:
            for i in range(0,len(list[0])):
                # print("{}:{}\t{}\n".format(i, list[0][i],list[1][i]))
                f1.write(list[0][i]+'\n')
        # with open('Output\\date\\' + name + '.txt', 'w', encoding='utf-8') as f2:
        #     for i in range(0, len(list[1])):
        #         # print("{}:{}\t{}\n".format(i, list[0][i],list[1][i]))
        #         f2.write(list[1][i]+'\n')
        return 1
    except:
        print('清洗后写入出现问题')
        return 0







