import requests
from bs4 import BeautifulSoup

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
        self.soup_bs()        # calling function from parent class
        self.function=self.Soup.find_all('div',{'class':'top-story'})
                 
    def text_extract(self):
        self.findall_function()
        for self.news in self.function:
            for self.news_var1 in self.news:
                self.news_text=self.news_var1.get_text("\n",strip=True)
                #with the use of new line(\n) in get_text funtion the string is added with a \n whenever line ends 
        return self.news_text.split('\n')        
                     
    def link_extract(self):
        self.findall_function()
        self.link_list=[]
        for self.news in self.function:
            self.news_var2=self.news.find_all('a',{'class':""})
            for self.news_var3 in self.news_var2:
                href=self.news_var3.get("href")
                self.link_list.append(href)
        self.set_list=set(self.link_list)
        # the list is converted to a Set to remove repetitive elements and then reconverted to another list to use further 
        self.final_link_list=list(self.set_list)
        return self.final_link_list
