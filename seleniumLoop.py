# configuration
from Config.config import CrawlConfig as config
# selenium imports
from seleniumConnection import MmeDriver as dr
# python imports
from pprint import pprint

queue = ["https://google.com"]
i = 0
driver = dr()
if __name__=='__main__':
    while i < len(queue):
        print("{0}. {1}".format(i, queue[i]))
        driver.read_page(queue[i])
        # add or remove items from queue here
        i += 1
