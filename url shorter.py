import pyshorteners
url=input('enter the url:')
s=pyshorteners.Shortener().tinyurl.short(url)
print('short url is :' , s)