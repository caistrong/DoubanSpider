from scrapy.cmdline import execute

try:
    execute(
        [
            'scrapy',
            'crawl',
            'douban_movie',
            '-o',
            'movies.jl',
        ]
    )
except SystemExit:
    pass