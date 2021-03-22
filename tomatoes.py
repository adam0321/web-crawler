# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 13:13:50 2020
#import matplotlib.pyplot as plt
import numpy as np
@author: USER
"""
#匯入套件
import pandas as pd
import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import messagebox


#將下方主程式傳上來url做成深入爬取得網頁
def detail (url):
    
    #設定成新的url request
    res = requests.get(url)
    
    #設定Beautifulsoup解析網頁資料，使用lxml
    soup = BeautifulSoup(res.content, 'lxml')
    
    #抓取網頁架構中的.mop-ratings-wrap__percentage的資料
    a_s=soup.select('.audience-score .mop-ratings-wrap__percentage')
    
    #將資料的文字存成變數audience_score
    audience_score=[c.text for c in a_s]
    
    #抓取網頁架構中的li的所有資料
    tag=soup.find('ul','content-meta info').find_all('li')
    
    #從li中抓出第一筆資料(電影的排名)
    rating=tag[0].find('div','meta-value').text
    
    #從li中抓出第二筆資料(電影的歸類)
    genre=tag[1].find('div','meta-value').text
    
    #從li中抓出第三筆資料(所有的導演列表)
    direct=tag[2].find('div','meta-value').find_all('a')
    
    #從li中抓出第四筆資料(所有的作者列表)
    write=tag[3].find('div','meta-value').find_all('a')
    
    #定義directed和written的list
    directed=[]
    written=[]
    
    #將列表中的導演一個個從進list
    for a in direct:
        directed.append(a.text)
        
    #將列表中的作者一個個從進list
    for c in write:
        written.append(c.text)
        
    #抓取網頁架構中的.media-body a span的所有資料
    tags2 = soup.select('.media-body a span')

    #從.media-body a span中將所有的影星名字一個個塞進star的list中
    star = [c.text for c in tags2 ]

    #抓取網頁架構中的#reviews p的資料
    CR= soup.select('#reviews p')

    #從#reviews p中將所有的影評專家一個個塞進critic_reviews的list中
    critic_reviews=[c.text for c in CR ]

    #抓取網頁架構中的的#audience_reviews .js-clamp資料
    AR= soup.select('#audience_reviews .js-clamp')

    #從#audience_reviews .js-clamp中將所有觀眾的影評一個個塞進audience_reviews的list中
    audience_reviews=[c.text for c in AR ]

    #將抓下的資料回傳回去
    return rating,audience_score,genre,directed,written,star,critic_reviews,audience_reviews



#主程式catch，對排行中每一欄的做資料擷取，並用接截下的url傳給上方的function，並將回傳值與截取的值做成list
def catch():
    #url_top_100輸入爛番茄前100的網址
    #prefix設定為爛番茄的domain name
    url_top_100 = 'https://www.rottentomatoes.com/top/bestofrt/'
    prefix = 'https://www.rottentomatoes.com/'
    #利用request套件對剛剛的網址建立請求
    res = requests.get(url_top_100)

    #設定Beautifulsoup解析網頁資料，使用lxml(官方推薦較強的解析器)
    soup = BeautifulSoup(res.content, 'lxml')

    #抓取網頁架構中的table的所有資料
    table = soup.find('div', class_='panel-body content_body allow-overflow').find('table')

    #並從table取出我們要的tr部分
    trs = table.find_all('tr')
    movie_list = []

    #使用for迴圈從剛找到tr中一個個取出，並將資料存在的class中取出要的資料
    for i, tr in enumerate(trs[1:]):
        tmeter_score = int(tr.find(class_='tMeterScore').text.strip()[:-1]) 
        title = tr.find(class_='unstyled articleLink').text.strip()

        #取出這部電影詳細簡介子網頁的網址
        url = prefix + tr.find(class_='unstyled articleLink').get('href').strip()
        no_of_reviews = int(tr.find(class_='right hidden-xs').text.strip())
        
        #將取出的子網頁當參數傳到面的detail方法中，將回傳的值一個個用變數存取
        rating,audience_score,genre,directed,written,star,critic_reviews,audience_reviews=detail(url)
        
        #確認存取的資料是否正確回傳或抓取
        print(title,tmeter_score,no_of_reviews,url,rating,audience_score,genre,directed,written,star)
        
        #將每個title合在一起
        text1.insert(END,str(i+1)+"."+title+'\n')
        
        #將所有title的結果呈現在GUI視窗上，根據橫方向排列呈現
        text1.pack()

        #在製作一個movie_list，將所有抓下的資料存進去裡面
        movie_list.append({
                          'rank': i+1,
                          'tmeter_score': tmeter_score,
                          'title': title,
                          'url': url,
                          'no_of_reviews': no_of_reviews,
                          'audience_score':audience_score,
                          'rating':rating,
                          'genre':genre,
                          'directed':directed,
                          'written':written,
                          'star':star,
                          'critic_reviews':critic_reviews,
                          'audience_reviews':audience_reviews
                          })

    #並將movie_list利用Panda套件作成dataframe，並定義欄位的名字，存成.csv檔
    df = pd.DataFrame(movie_list, columns=['rank','tmeter_score','title','url','no_of_reviews',
                                           'audience_score','rating','genre','directed',
                                           'written','star','critic_reviews','audience_reviews'])
    df['year'] = df['title'].str.slice(-5,-1).astype(int)
    df.to_csv('tomatoes.csv')
    

#GUI
#設定一個叫做window的新視窗
window = Tk()

#將視窗的title換成一鍵爬蟲
window.title("一鍵爬蟲")

#視窗的長寬變成500*250
window.geometry("500x250")

#設定視窗的最大的大小
window.maxsize(1200,1000)

#定義一個捲軸
sbar1 = Scrollbar(window)

#設定文字大小寬為60高為50
text1 = Text(window, width = 60, height = 50, wrap = WORD)

#將捲軸的command選擇性參數設定為text1.yview，表示當移動捲軸時，會呼叫yview()方法捲動文字區域內容
sbar1["command"] = text1.yview

#將文字區域的yscrollcommand選擇性參數設定為sbar1.set，表示將捲軸連接到文字區域
text1["yscrollcommand"] = sbar1.set

#設定Button的文字，然後點下後會呼叫catch方法
btn1 = Button(window, text = "按下爬取爛番茄", command = catch)

#將btn1根據橫方向排列呈現
btn1.pack()

#加入一個紅色label做提醒
label1 = Label(window, text = "非動態新增，按下後請稍等...", width = 30, bg = "red")

#將label1根據橫方向排列呈現
label1.pack()

#進入等待處理物件的狀態
window.mainloop()

