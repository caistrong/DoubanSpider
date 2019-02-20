from scrapy.cmdline import execute

try:
    execute(
        [
            'scrapy',
            'crawl',
            'douban_movie'
        ]
    )
except SystemExit:
    pass