import os

aa = os.walk("c:/")

for path,dir,files in aa:
    #files 이거는 그냥 모든 파일
    #확장자가 .py면 쭉쭉 그 path 와 filename 를 뽑아재낌
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.py':
            print("path:{0} filename:{1}".format(path,filename))

