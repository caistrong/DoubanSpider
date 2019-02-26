# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst
class DoubanMovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field(
        output_processor=TakeFirst(),
    ) # from API
    directors = scrapy.Field(serializer=str) # from API
    actors = scrapy.Field(serializer=str) # from API
    year = scrapy.Field(
        output_processor=TakeFirst(),
    ) #from HTML Page
    screenwriters = scrapy.Field(serializer=str) # from HTML Page
    types = scrapy.Field(serializer=str) # from HTML Page
    nations = scrapy.Field(
        output_processor=TakeFirst(),
    ) # from HTML Page
    languages = scrapy.Field(
        output_processor=TakeFirst(),
    ) # from HTML Page
    releaseDate = scrapy.Field(serializer=str) # from HTML Page
    duration = scrapy.Field(
        output_processor=TakeFirst(),
    ) # from HTML Page
    knownAs = scrapy.Field(
        output_processor=TakeFirst(),
    ) # from HTML Page
    doubanId = scrapy.Field(
        output_processor=TakeFirst(),
    ) # from API
    imdbId = scrapy.Field(
        output_processor=TakeFirst(),
    ) # from HTML Page
    posterUrl = scrapy.Field(
        output_processor=TakeFirst(),
    ) # from API
    rate = scrapy.Field(
        output_processor=TakeFirst(),
    ) # from API
    star = scrapy.Field(
        output_processor=TakeFirst(),
    ) # from API
    votesNum = scrapy.Field(
        output_processor=TakeFirst(),
    ) # from HTML Page
    fiveStarRatio = scrapy.Field(
        output_processor=TakeFirst(),
    ) # from HTML Page
    fourStarRatio = scrapy.Field(
        output_processor=TakeFirst(),
    ) # from HTML Page
    threeStarRatio = scrapy.Field(
        output_processor=TakeFirst(),
    ) # from HTML Page
    twoStarRatio = scrapy.Field(
        output_processor=TakeFirst(),
    ) # from HTML Page
    oneStarRatio = scrapy.Field(
        output_processor=TakeFirst(),
    ) # from HTML Page
    summary = scrapy.Field(
        output_processor=TakeFirst(),
    ) # from HTML Page
    posterX = scrapy.Field(
        serializer=str,
        output_processor=TakeFirst(),
    ) # from API
    posterY = scrapy.Field(
        serializer=str,
        output_processor=TakeFirst(),
    ) # from API
    doubanUrl = scrapy.Field(
        output_processor=TakeFirst(),
    ) # from API
    playLinks = scrapy.Field(serializer=str) # from HTML Page