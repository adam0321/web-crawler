# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 20:30:46 2020

@author: USER
"""
#匯入套件
import re
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#使用read_csv讀取檔案
data=pd.read_csv("C:/Users/USER/Desktop/期末專題python/tomatoes_new.csv",engine='python')

#將資料做成dataframe型態
df = pd.DataFrame(data)

#去除\n和''
df = df.replace(r'\\n','', regex=True)
df=df.replace(r' ','', regex=True)


#將star一個一個取出用split將資料依據逗號分開，並存回去原本的欄位
for ind in df.index:
    a=re.split(',',df['star'][ind])   
    print(df['star'][ind])
    df['star'][ind]=a







#爛番茄100名導演
#計算資料中的導演出現次數，並將資料做成df1的資料框
df1=pd.value_counts(df['directed'])

#將做好的資料框設定欄位名稱，設定為directed和counts
df1=df1.rename_axis('directed').reset_index(name='counts')

#保留次數大於1的資料
df1=df1[df1['counts']>1]

#設定要做的圖片大小寬高為12和6英吋
plt.figure(figsize=(12,6))

#做一個橫向長條圖，設定顏色
plt.barh(df1['directed'],df1['counts'],color=["#2E86AB", "#424B54", "#00A6A6", "#F24236", "#9E643C", "#f7bb5f", "#EDE6F2","#E9D985", "#8C4843", "#90d595", "#e48381", "#090446", "#f7bb5f", "#eafb50","#adb0ff",
     "#ffb3ff", "#90d595", "#e48381", "#aafbff",'#746D75'])

#設定x軸標題及粗體 
plt.xlabel("Number of Movie", fontweight = "bold")

#設定y軸標題及粗體            
plt.ylabel("Name", fontweight = "bold")

#設定圖的大標題為RottenTomatoes Top_100 Director，文字大小為15和粗體   
plt.title("RottenTomatoes Top_100 Director", fontsize = 15, fontweight = "bold", y = 1.1)





#爛番茄100名影星
#定義叫y的list
y=[]

#將df['star'][ind]的資料一個個放進y內
for ind in df.index:
    y.extend(df['star'][ind])
    
#定義一個df2的資料框，計算影星的出現數量
df2=pd.value_counts(y)
print(df2)

#定義一個新的df3，欄位為star和counts
df3=df2.rename_axis('star').reset_index(name='counts')

#然後只取出大於2次出現在榜上的影星
df3=df3[df3['counts']>2]

#排序名字A-Z
df3=df3.sort_values('star')

#設定圖案大小
plt.figure(figsize=(16,12))

#做橫向的長條圖，設定顏色
plt.barh(df3['star'],df3['counts'],color=["#2E86AB", "#424B54", "#00A6A6", "#F24236", "#9E643C", "#f7bb5f", "#EDE6F2","#E9D985", "#8C4843", "#90d595", "#e48381", "#090446", "#f7bb5f", "#eafb50","#adb0ff",
     "#ffb3ff", "#90d595", "#e48381", "#aafbff",'#746D75'])

#設定x軸標題及粗體
plt.xlabel("Number of Movie", fontweight = "bold")

#設定y軸標題及粗體
plt.ylabel("Name", fontweight = "bold")

#設定圖的大標題為RottenTomatoes Top_100 star，文字大小為23和粗體
plt.title("RottenTomatoes Top_100 star", fontsize = 23, fontweight = "bold", y = 1.1)
 




#根據觀眾評分>94的電影(1998後)評論做文字雲
#使用read_csv讀取檔案
data=pd.read_csv("C:/Users/USER/Desktop/期末專題python/tomatoes_new.csv",engine='python')

#將資料做成dataframe型態
df = pd.DataFrame(data)


#去除\n、''、%
df = df.replace(r'\\n','', regex=True)
df = df.replace(r'\%','', regex=True)
df = df.replace(r'\'','', regex=True)

#將audience_score和rank轉成int型態
df['audience_score'] = df['audience_score'].astype(int)
df['rank'] = df['rank'].astype(int)

#依照audience_score做排序
df=df.sort_values('audience_score',ascending=False)
df['audience_score']

#定義一個a的list
a=[]

#將分數大於等於94分且1998年後的影片資料取出
for ind in df.index:
    if df['audience_score'][ind]>=94 and df['year'][ind] >= 1998:
        a.append((df['rank'][ind]-1))
#將編號結果呈現出來
print(a)




#Spider-Man: Far From Home (2019)
#透過上面的結果，將專業評論取出
text=""
text=(df['critic_revies'][58])
print(text)

#透過WordCloud套件將評論製作成文字雲，底色為白色
wordcloud = WordCloud(width=480, height=480, margin=0,background_color='white').generate(text)

#調整圖的樣式
plt.imshow(wordcloud, interpolation='bilinear')

#將軸關閉
plt.axis("off")

#設定邊距
plt.margins(x=0, y=0)

#顯示結果
plt.show()




#Coco (2017)
#透過上面的結果，將專業評論取出
text=""
text=(df['critic_revies'][28])
print(text)

#透過WordCloud套件將評論製作成文字雲，底色為白色
wordcloud = WordCloud(width=480, height=480, margin=0,background_color='white').generate(text)

#調整圖的樣式
plt.imshow(wordcloud, interpolation='bilinear')

#將軸關閉
plt.axis("off")

#設定邊距
plt.margins(x=0, y=0)

#顯示結果
plt.show()

#Won't You Be My Neighbor? (2018)
#透過上面的結果，將專業評論取出
text=""
text=(df['critic_revies'][81])
print(text)

#透過WordCloud套件將評論製作成文字雲，底色為白色
wordcloud = WordCloud(width=480, height=480, margin=0,background_color='white').generate(text)

#調整圖的樣式
plt.imshow(wordcloud, interpolation='bilinear')

#將軸關閉
plt.axis("off")

#設定邊距
plt.margins(x=0, y=0)

#顯示結果
plt.show()
    




#TOY STORY 4    
#透過上面的結果，將專業評論取出
text=""
text=(df['critic_revies'][3])
print(text)

#透過WordCloud套件將評論製作成文字雲，底色為白色
wordcloud = WordCloud(width=480, height=480, margin=0,background_color='white').generate(text)

#調整圖的樣式
plt.imshow(wordcloud, interpolation='bilinear')

#將軸關閉
plt.axis("off")

#設定邊距
plt.margins(x=0, y=0)

#顯示結果
plt.show()





#根據爛番茄指數滿分的電影(1998後)評論做文字雲
#使用read_csv讀取檔案
data=pd.read_csv("C:/Users/USER/Desktop/期末專題python/tomatoes_new.csv",engine='python')

#將資料做成dataframe型態
df = pd.DataFrame(data)


#去除\n、''、%
df = df.replace(r'\\n','', regex=True)
df = df.replace(r'\%','', regex=True)
df = df.replace(r'\'','', regex=True)


#將tmeter_score和rank轉成int型態
df['tmeter_score'] = df['tmeter_score'].astype(int)
df['rank'] = df['rank'].astype(int)

#依照tmeter_score做排序
df=df.sort_values('tmeter_score',ascending=False)


#定義一個a的list
a=[]

#將爛番茄指數等於100分且1998年後的影片資料取出
for ind in df.index:
    if df['tmeter_score'][ind] == 100 and df['year'][ind] >= 1998:
        a.append((df['rank'][ind]-1))
print(a)



#Paddington 2 
#透過上面的結果，將專業評論取出
text=""
text=(df['critic_revies'][50])
print(text)

#透過WordCloud套件將評論製作成文字雲，底色為亮黃色
wordcloud = WordCloud(width=480, height=480, margin=0,background_color="lightyellow").generate(text)
plt.imshow(wordcloud, interpolation='bilinear')

#將軸關閉
plt.axis("off")

#設定邊距
plt.margins(x=0, y=0)

#顯示結果
plt.show()

#Leave no trace (2018)
#透過上面的結果，將專業評論取出
text=""
text=(df['critic_revies'][57])
print(text)

#透過WordCloud套件將評論製作成文字雲，底色為亮黃色
wordcloud = WordCloud(width=480, height=480, margin=0,background_color="lightyellow").generate(text)
plt.imshow(wordcloud, interpolation='bilinear')

#將軸關閉
plt.axis("off")

#設定邊距
plt.margins(x=0, y=0)

#顯示結果
plt.show()


#Toy Story 2
#透過上面的結果，將專業評論取出
text=""
text=(df['critic_revies'][90])
print(text)

#透過WordCloud套件將評論製作成文字雲，底色為亮黃色
wordcloud = WordCloud(width=480, height=480, margin=0,background_color="lightyellow").generate(text)
plt.imshow(wordcloud, interpolation='bilinear')

#將軸關閉
plt.axis("off")

#設定邊距
plt.margins(x=0, y=0)

#顯示結果
plt.show()


    


