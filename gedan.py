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

def getSongList(lst, songURL):
    html = getHTMLText(songURL)
    soup = BeautifulSoup(html,"html.parser")
    a = soup.find_all(name='a', attrs={'class': 'tit f-thide s-fc0'})
    for i in a:
        try:
            href = i.attrs['href']
            title = i.attrs['title']
            lst.append({title:'https://music.163.com'+href})
        except:
            continue
def writeSongInfo(lst,fpath):
    for sid in lst:
        try:
            with open(fpath, 'a',encoding = 'utf-8') as f:
                f.write(str(sid) + '\n')
        except:
            traceback.print_exc()
            continue
    
def main():
    song_list_url = "https://music.163.com/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset="
    depth = 37
    output_file = 'G:/pyjy/SongInfo.txt'
    slist = []
    for i in range(depth):
        try:
            url = song_list_url +str(35*i)
            getSongList(slist, url)
            writeSongInfo(slist, output_file)
        except:
            continue
    
main()
    


