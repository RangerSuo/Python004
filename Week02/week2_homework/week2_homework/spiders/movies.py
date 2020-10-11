# -*- coding: utf-8 -*-

import scrapy
from scrapy.selector import Selector
from week2_homework.items import Week2HomeworkItem

class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

 
    def start_requests(self):  
        url = "https://maoyan.com/films?showType=3"
        yield scrapy.Request(url=url, callback=self.parse)

    # 解析函数，用XPATH
    def parse(self, response):
        
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        
        for movie in movies[:10]:
            item = Week2HomeworkItem()
            
            movie_name = movie.xpath('./div[@class="movie-hover-title"][1]/span/text()').extract_first().strip()
            movie_type = movie.xpath('./div[@class="movie-hover-title"][2]/text()')[1].extract().strip()
            movie_date = movie.xpath('./div[@class="movie-hover-title movie-hover-brief"]/text()')[1].extract().strip()

            item['movie_name'] = movie_name
            item['movie_type'] = movie_type
            item['movie_date'] = movie_date


            yield item
