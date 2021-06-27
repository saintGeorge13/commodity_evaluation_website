import csv

# line_w = []
# with open("特点.csv") as f:
#     lines = f.readlines()
#     for line in lines:
#         line = line.strip()
#         line = line.split(',')
#         if line[2].find("一般") != -1:
#             line[2] = re.sub("一般", "", line[2])
#             line[3] += "一般"
#             print(line[3])
#             print(line)
#         line_w.append(line)
#
# with open("特点2.csv", "a", newline="") as f:
#     writer = csv.writer(f)
#     for line in line_w:
#         writer.writerow(line)

# 剔除相似特征
flag = 1
start = 0
end = 0
comments = []
line_w = []
with open("特点2.csv") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        line = lines[i]
        line = line.strip()
        line = line.split(',')
        if int(line[0]) != flag:
            flag = int(line[0])
            end = i - 1

            for j in range(len(comments)):
                useful = 1
                for k in range(0, len(comments)):
                    if j != k and comments[k].find(comments[j]) != -1:
                        useful = 0
                if(useful):
                    line_w.append(lines[start+j].strip().split(','))
            start = i
            comments = []
        comments.append(line[4])
with open("特点3.csv", "a", newline="") as f:
    writer = csv.writer(f)
    for line in line_w:
        writer.writerow(line)




