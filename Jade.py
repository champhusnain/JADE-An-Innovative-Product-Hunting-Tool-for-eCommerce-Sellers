from multiprocessing import Event
import tkinter
import tkinter.messagebox
import customtkinter
import prophet
# print version number
#print('Prophet %s' % fbprophet.__version__)
from pandas import read_csv
from pandas import read_csv
from pandas import to_datetime
from prophet import Prophet
from matplotlib import pyplot
from pandas import DataFrame
from PIL import ImageTk, Image
from email.policy import default
from gc import callbacks
from os import link
from subprocess import call
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from lxml import html
from scrapy.crawler import CrawlerProcess
import csv
import datetime
from pandas import *
import re
import numpy as np
import pandas
from datetime import date
import json
import re
from urllib.parse import urlencode, urljoin 
from scrapy_splash import SplashRequest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait 
import time
import pandas as pd
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import csv
from pandas import read_csv
import itertools
import glob
import os
import pandas as pd
from sqlalchemy import true
from os import listdir

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.title("JADE")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # ============ create left frame ============

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        # ============ create right frame ============

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        image = Image.open("/home/champ/Downloads/MS PROJECT/Project/JADE/DB/JADE LOGO@4x.png").resize((self.WIDTH, self.HEIGHT))
        self.bg_image = ImageTk.PhotoImage(image)

        self.image_label = tkinter.Label(master=self.frame_right, image=self.bg_image)
        self.image_label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.button_5 = customtkinter.CTkButton(master=self.frame_right,
                                                text="CONTINNUE",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.button_event_right_frame_productsdata)
        self.button_5.grid(row=8, column=2, columnspan=1, pady=20, padx=20, sticky="we")



        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(3, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(7, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="JADE",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        self.label_2 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Welcome to Jade!",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_2.grid(row=2, column=0, pady=10, padx=10)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Products Data",
                                                command=self.button_event_right_frame_productsdata)
        self.button_1.grid(row=4, column=0, pady=10, padx=20)

        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Selling History",
                                                command=self.button_event_right_frame_saleshistory)
        self.button_2.grid(row=5, column=0, pady=10, padx=20)

        self.button_3 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Future Analysis",
                                                command=self.button_event_right_frame_futureanalysis)
        self.button_3.grid(row=6, column=0, pady=10, padx=20)

        self.button_4 = customtkinter.CTkButton(master=self.frame_left,
                                                text="INFO",
                                                command=self.button_event_info)
        self.button_4.grid(row=8, column=0, pady=10, padx=20)

        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Appearance Mode:")
        self.label_mode.grid(row=9, column=0, pady=0, padx=20, sticky="w")

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=["Light", "Dark", "System"],
                                                        command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        # ============ frame_right ============

    #Events    

    #def button_event_right_frame_contact(self):

        # set default values
        self.optionmenu_1.set("Dark")
        
        

    def button_event_right_frame_productsdata(self):

        # ============ create right frame ============

        self.frame_right1 = customtkinter.CTkFrame(master=self)
        self.frame_right1.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right1.rowconfigure((0, 1, 2, 3), weight=1)
        #self.frame_right.rowconfigure(7, weight=10)
        self.frame_right1.columnconfigure((0, 1), weight=1)
        self.frame_right1.columnconfigure(2, weight=0)

         # ============ create frame_info ============

        self.frame_info1 = customtkinter.CTkFrame(master=self.frame_right1)
        self.frame_info1.grid(row=0, column=0, columnspan=2, rowspan=4, pady=10, padx=10, sticky="nsew")

        # ============ frame_info ============

        # configure grid layout (1x1)
        self.frame_info1.rowconfigure((0, 1, 2), weight=1)
        self.frame_info1.columnconfigure((0, 1, 2), weight=1)

        self.button_p1 = customtkinter.CTkButton(master=self.frame_info1,
                                                text="Scrap eB",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.scrap_eBay)
        self.button_p1.grid(row=0, column=0, columnspan=1, pady=20, padx=20, sticky="we")

        self.button_p2 = customtkinter.CTkButton(master=self.frame_info1,
                                                text="Process-1",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.process_1)
        self.button_p2.grid(row=0, column=1, columnspan=1, pady=20, padx=20, sticky="we")

        self.button_p3 = customtkinter.CTkButton(master=self.frame_info1,
                                                text="Scrap LD",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.scrap_listdates)
        self.button_p3.grid(row=0, column=2, columnspan=1, pady=20, padx=20, sticky="we")

        self.button_p4 = customtkinter.CTkButton(master=self.frame_info1,
                                                text="Process-2",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.process_2)
        self.button_p4.grid(row=1, column=0, columnspan=1, pady=20, padx=20, sticky="we")

        self.button_p5 = customtkinter.CTkButton(master=self.frame_info1,
                                                text="Process-3",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.process_3)
        self.button_p5.grid(row=1, column=1, columnspan=1, pady=20, padx=20, sticky="we")

        self.button_p6 = customtkinter.CTkButton(master=self.frame_info1,
                                                text="Scrap A",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.scrap_amazon)
        self.button_p6.grid(row=1, column=2, columnspan=1, pady=20, padx=20, sticky="we")

        self.button_p7 = customtkinter.CTkButton(master=self.frame_info1,
                                                text="Process-4",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.process_4)
        self.button_p7.grid(row=2, column=0, columnspan=1, pady=20, padx=20, sticky="we")

        self.button_p8 = customtkinter.CTkButton(master=self.frame_info1,
                                                text="Results",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.create_popup_results_products)
        self.button_p8.grid(row=2, column=1, columnspan=1, pady=20, padx=20, sticky="we")

                # ============ frame_right ============

        self.label_1 = customtkinter.CTkLabel(master=self.frame_right1,
                                              text="HELP",
                                              text_font=("Roboto Medium", 30),
                                              fg_color='#E53238',)  # font name and size in px

        self.label_1.grid(row=0, column=2, pady=10, padx=10)

        self.label_2 = customtkinter.CTkLabel(master=self.frame_right1,
                                              text="Refrences: \n eB = eBay \n A = Amazon \n LD = Products Listing dates \n"+
                                              "while Scrap refered \n to Scraping\n"+
                                              "Note: In order to have \n a perfect results please \n follow the process's \n sequence as numbered.",
                                              text_font=("Roboto Medium", 10),
                                              justify=tkinter.LEFT )  # font name and size in px

        self.label_2.grid(row=1, column=2, pady=10, padx=10)

        self.entry = customtkinter.CTkEntry(master=self.frame_right1,
                                            width=120,
                                            placeholder_text="Search")
        self.entry.grid(row=8, column=0, columnspan=2, pady=20, padx=20, sticky="we")

        self.button_5 = customtkinter.CTkButton(master=self.frame_right1,
                                                text="BACK",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.button_event_right_frame_back)
        self.button_5.grid(row=8, column=2, columnspan=1, pady=20, padx=20, sticky="we")



    def button_event_right_frame_saleshistory(self):
        # ============ create right frame ============


        self.frame_right2 = customtkinter.CTkFrame(master=self)
        self.frame_right2.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right2.rowconfigure((0, 1, 2, 3), weight=1)
        #self.frame_right.rowconfigure(7, weight=10)
        self.frame_right2.columnconfigure((0, 1), weight=1)
        self.frame_right2.columnconfigure(2, weight=0)

         # ============ create frame_info ============

        self.frame_info2 = customtkinter.CTkFrame(master=self.frame_right2)
        self.frame_info2.grid(row=0, column=0, columnspan=2, rowspan=4, pady=10, padx=10, sticky="nsew")

       

        # ============ frame_info ============

        # configure grid layout (1x1)
        self.frame_info2.rowconfigure((0, 1, 2), weight=1)
        self.frame_info2.columnconfigure((0, 1, 2), weight=1)

        self.button_p6 = customtkinter.CTkButton(master=self.frame_info2,
                                                text="Process",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.process_6)
        self.button_p6.grid(row=0, column=1, columnspan=1, pady=20, padx=20, sticky="we")

        self.button_p7 = customtkinter.CTkButton(master=self.frame_info2,
                                                text="Scrap H",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.scrap_history_selenium)
        self.button_p7.grid(row=1, column=1, columnspan=1, pady=20, padx=20, sticky="we")

        self.button_p8 = customtkinter.CTkButton(master=self.frame_info2,
                                                text="Results",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.create_popup_results_sellinghistory)
        self.button_p8.grid(row=2, column=1, columnspan=1, pady=20, padx=20, sticky="we")

                # ============ frame_right ============

        self.label_1 = customtkinter.CTkLabel(master=self.frame_right2,
                                              text="HELP",
                                              text_font=("Roboto Medium", 30),
                                              fg_color='#E53238')  # font name and size in px

        self.label_1.grid(row=0, column=2, pady=10, padx=10)

        self.label_2 = customtkinter.CTkLabel(master=self.frame_right2,
                                              text="Refrences: \n H = History "+
                                              "while Scrap refered \n to Scraping\n"+
                                              "Note: \n 1 - In order to have \n a perfect results please \n follow the process's \n sequence as numbered.\n"+
                                              "2 - User have to put eBay's \n"+
                                              "USERNAMR & PASSWORD\n and fill CAPTCHA\n"+ "in automate chrome.\n"+
                                              "3 - User Must have \nchrome web browser.",
                                              text_font=("Roboto Medium", 10),
                                              justify=tkinter.LEFT )  # font name and size in px

        self.label_2.grid(row=1, column=2, pady=10, padx=10)

        self.entry = customtkinter.CTkEntry(master=self.frame_right2,
                                            width=120,
                                            placeholder_text="Search")
        self.entry.grid(row=8, column=0, columnspan=2, pady=20, padx=20, sticky="we")

        self.button_5 = customtkinter.CTkButton(master=self.frame_right2,
                                                text="BACK",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.button_event_right_frame_back)
        self.button_5.grid(row=8, column=2, columnspan=1, pady=20, padx=20, sticky="we")



    def button_event_right_frame_futureanalysis(self):
        # ============ create frame ============


        self.frame_right3 = customtkinter.CTkFrame(master=self)
        self.frame_right3.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right3.rowconfigure((0, 1, 2, 3), weight=1)
        #self.frame_right.rowconfigure(7, weight=10)
        self.frame_right3.columnconfigure((0, 1), weight=1)
        self.frame_right3.columnconfigure(2, weight=0)

         # ============ create frame_info ============

        self.frame_info3 = customtkinter.CTkFrame(master=self.frame_right3)
        self.frame_info3.grid(row=0, column=0, columnspan=2, rowspan=4, pady=10, padx=10, sticky="nsew")

        # ============ frame_info ============

        # configure grid layout (1x1)
        self.frame_info3.rowconfigure((0, 1, 2), weight=1)
        self.frame_info3.columnconfigure((0, 1, 2), weight=1)
        self.button_p1 = customtkinter.CTkButton(master=self.frame_info3,
                                                text="Process-1",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.process_7)
        self.button_p1.grid(row=0, column=0, columnspan=1, pady=20, padx=20, sticky="we")

        self.button_p2 = customtkinter.CTkButton(master=self.frame_info3,
                                                text="Process-2",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.process_8)
        self.button_p2.grid(row=0, column=1, columnspan=1, pady=20, padx=20, sticky="we")

        self.button_p3 = customtkinter.CTkButton(master=self.frame_info3,
                                                text="Process-3",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.process_9)
        self.button_p3.grid(row=0, column=2, columnspan=1, pady=20, padx=20, sticky="we")

        data_10 = read_csv('/home/champ/Downloads/MS PROJECT/Project/JADE/DB/ebay_products_final_products_with_amazon_prices_ML.csv')
        pidx = data_10['ITEM_Name']
        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_info3,
                                                        dynamic_resizing = False,
                                                        values=pidx,
                                                        command=self.machine_learning)
        self.optionmenu_1.grid(row=1, column=0, columnspan=1 ,pady=10, padx=20, sticky="w")




        self.button_p6 = customtkinter.CTkButton(master=self.frame_info3,
                                                text="Results",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.create_popup_results_futureprediction)
        self.button_p6.grid(row=1, column=2, columnspan=1, pady=20, padx=20, sticky="we")


               # ============ frame_right ============

        self.label_1 = customtkinter.CTkLabel(master=self.frame_right3,
                                              text="HELP",
                                              text_font=("Roboto Medium", 30),
                                              fg_color='#E53238')  # font name and size in px

        self.label_1.grid(row=0, column=2, pady=10, padx=10)

        self.label_2 = customtkinter.CTkLabel(master=self.frame_right3,
                                              text="In order to have \n a perfect results please \n follow the process's \n sequence as numbered.\n\n"+
                                              "Note: User have to\n press mouse right\n click until has selected\n product from options.",
                                              text_font=("Roboto Medium", 10),
                                              justify=tkinter.LEFT)  # font name and size in px

        self.label_2.grid(row=1, column=2, pady=10, padx=10)

        self.entry = customtkinter.CTkEntry(master=self.frame_right3,
                                            width=120,
                                            placeholder_text="Search")
        self.entry.grid(row=8, column=0, columnspan=2, pady=20, padx=20, sticky="we")

        self.button_5 = customtkinter.CTkButton(master=self.frame_right3,
                                                text="BACK",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.button_event_right_frame_back)
        self.button_5.grid(row=8, column=2, columnspan=1, pady=20, padx=20, sticky="we")
    
    def button_event_right_frame_back(self):

        # ============ create right frame ============

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        image = Image.open("/home/champ/Downloads/MS PROJECT/Project/JADE/DB/JADE LOGO@4x.png").resize((self.WIDTH, self.HEIGHT))
        self.bg_image = ImageTk.PhotoImage(image)

        self.image_label = tkinter.Label(master=self.frame_right, image=self.bg_image)
        self.image_label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.button_5 = customtkinter.CTkButton(master=self.frame_right,
                                                text="CONTINNUE",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.button_event_right_frame_productsdata)
        self.button_5.grid(row=8, column=2, columnspan=1, pady=20, padx=20, sticky="we")

#-----------------------EVENTS------------------------

    def scrap_eBay(self):
        class EbaySpider(scrapy.Spider):
            name = 'ebay'
            allowed_domains = ['ebay.co.uk']
            data = read_csv("/home/champ/Downloads/MS PROJECT/Project/JADE/DB/eBay_stores_data.csv")
            start_urls = data['Stores_Links'].tolist()

            custom_settings = {'DOWNLOAD_DELAY': 0.5}

            def parse(self, response):
                for link in (response.css('.s-item__info.clearfix > a::attr(href)').getall()):
                    yield response.follow(link, callback=self.productlinks)

                next_page = response.xpath('//a[contains(@class, "pagination__next")]/@href').get()
                if next_page:
                    next_page_link = response.urljoin(next_page)
                    yield scrapy.Request(url=next_page_link, callback=self.parse)

            def productlinks(self, response):
                
                yield {
                    'ITEM_Name': response.xpath('//h1//span//text()').get(),
                    'TIMES_Sold': response.xpath('//div[contains(@class, "quantity")]//a/text()').get(default= '0').replace('sold', ''),
                    'ITEM_Price_£': response.xpath('//span[@id="prcIsum"]/text()').get().replace('£', ''),
                    'ITEM_Revisions_Link' : response.xpath('//*[@id="vi-desc-maincntr"]/div[4]/div/span[2]/a/@href').get(default = '0'),
                    'ITEM_Sold_Link' : response.css('a.vi-txt-underline::attr(href)').get(default='N/A'),
                    'Seller_Name' : response.xpath('//*[@id="RightSummaryPanel"]/div[3]/div[1]/div/div[2]/div/div[1]/div/a[1]/span/text()').get(),
                    'Seller_Reviews' : response.xpath('//*[@id="RightSummaryPanel"]/div[3]/div[1]/div/div[2]/div/div[1]/div/a[2]/span/text()').get() + 'Reviews',
                    'Seller_Feedback_Link' : response.xpath('//*[@id="RightSummaryPanel"]/div[3]/div[1]/div/div[2]/div/div[1]/div/a[2]/@href').get()

                }


        process = CrawlerProcess(settings={
            'FEED_URI': '/home/champ/Downloads/MS PROJECT/Project/JADE/DB/eBay_products_data_initial.csv',
            'FEED_FORMAT': 'csv',
            'ROBOTSTXT_OBEY' : False ,
            'DOWNLOADER_MIDDLEWARES' : {
            'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
            'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
        }
        })
        process.crawl(EbaySpider)
        process.start() 

        window = customtkinter.CTk()
        #self.title("JADE")
        window.geometry("480x120")
        window.title("RESULTS")

        # create label on customtkinter.CTkToplevel(self) window
        #img1 = img1.resize((50, 50), Image.ANTIALIAS)
        label = customtkinter.CTkLabel(window, text="Process Complete")
        label.pack(side="top", fill="both", expand=True, padx=40, pady=40)



    def process_1(self):
        #Preprocess-1 (removind sold < 10)
        data = read_csv("/home/champ/Downloads/MS PROJECT/Project/JADE/DB/eBay_products_data_initial.csv")
        data['TIMES_Sold'] = data['TIMES_Sold'].str.strip().replace('\D', '0', regex=True).astype(int)
        data['ITEM_Price_£'] = data['ITEM_Price_£'].str.replace('[^\d.]+', '', regex=True).astype(float)
        data = data.loc[data["TIMES_Sold"] > 10]  
        #print(df.dtypes)
        data.to_csv('/home/champ/Downloads/MS PROJECT/Project/JADE/DB/ebay_products_data_initial_cleaned.csv', index=False)

        window = customtkinter.CTk()
        #self.title("JADE")
        window.geometry("480x120")
        window.title("RESULTS")

        # create label on customtkinter.CTkToplevel(self) window
        #img1 = img1.resize((50, 50), Image.ANTIALIAS)
        label = customtkinter.CTkLabel(window, text="Process Complete")
        label.pack(side="top", fill="both", expand=True, padx=40, pady=40)

    def scrap_listdates(self):
        class EbayProductsListedSpider(scrapy.Spider):
            name = 'ebay_products_listed'
            allowed_domains = ['ebay.co.uk']
            data = read_csv("/home/champ/Downloads/MS PROJECT/Project/JADE/DB/ebay_products_data_initial_cleaned.csv")

            start_urls = data['ITEM_Revisions_Link'].tolist()

            def parse(self, response):
                    yield{
                    'ITEM_Listed_Dtae': response.xpath('//*[@id="s0-0-17-5-mainRiver-layout"]/div/div/div/section/table/tr[2]/td[1]/div/span/span/text()').get(),
                    'ITEM_Link': response.xpath('//*[@id="s0-0-17-5-mainRiver-layout"]/div/div/div/div[1]/a/@href').get()
                    }

        process = CrawlerProcess(settings={
            'FEED_URI': '/home/champ/Downloads/MS PROJECT/Project/JADE/DB/ebay_products_data_initial_cleaned_with_dates.csv',
            'FEED_FORMAT': 'csv',
            'ROBOTSTXT_OBEY' : False ,
            'DOWNLOADER_MIDDLEWARES' : {
            'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
            'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
        }
        })
        process.crawl(EbayProductsListedSpider)
        process.start()

        window = customtkinter.CTk()
        #self.title("JADE")
        window.geometry("480x120")
        window.title("RESULTS")

        # create label on customtkinter.CTkToplevel(self) window
        #img1 = img1.resize((50, 50), Image.ANTIALIAS)
        label = customtkinter.CTkLabel(window, text="Process Complete")
        label.pack(side="top", fill="both", expand=True, padx=40, pady=40)   

    def process_2(self):
        #Preprocess-2 (taking dates data and merging accordingly)
        #Preprocess-3 (Droping the unused links)
        data_1 = read_csv("/home/champ/Downloads/MS PROJECT/Project/JADE/DB/ebay_products_data_initial_cleaned_with_dates.csv")
        Listed_Dates = data_1['ITEM_Listed_Dtae'].tolist()
        Items_Links = data_1['ITEM_Link']
        data_2 = read_csv("/home/champ/Downloads/MS PROJECT/Project/JADE/DB/ebay_products_data_initial_cleaned.csv")
        data_2['LISTED_Dates'] = Listed_Dates
        data_2['ITEM_Link'] = Items_Links
        data_2 = data_2.drop(labels="ITEM_Revisions_Link", axis=1)
        data_2.to_csv('/home/champ/Downloads/MS PROJECT/Project/JADE/DB/ebay_products_data_cleaned_with_dates_final.csv', index=False)

        window = customtkinter.CTk()
        #self.title("JADE")
        window.geometry("480x120")
        window.title("RESULTS")

        # create label on customtkinter.CTkToplevel(self) window
        #img1 = img1.resize((50, 50), Image.ANTIALIAS)
        label = customtkinter.CTkLabel(window, text="Process Complete")
        label.pack(side="top", fill="both", expand=True, padx=40, pady=40)

    def process_3(self):
        #Preprocess-4 (Converting to dates)
        #Preprocess-5 (includind current dates)
        #Preprocess-6 (Calculating difference Months and droping products with difference greater then 5 months)
        data_3 = read_csv("/home/champ/Downloads/MS PROJECT/Project/JADE/DB/ebay_products_data_cleaned_with_dates_final.csv")
        data_3['LISTED_Dates'] = pandas.to_datetime(data_3['LISTED_Dates'])
        CurrentDate = date.today()
        #print(CurrentDate)
        for i in data_3['LISTED_Dates']:
            data_3['Current_date'] = CurrentDate
        data_3['Current_date'] = pandas.to_datetime(data_3['Current_date'])
        data_3[['LISTED_Dates','Current_date']] = data_3[['LISTED_Dates','Current_date']].apply(pandas.to_datetime)
        df = pandas.DataFrame({'dates1': np.array(
        data_3['LISTED_Dates'].tolist()),
                        'dates2': np.array(data_3['Current_date'].tolist()
                            )})
        df['Difference_months'] = ((df.dates2 - df.dates1)/np.timedelta64(1, 'M'))
        df['Difference_months'] = df['Difference_months'].astype(int)
        data_3['Difference_months'] = df['Difference_months']
        data_3 = data_3.loc[data_3["Difference_months"] < 5]
        #print(data)
        data_3.to_csv('/home/champ/Downloads/MS PROJECT/Project/JADE/DB/ebay_products_final_products.csv', index=False)

        window = customtkinter.CTk()
        #self.title("JADE")
        window.geometry("480x120")
        window.title("RESULTS")

        # create label on customtkinter.CTkToplevel(self) window
        #img1 = img1.resize((50, 50), Image.ANTIALIAS)
        label = customtkinter.CTkLabel(window, text="Process Complete")
        label.pack(side="top", fill="both", expand=True, padx=40, pady=40)

    def scrap_amazon(self):
        data = read_csv("/home/champ/Downloads/MS PROJECT/Project/JADE/DB/ebay_products_final_products.csv")

        queries = data['ITEM_Name'].tolist()
        #queries = ['Elemis Pro-Collagen Cleansing Balm, 3-in-1 Deep Cleansing Milk to Nourish & with']

        class AmazonProductsSpider(scrapy.Spider):
            name = 'amazon_products'
            allowed_domains = ['amazon.co.uk']
            start_urls = ['http://amazon.co.uk/']

            def start_requests(self):
                for query in queries:
                    url = 'https://www.amazon.co.uk/s?' + urlencode({'k': query})
                    yield scrapy.Request(url, callback=self.parse_keyword_response)
                    #yield SplashRequest(url, callback=self.parse_keyword_response)

            def parse_keyword_response(self, response):
                products = response.xpath('//*[@data-asin]')
                for product in products:
                    asin = product.xpath('@data-asin').extract_first()
                    product_url = f"https://www.amazon.co.uk/dp/{asin}"
                    yield scrapy.Request(url=product_url, callback=self.parse_product_page, meta={'asin': asin})
                next_page = response.xpath('//li[@class="a-last"]/a/@href').extract_first()
                if next_page:
                    url = urljoin("https://www.amazon.co.uk",next_page)
                    yield scrapy.Request(url, callback=self.parse_keyword_response)
                    
            def parse_product_page(self, response):
                asin = response.meta['asin']
                title = response.xpath('//*[@id="productTitle"]/text()').extract_first()
                image = re.search('"large":"(.*?)"',response.text).groups()[0]
                rating = response.xpath('//*[@id="acrPopover"]/@title').extract_first()
                number_of_reviews = response.xpath('//*[@id="acrCustomerReviewText"]/text()').extract_first()
                price = response.xpath('//*[@id="sns-base-price"]/text()').extract_first()
                #if not price:
                #    price = response.xpath('//*[@data-asin-price]/@data-asin-price').extract_first() or \
                #            response.xpath('//*[@id="price_inside_buybox"]/text()').extract_first()
                temp = response.xpath('//*[@id="twister"]')
                sizes = []
                colors = []
                if temp:
                    s = re.search('"variationValues" : ({.*})', response.text).groups()[0]
                    json_acceptable = s.replace("'", "\"")
                    di = json.loads(json_acceptable)
                    sizes = di.get('size_name', [])
                    colors = di.get('color_name', [])
                bullet_points = response.xpath('//*[@id="feature-bullets"]//li/span/text()').extract()
                seller_rank = response.xpath('//*[text()="Amazon Best Sellers Rank:"]/parent::*//text()[not(parent::style)]').extract()
                yield {'asin': asin, 'Title': title, 'MainImage': image, 'Rating': rating, 'NumberOfReviews': number_of_reviews,
                    'Price': price, 'AvailableSizes': sizes, 'AvailableColors': colors, 'BulletPoints': bullet_points,
                    'SellerRank': seller_rank}


        process = CrawlerProcess(settings={
            'FEED_URI': '/home/champ/Downloads/MS PROJECT/Project/JADE/DB/Amazon_products_data.csv',
            'FEED_FORMAT': 'csv',
            'ROBOTSTXT_OBEY' : True ,
            'DOWNLOADER_MIDDLEWARES' : {
            'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
            'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
        }
        })
        process.crawl(AmazonProductsSpider)
        process.start()

        window = customtkinter.CTk()
        #self.title("JADE")
        window.geometry("480x120")
        window.title("RESULTS")

        # create label on customtkinter.CTkToplevel(self) window
        #img1 = img1.resize((50, 50), Image.ANTIALIAS)
        label = customtkinter.CTkLabel(window, text="Process Complete")
        label.pack(side="top", fill="both", expand=True, padx=40, pady=40)

    def process_4(self):
        data_4 = read_csv("/home/champ/Downloads/MS PROJECT/Project/JADE/DB/ebay_products_final_products.csv")
        product_links = data_4['ITEM_Link']
        ebay_price = data_4['ITEM_Price_£']
        print(ebay_price)
        print(data_4.dtypes)
        amazon_price = []
        amount = 2.13
        for price in ebay_price:
            amazon_price = ebay_price - amount
        data_4['amazon_price_approx'] = amazon_price
        data_4.to_csv('/home/champ/Downloads/MS PROJECT/Project/JADE/DB/ebay_products_final_products_with_amazon_prices.csv', index=False)
        data_4 = data_4.drop(labels="ITEM_Sold_Link", axis=1)
        data_4 = data_4.drop(labels="Seller_Name", axis=1)
        data_4 = data_4.drop(labels="Seller_Reviews", axis=1)
        data_4 = data_4.drop(labels="Seller_Feedback_Link", axis=1)
        data_4 = data_4.drop(labels="ITEM_Link", axis=1)
        data_4['Links'] = product_links
        data_4.to_csv('/home/champ/Downloads/MS PROJECT/Project/JADE/FINAL_PRODUCTS.csv', index=False)

        window = customtkinter.CTk()
        #self.title("JADE")
        window.geometry("480x120")
        window.title("RESULTS")

        # create label on customtkinter.CTkToplevel(self) window
        #img1 = img1.resize((50, 50), Image.ANTIALIAS)
        label = customtkinter.CTkLabel(window, text="Process Complete")
        label.pack(side="top", fill="both", expand=True, padx=40, pady=40)

    def process_6(self):
        data_5 = read_csv('/home/champ/Downloads/MS PROJECT/Project/JADE/DB/ebay_products_final_products_with_amazon_prices.csv')
        data_5["ITEM_Name"] = data_5["ITEM_Name"].apply(lambda x: x.replace("/", "-"))
        #data_5.to_csv('/home/champ/Downloads/MS PROJECT/Project/JADE/DB/ebay_products_final_products_with_amazon_prices_ML.csv', index=False)
        Pnames = data_5['ITEM_Name']
        product_idx = []
        product_id = []
        for nm in range(len(Pnames)):
            product_idx = "Product-" + str(nm)
            product_id.append(product_idx)
        data_5['product_idx'] = product_id
        data_5.to_csv('/home/champ/Downloads/MS PROJECT/Project/JADE/DB/ebay_products_final_products_with_amazon_prices_ML.csv' , index=True)

        window = customtkinter.CTk()
        #self.title("JADE")
        window.geometry("480x120")
        window.title("RESULTS")

        # create label on customtkinter.CTkToplevel(self) window
        #img1 = img1.resize((50, 50), Image.ANTIALIAS)
        label = customtkinter.CTkLabel(window, text="Process Complete")
        label.pack(side="top", fill="both", expand=True, padx=40, pady=40)



    def scrap_history_selenium(self):
        #API_KEY = '5b1d2d1fc53a08fec8460963bdef8c9c'

        url_link="https://www.ebay.co.uk/signin/s"

        #start_urls=['http://api.scraperapi.com/?api_key='+ API_KEY + '&url=' + url_link + '&render=true']
        driver = webdriver.Chrome('/home/champ/Downloads/MS PROJECT/Project/JADE/DB/chromedriver_linux64/chromedriver')

        #driver.get('http://api.scraperapi.com/?api_key='+ API_KEY + '&url=' + url_link + '&render=true')
        driver.get('https://www.ebay.co.uk/signin/s')

        driver.implicitly_wait(10)

        signin = driver.find_elements_by_xpath('//*[@id="gh-ug"]/a')



        login = driver.find_element_by_xpath('//*[@id="userid"]').send_keys('champ.husnain@gmail.com')

        submit = driver.find_element_by_xpath('//*[@id="signin-continue-btn"]').click()

        driver.implicitly_wait(20)

        password = driver.find_element_by_xpath('//*[@id="pass"]').send_keys('s5YfG3kRh$9WakJm123')

        submit1 = driver.find_element_by_xpath('//*[@id="sgnBt"]').click()

        driver.implicitly_wait(40)
        time.sleep(100)

        data = read_csv("/home/champ/Downloads/MS PROJECT/Project/JADE/DB/ebay_products_final_products_with_amazon_prices_ML.csv")

        product_names = data['ITEM_Name'].tolist()
        urls = data['ITEM_Sold_Link'].tolist()
        print(product_names) 

        for (url , name) in zip(urls , product_names):
            driver.get(url)


            
            num_rows = len (driver.find_elements_by_xpath('//*[@id="mainContent"]/div[1]/div[2]/table/tbody/tr/td'))
            print("Rows in table are " + repr(num_rows))

            num_cols = len (driver.find_elements_by_xpath('//*[@id="mainContent"]/div[1]/div[2]/table/tbody/tr[2]/td'))
            print("Columns in table are " + repr(num_cols))

            before_XPath = '//*[@id="mainContent"]/div[1]/div[2]/table/tbody/tr['
            aftertd_XPath = ']/td['
            aftertr_XPath = ']'

            before_XPath = '//*[@id="mainContent"]/div[1]/div[2]/table/tbody/tr['
            aftertd_XPath_1 = "]/td[1]"
            aftertd_XPath_2 = ']/td[2]'
            aftertd_XPath_3 = ']/td[3]'
            aftertd_XPath_4 = ']/td[4]'

            
            rows = len(driver.find_elements_by_xpath('//*[@id="mainContent"]/div[1]/div[2]/table/tbody/tr'))
                    # print (rows)
            columns = len(driver.find_elements_by_xpath('//*[@id="mainContent"]/div[1]/div[2]/table/tbody/tr[1]/td'))
                    # print(columns)
                    
                    # print("Company"+"               "+"Contact"+"               "+"Country")
            cell_text1 = [] 
            cell_text2 = [] 
            cell_text3 = [] 
            cell_text4 = []
            i=0 
            print("Data present in Rows, Col - 1")
            print()
            for t_row in range(2, (rows + 1)):
                FinalXPath = before_XPath + str(t_row) + aftertd_XPath_1
                cell_text = driver.find_element_by_xpath(FinalXPath).text
                #print(cell_text)
                cell_text1.append(cell_text)

            print(cell_text1)
            
            print()    
            print("Data present in Rows, Col - 2")
            print()
            for t_row in range(2, (rows + 1)):
                FinalXPath = before_XPath + str(t_row) + aftertd_XPath_2
                cell_text = driver.find_element_by_xpath(FinalXPath).text
                #print(cell_text)
                cell_text2.append(cell_text)

            print(cell_text2)
                        
            print()
            print("Data present in Rows, Col - 3")
            print()
            for t_row in range(2, (rows + 1)):
                FinalXPath = before_XPath + str(t_row) + aftertd_XPath_3
                cell_text = driver.find_element_by_xpath(FinalXPath).text
                #print(cell_text) 
                cell_text3.append(cell_text)

            print(cell_text3)

            print()
            print("Data present in Rows, Col - 4")
            print()
            for t_row in range(2, (rows + 1)):
                FinalXPath = before_XPath + str(t_row) + aftertd_XPath_4
                cell_text = driver.find_element_by_xpath(FinalXPath).text
                #print(cell_text) 
                cell_text4.append(cell_text)

            print(cell_text4)


            raw_data = {'User ID': cell_text1,
                            'Buy it now price': cell_text2,
                            'Quantity': cell_text3,
                            'Date_of_purchase': cell_text4}

            df = pd.DataFrame(raw_data, columns = ['User ID', 'Buy it now price', 'Quantity',
                                                    'Date_of_purchase'])
            print(df)

            
            df.to_csv('/home/champ/Downloads/MS PROJECT/Project/JADE/Products_sold_history/' + name + '.csv', index=False) 
            print(name)

        window = customtkinter.CTk()
        #self.title("JADE")
        window.geometry("480x120")
        window.title("RESULTS")

        # create label on customtkinter.CTkToplevel(self) window
        #img1 = img1.resize((50, 50), Image.ANTIALIAS)
        label = customtkinter.CTkLabel(window, text="Process Complete")
        label.pack(side="top", fill="both", expand=True, padx=40, pady=40)



    def create_popup_results_products(self):
        window = customtkinter.CTk()
        #self.title("JADE")
        window.geometry("780x120")
        window.title("RESULTS")

        # create label on customtkinter.CTkToplevel(self) window
        #img1 = img1.resize((50, 50), Image.ANTIALIAS)
        label = customtkinter.CTkLabel(window, text="You can see the results in the file name FINAL_PRODUCTS.csv in parent directory of the application.")
        label.pack(side="top", fill="both", expand=True, padx=40, pady=40)

    def create_popup_results_sellinghistory(self):
        window = customtkinter.CTk()
        #self.title("JADE")
        window.geometry("780x120")
        window.title("RESULTS")

        # create label on customtkinter.CTkToplevel(self) window
        #img1 = img1.resize((50, 50), Image.ANTIALIAS)
        label = customtkinter.CTkLabel(window, text="You can see the results in the CSVs in folder Products_sold_history in parent directory of the application.")
        label.pack(side="top", fill="both", expand=True, padx=40, pady=40)
    
    def create_popup_results_futureprediction(self):
        window = customtkinter.CTk()
        #self.title("JADE")
        window.geometry("780x120")
        window.title("RESULTS")

        # create label on customtkinter.CTkToplevel(self) window
        #img1 = img1.resize((50, 50), Image.ANTIALIAS)
        label = customtkinter.CTkLabel(window, text="You can see the results in the PRODUCTNAME.png in folder Products_Predictions in parent directory of the application.")
        label.pack(side="top", fill="both", expand=True, padx=40, pady=40)

    def process_7(self):

       

        all_files = listdir("/home/champ/Downloads/MS PROJECT/Project/JADE/Products_sold_history")   
        all_files_2 = glob.glob("/home/champ/Downloads/MS PROJECT/Project/JADE/Products_sold_history/*.csv") 
        csv_files = list(filter(lambda f: f.endswith('.csv'), all_files))
        for (filename , name) in zip (all_files_2 , csv_files):
            #df = pd.read_csv(filename, index_col=None, header=0)
            df = read_csv(filename)
            df = df.drop(labels="User ID", axis=1)
            df = df.drop(labels="Buy it now price", axis=1)
            df.to_csv("/home/champ/Downloads/MS PROJECT/Project/JADE/DB/ML_DATASETS/" + name , index=False)

        '''
        data_6 = read_csv('/home/champ/Downloads/MS PROJECT/Project/JADE/DB/ebay_products_final_products_with_amazon_prices_ML.csv')
        all_files = glob.glob("/home/champ/Downloads/MS PROJECT/Project/JADE/Products_sold_history/*.csv")
        item_names = data_6['ITEM_Name'].tolist()
        for (filename , name) in zip (all_files , item_names):
            #df = pd.read_csv(filename, index_col=None, header=0)
            df = read_csv(filename)
            df = df.drop(labels="User ID", axis=1)
            df = df.drop(labels="Buy it now price", axis=1)
            df.to_csv("/home/champ/Downloads/MS PROJECT/Project/JADE/DB/ML_DATASETS/" + name + ".csv" , index=False)'''

        window = customtkinter.CTk()
        #self.title("JADE")
        window.geometry("480x120")
        window.title("RESULTS")

        # create label on customtkinter.CTkToplevel(self) window
        #img1 = img1.resize((50, 50), Image.ANTIALIAS)
        label = customtkinter.CTkLabel(window, text="Process Complete")
        label.pack(side="top", fill="both", expand=True, padx=40, pady=40)
    
    def process_8(self):
        all_files = listdir("/home/champ/Downloads/MS PROJECT/Project/JADE/DB/ML_DATASETS")   
        all_files_2 = glob.glob("/home/champ/Downloads/MS PROJECT/Project/JADE/DB/ML_DATASETS/*.csv") 
        csv_files = list(filter(lambda f: f.endswith('.csv'), all_files))
        for (filename , name) in zip (all_files_2 , csv_files):
            df = read_csv(filename)
            df = df.assign(Date_of_purchase = pandas.to_datetime(
            df['Date_of_purchase'].astype(str).str.extract(r'(.*)(at)')[0].str.strip())
            ).groupby('Date_of_purchase')['Quantity'].sum().reset_index()
            df.to_csv("/home/champ/Downloads/MS PROJECT/Project/JADE/DB/ML_DATASETS_FINAL/" + name , index=False)

        window = customtkinter.CTk()
        #self.title("JADE")
        window.geometry("480x120")
        window.title("RESULTS")

        # create label on customtkinter.CTkToplevel(self) window
        #img1 = img1.resize((50, 50), Image.ANTIALIAS)
        label = customtkinter.CTkLabel(window, text="Process Complete")
        label.pack(side="top", fill="both", expand=True, padx=40, pady=40)

    def process_9(self):
        all_files = listdir("/home/champ/Downloads/MS PROJECT/Project/JADE/DB/ML_DATASETS_FINAL")   
        all_files_2 = glob.glob("/home/champ/Downloads/MS PROJECT/Project/JADE/DB/ML_DATASETS_FINAL/*.csv") 
        csv_files = list(filter(lambda f: f.endswith('.csv'), all_files))
        for (filename , name) in zip (all_files_2 , csv_files):
            #path = '/home/champ/Downloads/MS PROJECT/Project/JADE/Scrapers/products_sold_history_data_final.csv'
            df = read_csv(filename, header=0)
            #df = df.drop(labels="Unnamed: 0", axis=1)
            # summarize shape
            #print(df.shape)
            # show first few rows
            #print(df.head())
            #df.plot()
            #pyplot.show()
            #print(pyplot.show())
            df.columns = ['Date_of_purchase', 'Quantity']
            df['ds'] = df['Date_of_purchase']
            df['y'] = df['Quantity']
            df = df.drop(labels="Date_of_purchase", axis=1)
            df = df.drop(labels="Quantity", axis=1)
            df.to_csv("/home/champ/Downloads/MS PROJECT/Project/JADE/DB/ML_DATASETS_TRAINING/" + name  , index=False)

        window = customtkinter.CTk()
        #self.title("JADE")
        window.geometry("480x120")
        window.title("RESULTS")

        # create label on customtkinter.CTkToplevel(self) window
        #img1 = img1.resize((50, 50), Image.ANTIALIAS)
        label = customtkinter.CTkLabel(window, text="Process Complete")
        label.pack(side="top", fill="both", expand=True, padx=40, pady=40)
            
            
    def machine_learning(self , selectedproduct):

        path = "/home/champ/Downloads/MS PROJECT/Project/JADE/DB/ML_DATASETS_TRAINING/" + selectedproduct + ".csv"
        df = read_csv(path, header=0)

        p = Prophet(interval_width=0.92, daily_seasonality=True)

        model = p.fit(df)

        future = p.make_future_dataframe(periods= 1, freq='D')
        print(future.tail())

        forecast_prediction = p.predict(future)
        print(forecast_prediction.tail())

        plot1 = p.plot(forecast_prediction)

        #plot1.show()
        plot2 = p.plot_components(forecast_prediction)

        #model.plot(forecast_prediction)
        pyplot.show()

        plot2.savefig('/home/champ/Downloads/MS PROJECT/Project/JADE/Products_predictions/' + selectedproduct + '.png')

        

    def button_event_info(self):

        # ============ create right frame ============

        self.frame_right_about = customtkinter.CTkFrame(master=self)
        self.frame_right_about.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
                
        # configure grid layout (3x7)
        self.frame_right_about.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right_about.rowconfigure(7, weight=10)
        self.frame_right_about.columnconfigure((0, 1), weight=1)
        self.frame_right_about.columnconfigure(2, weight=0)

        self.label_info= customtkinter.CTkLabel(master=self.frame_right_about,
                                                   text="ABOUT JADE" ,
                                                   height=50,  # <- custom tuple-color
                                                   text_font=("Roboto Large", 14),
                                                   justify=tkinter.CENTER)
        self.label_info.grid(column=0, row=1, sticky="nwe", padx=15, pady=15)

        self.label_info1= customtkinter.CTkLabel(master=self.frame_right_about,
                                                   text="JADE (A Product Hunting Tool For eBay) will allow the\n"+
                                                     "sellers to find the product without the hustle of managing\n"+
                                                     "virtual assistants and paying a lot of profit shares to the\n"+
                                                     "virtual assistants. JADE system will going to be a blend of\n"+
                                                     "modern day technology like Machine Learning and Natural Language\n"+
                                                     "Processing that can help users to find the products that will boost\n"+
                                                     "sales and the reliability of the store.  Because of this innovative\n" +
                                                     "way sellers will not only be saving money but it will also help\n" +
                                                     "them to save a lot of time that they were investing while finding\n"+
                                                     "for the product and virtual assistants. " +
                                                     "\n\n\n\n\n for more info please visit dynamicxolutions.com" ,
                                                   height=100,  # <- custom tuple-color
                                                   text_font=("Roboto Medium", 14),
                                                   justify=tkinter.CENTER)
        self.label_info1.grid(column=0, row=2, sticky="nwe", padx=15, pady=15)

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()

if __name__ == "__main__":
        app = App()
        app.mainloop()