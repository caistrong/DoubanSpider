# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
import json


class MySQLStorePipeLine(object):
    def __init__(self):
        self.conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root',
                                    passwd='xiaocongcai', db='lmovie', charset='utf8', use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            self.cursor.execute("""INSERT INTO movie_info (title, directors, screenwriters, types, nations, languages, releaseDate, year,
                    duration, actors, knownAs, doubanId, imdbId, posterUrl, star, rate, votesNum, fiveStarRatio, fourStarRatio, threeStarRatio,
                    twoStarRatio, oneStarRatio, summary, posterX, posterY, doubanUrl, playLinks)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                    (
                    item.get('title').encode('utf-8'),
                    json.dumps(item.get('directors'),
                               ensure_ascii=False).encode('utf-8'),
                    json.dumps(item.get('screenwriters'),
                               ensure_ascii=False).encode('utf-8'),
                    json.dumps(item.get('types'),
                               ensure_ascii=False).encode('utf-8'),
                    item.get('nations').encode('utf-8'),
                    item.get('languages').encode('utf-8'),
                    json.dumps(item.get('releaseDate'),
                               ensure_ascii=False).encode('utf-8'),
                    item.get('year').encode('utf-8'),
                    item.get('duration').encode('utf-8'),
                    json.dumps(item.get('actors'),
                               ensure_ascii=False).encode('utf-8'),
                    item.get('knownAs').encode('utf-8'),
                    item.get('doubanId').encode('utf-8'),
                    item.get('imdbId').encode('utf-8'),
                    item.get('posterUrl').encode('utf-8'),
                    item.get('star').encode('utf-8'),
                    str(item.get('rate')).encode('utf-8'),
                    item.get('votesNum').encode('utf-8'),
                    item.get('fiveStarRatio').encode('utf-8'),
                    item.get('fourStarRatio').encode('utf-8'),
                    item.get('threeStarRatio').encode('utf-8'),
                    item.get('twoStarRatio').encode('utf-8'),
                    item.get('oneStarRatio').encode('utf-8'),
                    item.get('summary').encode('utf-8'),
                    str(item.get('posterX')).encode('utf-8'),
                    str(item.get('posterY')).encode('utf-8'),
                    item.get('doubanUrl').encode('utf-8'),
                    json.dumps(item.get('playLinks'),
                               ensure_ascii=False).encode('utf-8')
                    )
                )
            self.conn.commit()
            with open('last_success.json', 'w') as outfile:
                json.dump({
                    'urlListIndex': spider.currentIdx,
                    'movieTitle': item.get('title'),
                    'movueDoubanId': item.get('doubanId')
                    }, outfile, ensure_ascii=False)

        except MySQLdb.Error as err:  # pylint: disable=no-member
            print('Insert Data Error:{e}'.format(e=err))
            self.conn.rollback()

        return item

class StringifyPipeline(object):
    def process_item(self, item, spider):
        return item
