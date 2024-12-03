from dataclasses import dataclass

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC

#I need to move onto processing the data


class Scrape:
    def setup(url):
        driver = webdriver.Chrome()
        driver.get(url)
        return driver

    
    def get_element_by_XPATH(driver,xpath):
        try:
            job_title = driver.find_element(By.XPATH, (xpath))
            return job_title
        except Exception as e:
            return e
    
    def get_elements_by_XPATH(driver,xpath):
        try:
            job_titles = driver.find_elements(By.XPATH, (xpath))
            return job_titles
        except Exception as e:
            return e
    
    def get_children(parent, keyword):
        try:
            for child in parent:
                print(child.text)

            return 0
        except Exception as e:
            return e    
    
    #get the job description
    
    def teardown(driver):
        driver.quit()


