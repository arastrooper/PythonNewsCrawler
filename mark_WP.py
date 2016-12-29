import requests
from bs4 import BeautifulSoup
import re

class news_crawl:
    def __init__(self,url):
        self.url=url

    def requests_get(self):
        self.Source_code=requests.get(self.url)
        self.Source_text=self.Source_code.text
        return self.Source_text

    def soup_bs(self):
        self.requests_get()
        self.Soup=BeautifulSoup(self.Source_text)  #transforms the source into readable html
        
      
class news_filter(news_crawl):
#use of inheritance
    def __init__(self,url):
        self.url=url    
        
    def findall_function(self):
        self.soup_bs()
        self.function=self.Soup.find_all('div',{'id':'post_most'})
                 
    def text_extract(self):
        self.findall_function()
        self.text_list=[]
        for self.news in self.function:
            self.news_var1=self.news.find_all('div',{'class':'headline'})
            for self.news_var2 in self.news_var1:
                self.news_text=self.news_var2.text
                self.text_list.append(self.news_text)
        return self.text_list       
                
 
    def link_extract(self):
        self.findall_function()
        self.link_list=[]
        for self.news in self.function:
            self.news_var3=self.news.find_all('a')
            for self.news_var4 in self.news_var3:
                href=self.news_var4.get("href")
                self.link_list.append(href)
        return self.link_list        
        

