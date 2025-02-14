
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType


class Session:
    def __init__(self, url):
        self.url = url

    #config for driver
    def setup():
        pass

    #start the session
    def start(self):
        driver = webdriver.Chrome()
        try:
            driver.get(self.url)    
            html = driver.page_source
            return html
        finally:
            driver.delete_all_cookies()
            driver.quit()

    #html->[DOM,DOM,DOM]
    #segment html into digestable batches for LLM
    #ex: TopCV html -> [<div>...</div>,<div>...</div>,<div>...</div>]
    def batch(self):
        pass

    #array of DOMs -> array of strings
    #extract text from DOMs using LLM API
    #if not job text, return None
    #ex:[<div>...</div>,<div>...</div>,<div>...</div>] -> ['job_title','url_link','job_description']
    #ex:[<div>...</div>,<div>...</div>,<div>...</div>] -> [None,'text2','text3']
    def AI(self):
        pass

    def store(self):
        pass

    #write a cover letter if needed
    def write(self):
        pass










        


