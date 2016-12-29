from Tkinter import *
#from PIL import Image, ImageTk

import PIL
import webbrowser
import mark_TOI
import mark_BBC
import mark_WP
import WP_image
import pywapi



class TheNewsCrawler:
    def __init__(self, master):
        self.master = master

        self.master.geometry("750x700")
        master.title("The News Crawler")

        self.frame_all=Frame(master, bg='#333')
        self.frame_all.pack(fill=BOTH, expand=YES)

        self.title=Label(self.frame_all, bg='#333', text='THE NEWS CRAWLER', fg='white', font = ("Purisa",26))
        self.title.pack(side=TOP)

        self.bg_wp = PhotoImage(file="wp.gif")
        self.bg_toi = PhotoImage(file="toi-back.gif")
        self.bg_bbc = PhotoImage(file="bbc-bg.gif")
        self.weather_image=PhotoImage(file="w_logo.gif")
        self.w_WP = self.bg_wp.width()
        self.h_WP = self.bg_wp.height()
        self.w_toi = self.bg_toi.width()
        self.h_toi = self.bg_toi.height()
        self.w_bbc = self.bg_bbc.width()
        self.h_bbc = self.bg_bbc.height()

        self.TOI_url='http://timesofindia.indiatimes.com/'
        self.BBC_url='http://www.bbc.com/'
        self.WP_url='http://www.washingtonpost.com/?reload=true'

        self.image=WP_image.image_down(self.WP_url)
        self.image.Download()

        self.big_frame1=Frame(self.frame_all)
        self.big_frame1.pack(expand=YES, side=TOP)

        self.w_frame=Frame(self.frame_all, bg="white", width=8000, height=200)
        self.w_frame.pack(expand=YES)

        self.big_frame2=Frame(self.frame_all)
        self.big_frame2.pack(expand=YES, side=BOTTOM)

        
        self.upframe=Frame(self.big_frame1, width=self.w_WP, height=self.h_WP)
        self.upframe.pack(expand=YES)
        self.background_upframe = Label(self.upframe, image=self.bg_wp, bd=4)
        self.background_upframe.pack(fill=BOTH, expand=YES)
        self.background_upframe.place(x=0, y=0, relwidth=1, relheight=1)
        self.background_upframe.image = self.bg_wp
        # save the image from 'garbage collection'
        
        self.frame1=Frame(self.big_frame2, width=self.w_toi, height=self.h_toi)
        self.frame1.pack(expand=YES, side=LEFT)
        self.background_frame1 = Label(self.frame1, image=self.bg_toi, bd=4)
        self.background_frame1.pack(fill=BOTH, expand=YES)
        self.background_frame1.place(x=0, y=0, relwidth=1, relheight=1)
        self.background_frame1.image = self.bg_toi
        # save the image from 'garbage collection'
        

        self.frame2=Frame(self.big_frame2, width=self.w_bbc, height=self.h_bbc)
        self.frame2.pack(expand=YES, side=RIGHT)
        self.background_frame2 = Label(self.frame2, image=self.bg_bbc, bd=4)
        self.background_frame2.pack(fill=BOTH, expand=YES)
        self.background_frame2.place(x=0, y=0, relwidth=1, relheight=1)
        self.background_frame2.image = self.bg_bbc
        # save the image from 'garbage collection'


        self.WP=mark_WP.news_filter(self.WP_url)
        self.WP_news_text=self.WP.text_extract()
        self.WP_news_link=self.WP.link_extract()

        self.background_upframe.columnconfigure(1, weight=1)
        self.background_upframe.columnconfigure(3, pad=7)
        self.background_upframe.rowconfigure(3, weight=1)
        self.background_upframe.rowconfigure(5, pad=7)

        self.inside_frame=Frame(self.background_upframe)
        self.inside_frame.grid(row=3, column=1, columnspan=3, rowspan=4)
        self.inside_button=Frame(self.background_upframe)
        self.inside_button.grid(row=5, column=3)

        

        #news headlines of Washington Post use label with variable string element, changed on each button clicked  
        self.WP_label_index = 0
        self.WP_label_text = StringVar()
        self.WP_label_text.set(self.WP_news_text[self.WP_label_index])
        self.up_news_label=Label(self.inside_frame, textvariable=self.WP_label_text, anchor=W, justify=LEFT, wraplengt=200, width=40)
        self.up_news_label.pack(side=RIGHT, padx=5)

        self.key_name=['url1','url2','url3','url4','url5']
        self.image_label_index=0
        self.im=Image.open(self.key_name[self.image_label_index]+".jpg")
        self.img=ImageTk.PhotoImage(self.im)
        self.image_label=Label(self.inside_frame, bd=5, relief=RAISED, image=self.img)
        self.image_label.pack(side=RIGHT)

        self.up_link_button=Button(self.inside_button, relief=RAISED, text= 'SEE THIS ON THE WEB', command=self.WP_link_open)
        self.up_news_change_button=Button(self.inside_button, relief=RAISED, text= 'NEXT NEWS', command=self.News_Image_change_button)
        self.up_link_button.pack(side=RIGHT, padx=5, pady=5)
        self.up_news_change_button.pack(side=RIGHT)

        # assigning button to open dialogue box for wheather search
        self.weather_button=Button(self.w_frame, text="click for weather updates of your place", command=self.weather)
        self.weather_button.pack(side=RIGHT)
        self.weather_logo=Label(self.w_frame, image=self.weather_image)
        self.weather_logo.pack(side=LEFT)
        self.weather_logo.image = self.weather_image

        # news headlines from Times of India
        # each title is linked to its page
        self.TOI=mark_TOI.news_filter(self.TOI_url)
        self.TOI_news_text=self.TOI.text_extract()
        self.TOI_news_link=self.TOI.link_extract()

        self.TOI_title_label = Label(self.background_frame1, text="Times of India", fg = "blue", font = ("Purisa",20))
        self.TOI_title_label.pack(side=TOP)
        self.TOI_label_index = 0

        self.TOI_label_1 = Label(self.background_frame1, text=self.TOI_news_text[0])
        self.TOI_label_1.bind("<Button-1>", self.TOI_link_open)
        self.TOI_label_1.pack()

        self.TOI_label_2 = Label(self.background_frame1, text=self.TOI_news_text[1])
        self.TOI_label_2.bind("<Button-1>", self.TOI_link_open)
        self.TOI_label_2.pack()


        self.TOI_label_3 = Label(self.background_frame1, text=self.TOI_news_text[2])
        self.TOI_label_3.bind("<Button-1>", self.TOI_link_open)
        self.TOI_label_3.pack()

        self.TOI_label_4 = Label(self.background_frame1, text=self.TOI_news_text[3])
        self.TOI_label_4.bind("<Button-1>", self.TOI_link_open)
        self.TOI_label_4.pack()

        self.TOI_label_5 = Label(self.background_frame1, text=self.TOI_news_text[4])
        self.TOI_label_5.bind("<Button-1>", self.TOI_link_open)
        self.TOI_label_5.pack()

        self.TOI_label_6 = Label(self.background_frame1, text=self.TOI_news_text[5])
        self.TOI_label_6.bind("<Button-1>", self.TOI_link_open)
        self.TOI_label_6.pack()

        self.TOI_label_7 = Label(self.background_frame1, text=self.TOI_news_text[6])
        self.TOI_label_7.bind("<Button-1>", self.TOI_link_open)
        self.TOI_label_7.pack()
        
        #news headlines from BBC news
        #each title is linked to its page 
        self.BBC=mark_BBC.news_filter(self.BBC_url)
        self.BBC_news_text=self.BBC.text_extract()
        self.BBC_news_link=self.BBC.link_extract()

        self.BBC_title_label = Label(self.background_frame2, text="BBC.COM", fg = "blue", font = ("Purisa",20))
        self.BBC_title_label.pack(side=TOP)
        self.BBC_label_index = 0

        self.BBC_label_1 = Label(self.background_frame2, text=self.BBC_news_text[0])
        self.BBC_label_1.bind("<Button-1>", self.BBC_link_open)
        self.BBC_label_1.pack()

        self.BBC_label_2 = Label(self.background_frame2, text=self.BBC_news_text[1])
        self.BBC_label_2.bind("<Button-1>", self.BBC_link_open)
        self.BBC_label_2.pack()


        self.BBC_label_3 = Label(self.background_frame2, text=self.BBC_news_text[2])
        self.BBC_label_3.bind("<Button-1>", self.BBC_link_open)
        self.BBC_label_3.pack()

        self.BBC_label_4 = Label(self.background_frame2, text=self.BBC_news_text[3])
        self.BBC_label_4.bind("<Button-1>", self.BBC_link_open)
        self.BBC_label_4.pack()

        
    def News_Image_change_button(self):
        self.WP_label_index += 1
        self.image_label_index += 1
        self.WP_label_index %= len(self.WP_news_text)     #wraps the text around after limit reached
        self.image_label_index %= len(self.key_name)      #wraps the image around 
        self.WP_label_text.set(self.WP_news_text[self.WP_label_index])
        self.im2=Image.open(self.key_name[self.image_label_index]+".jpg")
        self.img2=ImageTk.PhotoImage(self.im2)
        self.image_label.configure(image = self.img2)
        self.image_label.image=self.img
        # save the image from 'garbage collection'

    def weather(self):
        self.top=Toplevel(self.master) #use of toplevel to create dialogue box
        self.top.title="Weather Updates"
        self.weather_label = Label(self.top, text="Enter name in below box \n Eg. london,uk ")
        self.weather_label.pack()
        self.entry = Entry(self.top, bd =5)
        self.entry.pack()
        self.button=Button(self.top, text="OK", command=self.weather_show)
        self.button.pack()
        

    def weather_show(self):
       
       self.city=self.entry.get()
       '''a deliberate use of exceptions here to stop error
          when user types in a unidentified name'''
       try:
           self.lookup = pywapi.get_location_ids(self.city)
       except (KeyError, RuntimeError, TypeError, NameError, AttributeError, ):
           print("no info of this place")
       '''The following  code is given in the API user manule to search for
          location id and procure weather condition'''
       for i in self.lookup:
           self.location_id = i
       weather_com_result = pywapi.get_weather_from_weather_com(self.location_id)
       self.weather_text="Weather.com says: It is " + weather_com_result['current_conditions']['text'].lower() + " and " + weather_com_result['current_conditions']['temperature'] + "°C now in " + str.upper(self.city)
       self.q=Label(self.top, text=self.weather_text)
       self.q.pack(side=BOTTOM)

    def WP_link_open(self):
        webbrowser.open(self.WP_news_link[self.WP_label_index],new=2,autoraise=True)
                                        

    def TOI_link_open(self, event):
        self.TOI_label_index += 1
        webbrowser.open(self.TOI_url+self.TOI_news_link[self.TOI_label_index],new=2,autoraise=True)
        

    def BBC_link_open(self, event):
        self.BBC_label_index += 1
        webbrowser.open(self.BBC_news_link[self.BBC_label_index],new=2,autoraise=True)
        


                                     
root = Tk()
gui = TheNewsCrawler(root)
root.mainloop()        
      
