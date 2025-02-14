from classes.scrape import Session
from selenium.webdriver.support.wait import WebDriverWait
import time
import logging


logging.basicConfig(level=logging.DEBUG)

#get a list of urls

url = "https://jobs.vn.indeed.com/"
urls = ["https://jobs.vn.indeed.com/", "https://www.topcv.vn/viec-lam", "https://it.viecoi.vn/"]

def main():

    start_time = time.time()
    for url in urls:
        session = Session(url)
        try:
            session.start()
        except Exception as e:
            print(e)
        finally:
            print("Session ended")
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()

