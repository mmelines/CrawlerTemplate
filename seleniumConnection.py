# selenium imports
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
# python imports
import time

class MmeDriver:

    def __init__(self):
        # Define Firefox Path
        firefox_path = "/usr/local/bin/geckodriver"
        # Define Browser Options
        firefox_options = Options()
        firefox_options.add_argument("--headless") # Hides the browser window
        # Instantiate Webdriver
        self.driver = webdriver.Firefox(executable_path=firefox_path, 
                    options=firefox_options)
        self.page = None
        self.html = None
        self.url = ""

    def getSeleniumPage(self, url):
        self.url = url
        self.page = self.driver.get(url)
        return self.page

# -----------------------------------------------------------------------------
# selenium browsing methods
# ----------------------------------------------------------------------------- 
    def read_page(self, url):
        if url != None:
            self.url = url
        self.getSeleniumPage(self.url)
        # Scroll page to load whole content
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            # Scroll down to the bottom.
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Wait to load the page
            time.sleep(2)
            # Calculate new scroll height and compare with last height.
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        self.html = self.driver.page_source
        return self.html

if __name__ == '__main__':
    driver = MmeDriver()
    driver.read_page("https://www.google.com")
    print(driver.html)