#作业二：
#（1）使用 Scrapy 框架和 XPath 抓取猫眼电影的前 10 个电影名称、电影类型和上映时间，
#（2）并以 UTF-8 字符集保存到 csv 格式的文件中。
# 猫眼电影网址： https://maoyan.com/films?showType=3
# 要求：必须使用 Scrapy 框架及其自带的 item pipeline、选择器功能，不允许使用 bs4 进行页面内容的筛选。

# -*- coding: utf-8 -*-

import scrapy
from scrapy.selector import Selector
from spiders.items import SpidersItems

class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

 
    def start_requests(self):  
        url = "https://maoyan.com/films?showType=3"
        yield scrapy.Request(url=url, callback=self.parse)

    # 解析函数，用XPATH
    def parse(self, response):
        item = SpidersItems()
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        i=0

        for movie in movies:
            if i < 10:
                break
            movie_name = movie.xpath('./div[@class="movie-hover-title"][1]/span/text()').extract_first().strip()
            movie_type = movie.xpath('./div[@class="movie-hover-title"][2]/text()')[1].extract().strip()
            movie_date = movie.xpath('./div[@class="movie-hover-title movie-hover-brief"]/text()')[1].extract().strip()

            item['movie_name'] = movie_name
            item['movie_type'] = movie_type
            item['movie_date'] = movie_date

            i += 1
            yield item
