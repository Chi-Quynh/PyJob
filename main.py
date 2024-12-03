from classes.scrape import Scrape
from selenium.webdriver.support.wait import WebDriverWait
from classes.execute import insert_data, set_table


xpath ="//div[@class='title-block']//a[@rel='nooppener noreferrer']"
url = "https://www.topcv.vn/tim-viec-lam-data-engineer?sba=1&category_family="

def main():
    driver = Scrape.setup(url)

    #wait elements to load
    WebDriverWait(driver, 5)
    try:
        job_list = get_job_list(driver)
        print("Number of jobs indexed:")
        print(label_job_data(job_list, 0))
    except Exception as e:
        print(e)
    finally:
        Scrape.teardown(driver)


def label_job_data(job, index):
    if index >= len(job):
        return 0
    job_title = job[index].text
    job_link = job[index].get_attribute("href")
    job_company = job[index+1].text
    if "Pro\n" in job_company:
        job_company = job_company.replace("Pro\n", "")
    insert_data((job_title, job_link, job_company))
    return 1 + label_job_data(job, index+2)

def get_job_list(driver):
    try:
        job = Scrape.get_elements_by_XPATH(driver,xpath)
        print("Scraping job list completed")
        return job
    except Exception as e:
        print(e)


main()