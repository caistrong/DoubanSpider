
from douban_spider.my_middlewares.constants import PROXIES
import random

# 用了开源的scrapy_proxies库,这里暂时没用
class RandomProxy(object):
    def process_request(self,request, spider):
        proxy = random.choice(PROXIES)
        request.meta['proxy'] = 'https://%s'% proxy