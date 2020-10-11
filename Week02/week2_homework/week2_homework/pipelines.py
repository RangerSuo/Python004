# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from itemadapter import ItemAdapter
import pymysql

class SpidersPipeline:
    def open_spider(self,spider):
        self.conn = pymysql.connect(host='localhost',
                               port=3306,
                               user='root',
                               password='',
                               database='test',
                               charset='utf8mb4'
                               )
        # 获得cursor游标对象
        self.con1 = self.conn.cursor()
    def process_item(self, item, spider):
        movie_name = item['movie_name']
        movie_type = item['movie_type']
        movie_date = item['movie_date']
        print(movie_name)
        print(movie_type)
        print(movie_date)
        # 操作的行数
        count = self.con1.execute('insert into movies values(%s,%s,%s);',
        (movie_name, movie_type, movie_date))
        count = self.con1.execute('commit;')

        return item
    def close_spider(self,spider):
        self.con1.close()
        self.conn.close()
