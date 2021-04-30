import scrapy
from imdbcast.imdbcast.items import ImdbcastItem


class CastSpider(scrapy.Spider):
    per_page = 50
    page = 1
    target_page = 2
    name = 'cast'
    start_urls = ['https://www.imdb.com/search/title/?title_type=feature,tv_movie&view=simple&sort=num_votes,desc']

    def parse(self, response):
        movies = response.css('.col-title a')
        for movie in movies:
            item = ImdbcastItem()
            item['Name'] = movie.xpath('text()').get()
            item['Year'] = movie.xpath("following-sibling::span/text()").get()[1:-1]
            link = movie.xpath('@href').get()
            cast_page = link[:link.find('?')] + '/'
            yield response.follow(cast_page, callback=self.parse_movie, meta={'movie': item})
        if self.page < self.target_page:
            self.page += 1
            next_page = (self.start_urls[0] + "&start={0}").format(self.page*self.per_page)
            yield response.follow(next_page, callback=self.parse)

    def parse_movie(self, response):
        movie = response.meta['movie']
        movie['Id'] = response.xpath("//meta[@property='pageId']/@content").get()
        movie['Cast'] = []
        cast_all_tr = response.xpath("//table[@class='cast_list']/tr")
        for tr in cast_all_tr:
            movie['Cast'].append(tr.xpath("td[2]/a/text()").get())
        movie['Cast'] = [cast.rstrip("\n")[1:] for cast in movie['Cast'] if cast is not None]
        yield movie
