import os
from selenium import webdriver

class Request:
    def __init__(self, base_url):
        self._phantomjs_path = os.path.join(os.curdir,'phantomjs/bin/pahntomjs')
        self.base_url = base_url
        self._driver = webdriver.PhantomJS(self._phantomjs_path)

    def fetch_data(self, forecast, area):
        url = self._base_url.format(forecast = forecast, area= area)
        self._driver.get(url)
        if self._driver.title == '404 Not Found':
            error_message = ('Could Not find the area')
            raise Excpetion(error_message)
        return self._driver.page_source