import requests
import re
import lxml
from bs4 import BeautifulSoup
import os

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
def download_url(doi_org):
    libgen_header = "http://libgen.io/scimag/ads.php?doi="
    libgen_tailor = "&downloadname="
    doi = re.findall(r'\Shttps://doi.org/([a-zA-Z0-9/\.\-?]+)', doi_org, re.S)
    if doi!=None:
        dl_url = libgen_header+doi[0]+libgen_tailor
    else:
        dl_url = ""
    return dl_url

def doi_url(doi_org):

    doi = re.findall(r'\S(https://doi.org/[a-zA-Z0-9/\.\-?]+)', doi_org, re.S)

    return doi[0]

def article_search(a, key_dict):
    try:
        r = requests.get(url=url, headers=headers, params=key_dict)
    except:
        a.status_append("搜索超时！")

    else:
        soup = BeautifulSoup(r.text, 'lxml')
        list=[]
        table = soup.find(name='table')
        for item in table.find_all(name='td'):
            doi = doi_url(str(item))
            down_url = download_url(str(item))

            # print(doi_url)
            # print(download_url(doi_url))
            a.web_append('<a href="'+down_url+'">'+str(item.find(class_='lead'))+"</a>")
            # a.web_append('<a href="http://www.baidu.com">' + str(item.find(class_='lead')) + '</a>')
            a.web_append(str(item.find(class_='extra')))
            a.web_append(str(item.find(class_='expand')))
            a.web_append('<a href="'+doi+'">'+doi+"</a>")
            a.web_append("\n")

        a.status_append("搜索完成！请点击标题链接进入下载")



