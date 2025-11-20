import requests 
import pandas as pd
import numpy as py
from bs4 import BeautifulSoup





class data_mining_News18:
    def data_mining_News18_Home():
        urls="https://www.news18.com/"
        data = requests.get(urls)
        with open("News28_Home.html","w", encoding="utf-8") as f:
            q = str(data.text)
            f.write(q)
    
    def data_mining_News18_Home_get_url():

        
        maindata = requests.get("https://www.news18.com/")
        soup = BeautifulSoup(maindata.text, 'html.parser')


        find_main = soup.select("main.jsx-b55f31212a5faef4")

        soup = BeautifulSoup(str(find_main), 'html.parser')

        data_urls = []

        for x in soup.find_all('a', href=True):
                if str(x['href']).find(".html") >= 0:
                    data_urls.append(str(x['href']).replace("https://www.news18.com",""))
                else:pass

        return data_urls
    def Create_Csv_Urls(row:list):
        rowform = {
             "URLS":row
        }
        data = pd.DataFrame(rowform)
        data.to_csv("URLS.csv",index=False)

    def News_data(URLS:list):
        title_data =[]
        Image_data =[]
        Text= []
        Topic = []
        coubt = 0
        for like in URLS:

            asop0 = str(like).split("/")
            Topic.append(asop0[1])


            urls = "https://www.news18.com/"+like
            news_data = requests.get(urls,timeout=5)
    
            soup = BeautifulSoup(str(news_data.text), 'html.parser')
            rowdata_1 = soup.find_all("h1")
    
            soup2 = BeautifulSoup(str(rowdata_1), 'html.parser')
            title  = str(soup2.getText())
            title = title.replace("[","")
            title = title.replace("]","")
    
            imag = soup.select_one("figure")
    
            for x in imag.find_all('img'):
                img = x["src"]
    
    
            bodytext = str(soup.find_all("p"))
    
            bodytext = bodytext.replace("[","")
            bodytext = bodytext.replace("]","")


            coubt = coubt +1
            print(f"{coubt}Is Runging...",end="\r")
            title_data.append(title)
            Image_data.append(img)
            Text.append(bodytext)
          
        print("All are done")
        data  ={
            "Title":title_data,
            "Image":Image_data,
            "Text":Text,
            "Topic":Topic
        }
        wfqwf = pd.DataFrame(data)
        return data

 
data  = data_mining_News18.data_mining_News18_Home_get_url()

print(data)