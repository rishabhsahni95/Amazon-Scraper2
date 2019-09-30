# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonCrawlerItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    page_number=2
    api='http://api.scraperapi.com/?api_key=822da7f5e247570657b28227f6d782f1&url='
    link = 'https://www.amazon.com/s/ref=lp_3_nr_p_n_feature_browse-b_0?fst=as%3Aoff&rh=n%3A283155%2Cn%3A%211000%2Cn%3A3%2Cp_n_feature_browse-bin%3A2656022011&bbn=3&ie=UTF8&qid=1569085556&rnid=618072011' #URL to be scraped
    start_urls=[api+link]


    def parse(self, response):
        items = AmazonCrawlerItem()

        products = response.css('div.sg-col-4-of-12.sg-col-8-of-16.sg-col-16-of-24.sg-col-12-of-20.sg-col-24-of-32.sg-col.sg-col-28-of-36.sg-col-20-of-28') # To select div that holds details of individual products.

        for product in products:

                book_name=product.css('span.a-size-medium.a-color-base.a-text-normal::text').extract_first() #BOOK_NAME

                author=product.css('.a-color-secondary .a-size-base+ .a-size-base::text').extract_first() #AUTHOR_NAME

                out_of_5_stars=product.css('span.a-icon-alt::text').extract_first() #REVIEW (OUT OF 5 STARS)

                no_of_reviews=product.css('.a-size-small .a-size-base::text').extract_first() #NO. OF REVIEWS

                price_whole=product.css('span.a-price-whole::text').extract_first()

                price_cents=product.css('span.a-price-fraction::text').extract_first() #CENTS_PRICE_(CENTS)

                items['book_name'] = book_name
                items['author'] = author
                items['out_of_5_stars']=out_of_5_stars
                items['price']= price_whole+'.'+price_cents
                items['no_of_reviews']=no_of_reviews

                yield items

        #next_page = 'https://www.amazon.com/s?i=stripbooks&bbn=3&rh=n%3A283155%2Cn%3A1000%2Cn%3A3%2Cp_n_feature_browse-bin%3A2656022011&dc&page='+str(AmazonSpiderSpider.page_number)+'&fst=as%3Aoff&qid=1569258613&rnid=618072011&ref=sr_pg_2' #FOR PAGINATION
        #if AmazonSpiderSpider.page_number <75:
            #AmazonSpiderSpider.page_number+=1
            #yield scrapy.Request(url = AmazonSpiderSpider.api+next_page, callback=self.parse)
