from object import Scrape
from selenium.webdriver.support.wait import WebDriverWait

xpath ="//div[@class='title-block']//a[@rel='nooppener noreferrer']"
url = "https://www.topcv.vn/tim-viec-lam-data-engineer?sba=1&category_family="

def main():
    driver = Scrape.setup(url)

    #wait elements to load
    WebDriverWait(driver, 5)
    '''
    jobElements = Scrape.get_element_by_XPATH(driver,xpath)
    for job in jobElements:
        if job.class = company//companyjob pro:
            job_company = job.text
        else:
            job_title = job.text
            job_link = job.get_attribute("href")

        print(job_company)-> input into postgress
        print(job_title)-> input into postgress
        print(job_link)-> input into postgress
    '''
    
    
    job_title = Scrape.get_element_by_XPATH(driver,xpath).text
    job_link = job_title.get_attribute("href")
    print(job_title)
    print(job_link)
    Scrape.teardown(driver)

main()




