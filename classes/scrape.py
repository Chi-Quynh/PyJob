
from selenium import webdriver



class Session:
    def __init__(self, url):
        self.url = url

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
    #ex:[<div>...</div>,<div>...</div>,<div>...</div>] -> ['text1','text2','text3']
    #ex:[<div>...</div>,<div>...</div>,<div>...</div>] -> [None,'text2','text3']
    def AI(self):
        pass










        


