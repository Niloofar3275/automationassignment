from imdbcast.imdbcast.spiders.cast_spider import CastSpider
from scrapy.crawler import CrawlerProcess
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from most_frequent_members import get_top_5


def clean_json_feed():
    f = open('movies.json', 'w')
    f.write('')
    f.close()


def run_spider():
    process = CrawlerProcess(settings={
        "FEEDS": {
            "movies.json": {"format": "json"},
        },
    })

    process.crawl(CastSpider)
    process.start()


def authorize_gspread():
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    return gspread.authorize(creds)


clean_json_feed()
run_spider()
top_5_updated = get_top_5()

gspread_client = authorize_gspread()
sheet = gspread_client.open("5-most-frequent-cast-members").sheet1
for i in range(1, 6):
    sheet.update_cell(i, 1, top_5_updated[i-1])