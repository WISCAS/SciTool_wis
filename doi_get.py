import requests
import re
import lxml
from bs4 import BeautifulSoup

headers = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'accept-encoding': "gzip, deflate",
    'accept-language': "zh-CN,zh;q=0.9",
    'cache-control': "no-cache",
    'connection': "keep-alive",
    'host': "www.xicidaili.com",
    'if-none-match': "W/\"61f3e567b1a5028acee7804fa878a5ba\"",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"
}

url = 'https://search.crossref.org/'

key = {'q':'mram'}

def article_search(a, key_dict):
    r = requests.get(url=url, headers=headers, params=key_dict)
    #print(r.text)
    #print(type(r.text))

    soup = BeautifulSoup(r.text, 'lxml')
    list=[]
    for item in soup.find_all(name='td'):
        a.web_append(str(item.find(class_='lead')))
        a.web_append(str(item.find(class_='extra')))
        a.web_append(str(item.find(class_='expand')))
        a.web_append(str(item.find(name='a')))
        a.web_append("")

    a.status_append("Search finished!")



