# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class DoubanMovieItem(scrapy.Item):
    
    title = scrapy.Field() # from API
    directors = scrapy.Field() # from API
    actors = scrapy.Field() # from API
    year = scrapy.Field() #from HTML Page
    screenwriters = scrapy.Field() # from HTML Page
    types = scrapy.Field() # from HTML Page
    nations = scrapy.Field() # from HTML Page
    languages = scrapy.Field() # from HTML Page
    releaseDate = scrapy.Field() # from HTML Page
    duration = scrapy.Field() # from HTML Page
    knownAs = scrapy.Field() # from HTML Page
    doubanId = scrapy.Field() # from API
    imdbId = scrapy.Field() # from HTML Page
    posterUrl = scrapy.Field() # from API
    rate = scrapy.Field() # from API
    star = scrapy.Field() # from API
    votesNum = scrapy.Field() # from HTML Page
    fiveStarRatio = scrapy.Field() # from HTML Page
    fourStarRatio = scrapy.Field() # from HTML Page
    threeStarRatio = scrapy.Field() # from HTML Page
    twoStarRatio = scrapy.Field() # from HTML Page
    oneStarRatio = scrapy.Field() # from HTML Page
    summary = scrapy.Field() # from HTML Page
    posterX = scrapy.Field() # from API
    posterY = scrapy.Field() # from API
    doubanUrl = scrapy.Field() # from API