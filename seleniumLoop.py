# configuration
from config.main import CrawlConfig as config
config = config()
#
from datetime import datetime
from sys import getsizeof as sizeup
#
from urllib.request import urlopen as req
from urllib.parse import urlparse as parse
#
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
# python imports
import time
from pprint import pprint
# database imports
from db import Select as sel
from db import Insert as ins