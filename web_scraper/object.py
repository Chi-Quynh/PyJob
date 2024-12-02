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
    
    
    
    
    #get rel noope, the link
    #then get the a for the job title
    #get the salary
    #get the location
    #get the company name 
    '''
    <a class="company" href="https://www.topcv.vn/cong-ty/cong-ty-tnhh-skylink-group/24980.html" data-toggle="tooltip" title="" data-placement="top" target="_blank" rel="nooppener noreferrer" data-original-title="Công ty TNHH Skylink Group">
                                            <span class="company-name">Công ty TNHH Skylink Group</span>
                                        </a>
    get the a element with company class
    get the span for company name 

    <a target="_blank" href="https://www.topcv.vn/viec-lam/data-engineer-game/1551635.html?ta_source=JobSearchList_LinkDetail&amp;u_sr_id=kllo6bHng9ADfm1VpF8vH3ZYWRhyiXMgj1PwjSfo_1732932188" rel="nooppener noreferrer">
                                            <span data-toggle="tooltip" data-container="body" data-placement="top" title="" data-original-title="Data Engineer (Game)">Data Engineer (Game)</span>
                                                                                    </a>
    '''
    #get the job description
    
    def teardown(driver):
        driver.quit()

