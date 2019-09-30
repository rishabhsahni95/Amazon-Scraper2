# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

#Flow of things here:

#EVERY TIME WE YIELD AND ITEM > INIT WILL BE CALLED > ITEM WILL GO TO PROCESS_ITEM METHOD > THEN IT WILL SEND THE ITEM TO STORE_DB METHOD > WHICH EVENTUALLY STORE OUR ITEMS INSIDE THE DATABASE
import sqlite3


class AmazonCrawlerPipeline(object):

    def __init__(self): #every time the class instance is created - this init function is called upon first of all. (refer to classes and objecrs tutorial for more)
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("myquotes.db") #Database created
        self.curr = self.conn.cursor() #cursor created

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS quotes_tb""")
        self.curr.execute("""create table quotes_tb(
                        book_name text,
                        author text,
                        out_of_5_stars float,
                        price float,
                        no_of_reviews text
                        )""")



    def process_item(self, item, spider): #this item variable inside the bracket contains the items scrapped by the spider
        item['author']=item['author'].replace('\n','').strip()
        item['no_of_reviews']=str(item['no_of_reviews'])
        item['out_of_5_stars'] = item['out_of_5_stars'].replace('out of 5 stars','').strip()
        return item
        self.store_db(item)

    def store_db(self,item):
        self.curr.execute("""insert into quotes_tb values (?,?,?)"""(
                item['book_name'],
                item['author'],
                item['out_of_5_stars'],
                item['price'],
                item['no_of_reviews']))
        self.conn.commit()


#Flow of things :

#Every time we hit yield items, items are scraped > stored inside the cotainers we made > and those items are then passed through the above function
