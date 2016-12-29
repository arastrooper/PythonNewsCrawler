import shutil       # a module used in image file saving and downloading
import requests
from bs4 import BeautifulSoup
from PIL import Image

class image_crawl:
    def __init__(self,url):
        self.url=url

    def requests_get(self):
        self.Source_code=requests.get(self.url)
        self.Source_text=self.Source_code.text
        return self.Source_text

    def soup_bs(self):
        self.requests_get()
        self.Soup=BeautifulSoup(self.Source_text)
        

class image_filter(image_crawl):
#use of inheritance
    def __init__(self,url):
        self.url=url
        
    def findall_function(self):
        self.soup_bs()
        self.function=self.Soup.find_all('div',{'id':'post_most'})

    def link_extract(self):
        self.findall_function()
        self.link_list=[]
        '''the following code has been created to check for image bug
           on the website, the situation when a specific news has not been
           assigned an image by the website buiders, thus the code identifies
           the news without image and an image of a WASHINGTON POST LOGO is
           asigned to it.'''
           
        for self.tag in self.function:
            self.a_tag=self.tag.find_all('a')
        self.index=0
        while self.index<5:  #the while condition checks each news element seperatly
            self.img_list=self.a_tag[self.index].find_all('img')
            if self.img_list:
               for self.src_link in self.img_list:
                   self.im=self.src_link.get("src")
                   self.link_list.append(self.im)
            else:
                self.link_list.append('http://s3.timetoast.com/public/uploads/photos/2820825/washington_post_logo_small_square.jpg?1346856724')
            self.index += 1        
        
class image_down(image_filter):
#use of inheritance
    def __init__(self,url):
        self.url=url
        

    def link_dict(self):
        self.link_extract()
        self.key_name=['url1','url2','url3','url4','url5']
        #the dictionary element is used to download the specific image and give it name for further use
        self.link_dict={}
        self.index=0
        while self.index<5:
            self.key=self.key_name[self.index]
            self.value=self.link_list[self.index]
            self.link_dict[self.key]=self.value
            self.index += 1

    def Download(self):
        self.link_dict()
        for link in self.key_name:
            url=self.link_dict[link]
            response = requests.get(url, stream=True)
            with open(link+".jpg", 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
                # the module shutil takes the file and replaces it with the image
            del response
            # the image in response is deleted to clear memory and remove time tag

        for imageFile in self.key_name:  #the images are resized to make them uniform
            im1 = Image.open(imageFile+".jpg")
            width = 90
            height = 60
            im2 = im1.resize((width, height), Image.ANTIALIAS)
            im2.save(imageFile+".jpg")
            
            

    



