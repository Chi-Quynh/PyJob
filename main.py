from classes.scrape import Session
from selenium.webdriver.support.wait import WebDriverWait
import time


#get a list of urls

url = "https://www.topcv.vn/tim-viec-lam-backend-tai-ho-chi-minh-kl2?type_keyword=0&sba=1&locations=l2"


def main():

    start_time = time.time()
    session = Session(url)
    session.start()
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()

