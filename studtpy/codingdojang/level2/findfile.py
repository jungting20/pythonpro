import os,re


#리눅스로 찾는법
#find ./ -name *.txt | xargs grep "LIFE IS TOO SHORT"
aa = os.walk('C:\A')
for path,dir,files in aa:
    for filesname in files:
        ext = os.path.splitext(filesname)[-1]
        #if '.txt' in filename: 이방법도있음
        #얻은건 path.join 이거임 이거
        if ext == '.txt':
            bb = open(os.path.join(path,filesname),'rt')
            cc = bb.read()
            if re.search('LIFE IS TOO SHORT',cc):
                print(path,filesname)