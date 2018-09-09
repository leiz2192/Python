import urllib.request as request

def getWedHtml(url):
    return request.urlopen(url).read().decode('utf-8')

html = getWedHtml("http://www.baidu.com")

print(html)
