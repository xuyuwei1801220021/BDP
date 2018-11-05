import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
import traceback

def getHTMLText(url):
    try:
        r=webdriver.Chrome()
        r.get(url)
        r.switch_to.frame('g_iframe') 
        return r.page_source
    except:
        return ""

def getSong(href, stitle):
    songURL="https://music.163.com"+href
    html = getHTMLText(songURL)
    soup = BeautifulSoup(html,"html.parser")
    t = soup.find_all(name='tr',attrs={'class':'even'})
    info = {}
    for i in t:
        try:
            a=i.find_all(name='b')
            b=i.find_all(name='div',attrs={'class':'text'})
            title=a[0].attrs['title']
            sname=b[0].attrs['title']
            
            info[sname]=title
        except:
            continue
    with open("G:/pyjy/gequ/xiangxigedan.txt",'a',encoding = 'utf-8') as f:
                    f.write(str(info)+'\n')

def getSongList(songURL):
    html = getHTMLText(songURL)
    soup = BeautifulSoup(html,"html.parser")
    a = soup.find_all(name='a', attrs={'class': 'tit f-thide s-fc0'})
    for i in a:
        try:
            href = i.attrs['href']
            title = i.attrs['title']
            with open("G:/pyjy/gequ/xiangxigedan.txt",'a',encoding = 'utf-8') as f:
                f.write('\n'+str(title)+'\n')
            getSong(href,title)#lst.append({title:href})
            
        except:
            continue
    
def main():
    song_list_url = "https://music.163.com/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset="
    #url = "https://music.163.com/playlist?id=2474537199"
    depth = 37
    output_file = 'G:/pyjy/Song.txt'
    slist = []
    for i in range(depth):
        try:
            url = song_list_url +str(35*i)
            getSongList(url)
            # writeSongInfo(slist, output_file)
        except:
            continue
    
main()
