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
        self.Soup=BeautifulSoup(self.Source_text)   #transforms the source into readable html
        
      
class news_filter(news_crawl):
#use of inheritance
    def __init__(self,url):
        self.url=url    
        
    def findall_function(self):
        self.soup_bs()
        self.function=self.Soup.find_all('div',{'id':'most_popular_tabs_read'})
                 
    def text_extract(self):
        self.findall_function()
        self.text_list=[]
        for self.news in self.function:
            self.news_var1=self.news.find_all('a')
            for self.news_var2 in self.news_var1:
                self.news_text=self.news_var2.get_text("\n",strip=True)
                self.text_list.append(self.news_text)
        self.text_string=".".join(self.text_list)
        self.new_string=re.sub(r'\d*',"",self.text_string)
        # use of reguler expression to remove all digit lements from the string 
        self.new_string1=re.sub(r'\n*',"",self.new_string)
        # use of reguler expression to remove all next line elements from the string.
        self.final_text=self.new_string1.split('.')
        # splitting the string into list elements whenever a '.' element arrives
        return self.final_text

    def link_extract(self):
        self.findall_function()
        self.link_list=[]
        for self.news in self.function:
            self.news_var3=self.news.find_all('a')
            for self.news_var4 in self.news_var3:
                href=self.news_var4.get("href")
                self.link_list.append(href)
        self.set_list=set(self.link_list)
        self.final_link_list=list(self.set_list)
        return self.final_link_list







