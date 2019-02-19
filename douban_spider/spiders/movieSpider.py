import scrapy
import json
import string
import random
from urllib.parse import urlencode
from scrapy.loader import ItemLoader
from douban_spider.items import DoubanMovieItem


class MovieSpider(scrapy.Spider):
    name = "douban_movie"
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'Cookie':'bid=e_HJMaweruw'
    }
    allUrls = []
    currentIdx = 0
    # 根据豆瓣电影分类ajax请求url的特点构造请求url,实际上不能保证覆盖豆瓣都所有电影，也不能保证构造出的url一定有电影数据。
    def generateAllUrls(self):
        formdata = {
            'sort': 'T',
            'range': "m,n",
            'tags': '电影',
            'start': '0'
        }
        scores = [ '9,10', '8,9','7.6, 8','7,3,7.6','7,7.3','6.7, 7','6.5, 6.7','6,6.5','5,6', '4,5', '3,4','2,3']
        for score in scores:
            formdata['range'] = score
            for i in range(0, 9980, 20):
                start = str(i)
                formdata['range'] = score
                formdata['start'] = start
                url = 'http://movie.douban.com/j/new_search_subjects?' + urlencode(formdata)
                self.allUrls.append(url)
        
    def start_requests(self):
        self.generateAllUrls()
        startUrl = self.allUrls[self.currentIdx]
        yield scrapy.Request(startUrl, headers=self.headers ,callback=self.collectMovies, errback=self.changeCookies)
    
    def changeCookies(self, failure):
        # 记录错误
        self.logger.error(repr(failure))
        # 目前错误一般是403错误，更改cookies避开豆瓣反爬虫机制
        self.headers['Cookie'] = "bid=" + "".join(random.sample(string.ascii_letters + string.digits, 11))
        # 继续刚刚失败的那个请求
        yield scrapy.Request(self.allUrls[self.currentIdx], headers=self.headers, callback=self.collectMovies, errback=self.changeCookies)

    def collectMovies(self, response):
            
        rspJson = json.loads(response.text)
        moviedatas = rspJson.get('data')
        # 每完成一次请求就增加当前数组下标
        self.currentIdx += 1
        if(len(moviedatas) == 0):
            # 请求allUrls里的下一个链接
            yield scrapy.Request(self.allUrls[self.currentIdx], headers=self.headers, callback=self.collectMovies, errback=self.changeCookies)
        
        for data in moviedatas:
            il = ItemLoader(item=DoubanMovieItem(), response=response)
            il.add_value('title', data.get('title'))
            il.add_value('directors', data.get('directors'))
            il.add_value('rate', data.get('rate'))
            il.add_value('star', data.get('star'))
            il.add_value('posterUrl', data.get('cover'))
            il.add_value('posterX', data.get('cover_x'))
            il.add_value('posterY', data.get('cover_y'))
            il.add_value('doubanUrl', data.get('url'))
            il.add_value('actors', data.get('casts'))
            il.add_value('doubanId', data.get('id'))
            mi = il.load_item()
            # data.get('url') 是豆瓣电影详情页面
            yield scrapy.Request(data.get('url'), headers=self.headers, callback=self.parseDetailHtml, meta={'movieItem': mi}, errback=self.changeCookies)

        yield scrapy.Request(self.allUrls[self.currentIdx], headers=self.headers, callback=self.collectMovies, errback=self.changeCookies)

    def parseDetailHtml(self, response):
        mi = response.meta.get('movieItem')
        il = ItemLoader(item=mi, response=response)
        
        il.add_xpath('year', '//span[@class="year"]/text()')
        il.add_xpath('screenwriters', '//div[@id="info"]/span[2]/span[2]/a/text()')
        il.add_xpath('types', '//span[@property="v:genre"]/text()')
        # il.add_xpath('nations', '//div[@id="info"]', re='[\u4e00-\u9fa5]{4}\/[\u4e00-\u9fa5]{2}:</span>.*?([A-Za-z]+|[\u4e00-\u9fa5]+)') # 这个正则感觉不太可靠
        il.add_xpath('nations', '//div[@id="info"]', re='制片国家/地区:</span>.*?(.+)<') # 这个正则感觉不太可靠 下同
        il.add_xpath('languages', '//div[@id="info"]', re='语言:</span>.*?(.+)<')
        il.add_xpath('releaseDate', '//span[@property="v:initialReleaseDate"]/text()')
        il.add_xpath('duration', '//span[@property="v:runtime"]/text()')
        il.add_xpath('knownAs', '//div[@id="info"]', re='又名:</span>.*?(.*)<')
        il.add_xpath('imdbId', '//div[@id="info"]/a[@rel="nofollow"]/text()')
        il.add_xpath('votesNum', '//span[@property="v:votes"]/text()')
        il.add_xpath('fiveStarRatio', '//div[@class="ratings-on-weight"]/div[1]/span[@class="rating_per"]/text()')
        il.add_xpath('fourStarRatio', '//div[@class="ratings-on-weight"]/div[2]/span[@class="rating_per"]/text()')
        il.add_xpath('threeStarRatio', '//div[@class="ratings-on-weight"]/div[3]/span[@class="rating_per"]/text()')
        il.add_xpath('twoStarRatio', '//div[@class="ratings-on-weight"]/div[4]/span[@class="rating_per"]/text()')
        il.add_xpath('oneStarRatio', '//div[@class="ratings-on-weight"]/div[5]/span[@class="rating_per"]/text()')
        il.add_xpath('summary', '//span[@property="v:summary"]/text()')
        il.add_xpath('playLinks', '//ul[@class="bs"]/li/a', re='data-cn=(.*) href=(.*)')
    
        return il.load_item()



