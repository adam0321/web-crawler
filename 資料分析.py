# -*- coding: utf-8 -*-
#匯入套件
import pandas as pd
import matplotlib.pyplot as plt
import re
import squarify
import matplotlib.pyplot as plt


#透過pandas套件將csv匯入
data=pd.read_csv("C:/Users/USER/Desktop/期末專題python/imdb編碼.csv",engine='python')

#將資料以dataframe形式讀取
df = pd.DataFrame(data)

#將錯誤的資料移回正確位置，例如See more
for ind in df.index:
    if  ("See more" in df['language'][ind])==True:
        df['language'][ind]= df['country'][ind]
        df['country'][ind]=['See more']


#洗掉不要的資料，將逗號做分離，並扣除掉最後一筆不相關的資料
for ind in df.index:
    a=re.split(',',df['type'][ind])    
    a.remove(a[-1])
    df['type'][ind]=a

for ind in df.index:
    a=re.split(',',df['star'][ind])    
    a.remove(a[-1])
    df['star'][ind]=a

   
    
    
#做一個country次數的dataframe，由於資料過難處理，所以透過最基礎的計算方式
#將各個國家設為參數0
NewZealand=Turkey=Iran=USA=UK=Italy=France=Japan=Brazil=SouthKorea=Canada=Germany=India=Czechoslovakia=Spain=Denmark=Sweden=Australia=China=Seemore=Cyprus=Qatar=Lebanon=Mexico=Argentina=Ireland=SouthAfrica=0
#以for迴圈判斷資料是否為特定國家，若是的話就加一
for ind in df.index:
    if('New Zealand' in df['country'][ind])==True:
        NewZealand+=1
    if('Turkey' in df['country'][ind])==True:
        Turkey+=1
    if('Iran' in df['country'][ind])==True:
        Iran+=1
    if('USA' in df['country'][ind])==True:
        USA+=1
    if('UK' in df['country'][ind])==True:
        UK+=1
    if('Italy' in df['country'][ind])==True:
        Italy+=1
    if ('France' in df['country'][ind])==True:
        France+=1
    if ('Japan' in df['country'][ind])==True:
        Japan+=1
    if ("Brazil" in df['country'][ind])==True:
        Brazil+=1
    if ("South Korea" in df['country'][ind])==True:
        SouthKorea+=1
    if ("Canada" in df['country'][ind])==True:
        Canada+=1
    if ("Germany" in df['country'][ind])==True:
        Germany+=1
    if ("India" in df['country'][ind])==True:
        India+=1
    if ("Canada" in df['country'][ind])==True:
        Canada+=1
    if ("Czechoslovakia" in df['country'][ind])==True:
        Czechoslovakia+=1
    if ("Spain" in df['country'][ind])==True:
        Spain+=1
    if ('Denmark' in df['country'][ind])==True:
        Denmark+=1
    if ('Sweden' in df['country'][ind])==True:
        Sweden+=1
    if ('Australia' in df['country'][ind])==True:
        Australia+=1
    if ('China' in df['country'][ind])==True:
        China+=1
    if ('See more' in df['country'][ind])==True:
        Seemore+=1
    if ('Cyprus' in df['country'][ind])==True:
        Cyprus+=1
    if ('Qatar' in df['country'][ind])==True:
        Qatar+=1
    if ('Lebanon' in df['country'][ind])==True:
        Lebanon+=1
    if ('Mexico' in df['country'][ind])==True:
        Mexico+=1
    if ('Argentina' in df['country'][ind])==True:
        Argentina+=1
    if ('Ireland' in df['country'][ind])==True:
        Ireland+=1
    if ('South Africa' in df['country'][ind])==True:
        SouthAfrica+=1
#最後將計算出來的結果print出來
print(NewZealand,Turkey,Iran,USA,UK,Italy,France,Japan,Brazil,SouthKorea,Canada,Germany,India,Czechoslovakia,Spain,Denmark,Sweden,Australia,China,Seemore,Cyprus,Qatar,Lebanon,Mexico,Argentina,Ireland,SouthAfrica)

#將這些數字與國家名稱對應起來，命名為data2
data2={'country':['NewZealand','Turkey','Iran','USA','UK'
                  ,'Italy','France','Japan','Brazil','S.Korea'
                  ,'Canada','Germany','India','Czechoslovakia','Spain'
                  ,'Denmark','Sweden','Australia','China','Cyprus','Qatar','Lebanon'
                  ,'Mexico','Argentina','Ireland','S.Africa'],
       'count':[3,1,2,122,31,5,14,7,1,4,12,14,6,1,5,1,1,5,2,1,1,1,2,2,1,2]}
#然後用pandas將data2做成資料框的型態
df2=pd.DataFrame(data2)
df2


#國家的treeplot，看國家的數量大小
#設定treeplot的資料為剛剛的df2，設定為文字標題為國家名，設定顏色、文字大小
squarify.plot(sizes=df2['count'], label=df2['country'],color=["#2E86AB", "#424B54", "#00A6A6", "#F24236", "#9E643C", "#f7bb5f", "#EDE6F2","#E9D985", "#8C4843", "#90d595", "#e48381", "#46A3FF", "#f7bb5f", "#eafb50","#adb0ff",
     "#ffb3ff", "#90d595", "#e48381", "#aafbff","#746D75","#02F78E",'#5CADAD','#FFAF60','#5CADAD','#FFD306'],alpha=.8,text_kwargs={'fontsize':7})
#關閉圖的軸
plt.axis('off')

#將檔案存成country.jpg，dpi為200
plt.savefig('country.jpg', dpi=200)

#呈現圖的結果
plt.show()




#有3個或以上的電影在排行榜內的導演
#計算df['director']的數量，並存成df6
df6=pd.value_counts(df['director'])

#定義一個df6，設定欄位為directors和counts
df6=df6.rename_axis('director').reset_index(name='counts')
print (df6)

#然後只取出出現次數大於2的導演
df6=df6[df6['counts']>2]

#設定圖片大小寬12高6
plt.figure(figsize=(12,6))

#製作橫向的長條圖，並設定顏色
plt.barh(df6['director'],df6['counts'],color=["#2E86AB", "#424B54", "#00A6A6", "#F24236", "#9E643C", "#f7bb5f", "#EDE6F2","#E9D985", "#8C4843", "#90d595", "#e48381", "#090446", "#f7bb5f", "#eafb50","#adb0ff",
     "#ffb3ff", "#90d595", "#e48381", "#aafbff",'#746D75'])

# 設定x軸標題及粗體
plt.xlabel("Number of Movie", fontweight = "bold")    

# 設定y軸標題及粗體            
plt.ylabel("Name", fontweight = "bold")

# 設定圖案標題名稱、字體大小和粗體
plt.title("IMDB Top_250 Director", fontsize = 15, fontweight = "bold", y = 1.1) 

#將資料存成imdbDirector.jpg，解析度為200dpi
plt.savefig('imdbDirector.jpg', dpi=200)





#演員連續上榜
#定義叫y的list，先塞入' '
y=[' ']
#再將' '，從中刪除 
y.remove(' ')

#將df['star'][ind]的資料一個個放進y內
for ind in df.index:
    print(df['star'][ind])
    y.extend(df['star'][ind])
    
#定義一個df8的資料框，計算影星的出現數量
df8=pd.value_counts(y)

#定義一個新的df9，欄位為star和counts
df9=df8.rename_axis('star').reset_index(name='counts')

#排序名字A-Z
df9=df9.sort_values('star')

#然後只取出大於2次出現在榜上的影星
df9=df9[df9['counts']>2]

#設定圖案大小
plt.figure(figsize=(16,12))

#做橫向的長條圖，設定顏色
plt.barh(df9['star'],df9['counts'],color=["#2E86AB", "#424B54", "#00A6A6", "#F24236", "#9E643C", "#f7bb5f", "#EDE6F2","#E9D985", "#8C4843", "#90d595", "#e48381", "#090446", "#f7bb5f", "#eafb50","#adb0ff",
     "#ffb3ff", "#90d595", "#e48381", "#aafbff",'#746D75'])

# 設定x軸標題及粗體
plt.xlabel("Number of Movie", fontweight = "bold")   
   
# 設定y軸標題及粗體 
plt.ylabel("Name", fontweight = "bold")
plt.title("IMDB Top_250 Star", fontsize = 23, fontweight = "bold", y = 1.1) 



