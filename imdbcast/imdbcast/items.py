import scrapy


class ImdbcastItem(scrapy.Item):
    Name = scrapy.Field()
    Id = scrapy.Field()
    Year = scrapy.Field()
    Cast = scrapy.Field()
