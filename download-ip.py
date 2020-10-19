import urllib.request

url="http://api.aoikujira.com/ip/ini"
res= urllib.request.urlopen(url)
data = res.read()

test = data.decode("utf-8")
print(test)