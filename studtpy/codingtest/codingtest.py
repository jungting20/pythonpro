from urllib import request
import io
url = "http://www.daum.net/robots.txt"
response = request.urlopen(url)
string = request.urlsplit(url)
print(response)
aa =io.TextIOWrapper(response,'utf-8')
bb = aa.read()
print(bb.startswith("User-agent"))
list = [string[string.index(":")+1::].strip(" ")
        for string in bb.split("\n")
        if string.startswith("Disallow")]

print(list)


def checkcrolling(url):
    urlspli = request.urlsplit(url)
    netloc = urlspli.netloc
    path = urlspli.path
    robots = urlspli.scheme+"://"+netloc+"/robots.txt"
    response = request.urlopen(robots)
    wrapper = io.TextIOWrapper(response,'utf-8')
    read = wrapper.read()
    if read.startswith("User-agent"):
        disallowlist = [string[string.index(":")+1::].strip(" ")
                    for string in read.split("\n")
                    if string.startswith("Disallow")]
        disallowlist.append("/")
        if "/" in disallowlist:
            return False
        return path in disallowlist
    else:
        return False

print(checkcrolling(url))

