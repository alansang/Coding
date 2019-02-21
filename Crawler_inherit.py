#-*-coding:cp949-*-

import requests
from bs4 import BeautifulSoup

class Crawler:
    def __init__(self,url):
        self.url = url

    def req(self):
        r = requests.get(self.url)
        return r.content

    def bsoup(self, content):
        r = BeautifulSoup(content,"html.parser")
        return r

class BoanNews(Crawler):
    def pins (self, s, t):
        ts = s.find_all(class_= t)
        for t in ts:
            print t.get_text()

class Inews(Crawler):
    def select(self, s, sel):
        ts = s.select(sel)
        for t in ts:
            print t.text


if __name__ == "__main__":

    boan = BoanNews("https://www.boannews.com/media/list.asp")
    r = boan.req()
    s = boan.bsoup(r)
    boan.pins(s, "news_txt")

    print ''

    it = Inews('http://www.inews24.com/list/it')
    a = it.req()
    b = it.bsoup(a)
    it.select(b,'body > main > article > ol > li > a')
    
