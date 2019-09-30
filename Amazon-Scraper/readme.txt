This is a crawler to scrap following URL

URL = 'https://www.amazon.com/s/ref=lp_3_nr_p_n_feature_browse-b_0?fst=as%3Aoff&rh=n%3A283155%2Cn%3A%211000%2Cn%3A3%2Cp_n_feature_browse-bin%3A2656022011&bbn=3&ie=UTF8&qid=1569085556&rnid=618072011'

DATA FIELDS:
1 - Book Name.
2- Author Name.
3. Price
4 - Reviews (out of 5 stars)
5- No. of Reviews

To bypass imposed restrictions such as Captcha and IP tracing, a proxy service from 'scraperapi.com' has been used with http request

virtualenv_name - venv (scrapy is installed inside it)
project_name - amazon_crawler
spider name - amazon_spider

I have attached the output file (.csv format) along with the project.