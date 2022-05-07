import scrapy

class GMarket2Item(scrapy.Item):
    Sort = scrapy.Field()
    Name = scrapy.Field()
    Price = scrapy.Field()
    URL = scrapy.Field()
