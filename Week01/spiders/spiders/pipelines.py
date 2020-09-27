# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd

class SpidersPipeline:
    def process_item(self, item, spider):
        result = {
            '电影名称':[item['movie_name']],
            '电影类型':[item['movie_type']],
            '上映日期':[item['movie_date']],
        }
        result_df = pd.DataFrame(data = result)
        result_df.to_csv("./maoyan_spider_result.csv", index=False)
        return item
