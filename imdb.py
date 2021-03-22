# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 16:44:06 2020

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
    
    #選取網頁架構中的div.credit_summary_item的資料
    credit_summary_item = soup.select('div.plot_summary_wrapper div.credit_summary_item')
    
    #從上方選出的credit_summary_item中取出第一個a的文字，命名為director
    director=credit_summary_item[0].select_one('a').text
    
    #從上方選出的credit_summary_item中取出第二個a的文字，命名為writer
    writer=credit_summary_item[1].select_one('a').text  

    #從上方選出的credit_summary_item中取出第三個a的文字，塞入名為star的list中
    stars = [s.text for s in credit_summary_item[2].select('a') ]

    #選取網頁架構中的#titleDetails > div的資料
    a_tags = soup.select('#titleDetails > div')
    
    #從上方選出的a_tags中取出第二個a的文字，塞入名為country的list中
    country = [c.text for c in a_tags[1].select('a') ]
    
    #從上方選出的a_tags中取出第三個a的文字，塞入名為country的list中
    language = [l.text for l in a_tags[2].select('a') ]

    #截取網頁架構中div.subtext time的資料，命名為long
    long=soup.select_one('div.subtext time').text.strip()
    
    #截取網頁架構中div.ratingValue strong span的資料，命名為rating
    rating=soup.select_one('div.ratingValue strong span').text
    
    #截取網頁架構中span#titleYear a的資料，命名為year
    year=soup.select_one('span#titleYear a').text
    
    #截取網頁架構中div.subtext a的資料，命名為typ
    typ=soup.select('div.subtext a')
    
    #從typ中將資料一個個存進mtype的list中
    mtype = [c.text for c in typ ]
    
    #將上方抓取的資料顯示出來，確認是否成功
    print(stars,country,language,director,writer,long,rating,year,mtype)
    
    #將資料坐回傳，回傳catch的地方
    return stars,country,language,director,writer,long,rating,year,mtype
   
#主程式catch，對排行中每一欄的做資料擷取，並用接截下的url傳給上方的function，並將回傳值與截取的值做成list
def catch():
    
    #url_top_250輸入IMDB前250的網址
    #prefix設定為爛番茄的domain name
    url_top_250 = 'https://www.imdb.com/chart/top?ref_=nv_mv_250'
    prefix = 'https://www.imdb.com/'

    #利用request套件對剛剛的網址建立請求   
    res = requests.get(url_top_250)
    
    #設定Beautifulsoup解析網頁資料，使用lxml(官方推薦較強的解析器)
    soup = BeautifulSoup(res.content, 'lxml')
    
    #選取網頁架構中的tbody.lister-list tr td.titleColumn的所有資料
    rate_list = soup.select('tbody.lister-list tr td.titleColumn')
    
    #定義一個名叫movie_list的list，準備存放資料
    movie_list = []
    
    #使用for迴圈從剛找到中rate_list一個個取出，並將資料存在的class中取出要的資料    
    for movie in rate_list:
        
        #將數字從movie中取出，分離調.的符號，並存成int的格式
        num=int(movie.text.split('.')[0].strip())
        
        #取出這部電影詳細簡介子網頁的網址
        url=prefix+movie.select_one('a').get('href')
        
        #從movie資料中找出a的文字，存成title
        title=movie.select_one('a').text
        
        #將取出的子網頁當參數傳到面的detail方法中，將回傳的值一個個用變數存取
        stars,country,language,director,writer,long,rating,year,mtype=detail(url)
        
        #確認存取的資料是否正確回傳或抓取
        print(stars,country,language,director,writer,long,rating,year,mtype)
        
        #將每個title合在一起
        text1.insert(END,str(num)+"."+title+'\n')
        
        #將所有title的結果呈現在GUI視窗上，根據橫方向排列呈現
        text1.pack()
        
        #在製作一個movie_list，將所有抓下的資料存進去裡面
        movie_list.append({
                          'title':title,
                          'link':url,
                          'num':num,
                          'rating':rating,
                          'year':year,
                          'long':long,
                          'type':mtype,
                          'director':director,
                          'writer':writer,
                          'star':stars,
                          'country':country,
                          'language':language
                          })
        
    #並將movie_list利用Panda套件作成dataframe，並定義欄位的名字，存成.csv檔       
    df = pd.DataFrame(movie_list, columns=['title','link','num','rating','year',
                                           'long','type','director','writer',
                                           'star','country','language'])
    df.to_csv('imdb.csv')


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
btn1 = Button(window, text = "按下爬取IMDB", command = catch)

#將btn1根據橫方向排列呈現
btn1.pack()

#加入一個黃色label做提醒
label1 = Label(window, text = "非動態新增，按下後請稍等...", width = 30, bg = "yellow")

#將label1根據橫方向排列呈現
label1.pack()

#進入等待處理物件的狀態
window.mainloop()
    
