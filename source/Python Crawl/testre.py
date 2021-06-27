import re

with open('test.txt', 'r', encoding='utf-8') as f:
    s = f.read()

    appen = re.findall(r'(?<=videoList":\[\{).*?(?=\])', s)
    for i in appen:
        s = s.replace(i, "")


    append = re.findall(r'(?<=appendComment":\{).*?(?=\})', s)
    for i in append:
        s = s.replace(i, "")
    print(s)

    s = re.findall(r'(?<=pics":).*?(?=\],"buyCount")', s)
    print(s)
    print(len(s))
    f.close()