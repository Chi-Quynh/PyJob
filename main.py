import pandas as pd
from classes.scrape import Scrape
from selenium.webdriver.support.wait import WebDriverWait
from classes.execute import insert_data, set_table, get_data

company_name = "company_name"
job_title = "job_title"

letter_data_engineer="Kính gửi {company_name},\nEm hiện đang viết bức thư này nhờ sự automation của dự án Data Science PyJob em tự build. Em có cũng kiến thức trong mảng Software và Webdev nhờ làm các dự án chung và riêng. Em rất muốn có thể học hỏi thêm kiến thức và kinh nghiệm khi làm việc ở công ty dưới chức danh {job_title}.\nThân gửi,\nChi"
letter_data_analyst="Kính gửi {company_name},\nEm hiện đang viết bức thư này nhờ sự automation của dự án Data Science PyJob em tự build. Em có technical skills ( Python, SQL, etc) and people skills ( dạy tiếng Anh, làm việc với khách hàng) Em có cũng kiến thức trong mảng Software và Webdev nhờ làm các dự án chung và riêng. Em rất muốn có thể học hỏi thêm kiến thức và kinh nghiệm khi làm việc ở công ty dưới chức danh {job_title}.\nThân gửi,\nChi"
letter_data_analyst="Kính gửi {company_name},\nEm hiện đang viết bức thư này nhờ sự automation của dự án Data Science PyJob em tự build. Em có technical skills ( Python, SQL, etc) and people skills ( dạy tiếng Anh, làm việc với khách hàng) Em có cũng kiến thức trong mảng Software và Webdev nhờ làm các dự án chung và riêng. Em rất muốn có thể học hỏi thêm kiến thức và kinh nghiệm khi làm việc ở công ty dưới chức danh {job_title}.\nThân gửi,\nChi"

letter_QA="Kính gửi {company_name},\n\nEm tên là Đặng Chi, hiện đang là sinh viên chuyên ngành Khoa học Máy tính tại Trường Đại học Công nghệ Swinburne (Liên kết FPT). Em mong muốn ứng tuyển vào vị trí {job_title} tại Quý công ty để vừa có thể hiểu rõ hơn về quy trình phát triển và bảo trì sản phẩm, vừa tích lũy thêm kinh nghiệm thực tiễn, đồng thời cải thiện thu nhập của bản thân trong quá trình học tập.\nXin chân thành cảm ơn Quý công ty đã xem xét thư ứng tuyển của em.\n\nTrân trọng,\nĐặng Chi"
company_name = "company_new_name"

xpath ="//div[@class='title-block']//a[@rel='nooppener noreferrer']"
url = "https://www.topcv.vn/tim-viec-lam-data-engineer-tai-ho-chi-minh-kl2?type_keyword=0&locations=l2&sba=1"

def main():
    driver = Scrape.setup(url)

    #wait elements to load
    WebDriverWait(driver, 5)
    try:
        
        #create table
        set_table()

        #extract
        job_list = scrape_web(driver)
        print("Number of jobs indexed:")
        print(len(job_list))
        for job in job_list:
            print(job.text)
        
    
        #transform & load
        print(label_job_data(job_list, 0))
        
        #export data as excel
        export_job_list(letter_data_engineer)
        
        
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

def scrape_web(driver):
    try:
        job = Scrape.get_elements_by_XPATH(driver,xpath)
        print("Scraping job list completed")
        return job
    except Exception as e:
        print(e)

def export_job_list(letter):
    try:
        jobs = get_data()

        # creating the DataFrame
        job_data = create_data_mark(jobs, letter)

        # determining the name of the file
        file_name = 'Output.xlsx'

        # saving the excel
        job_data.to_excel(file_name)
        print('DataFrame is written to Excel File successfully.')
        
    except Exception as e:
        print(e)
    
def create_data_mark(jobs, letter):
    ID={}
    job_link={}
    job_letter={}

        
    index  = 0
    for job in jobs:
        ID[index]=job[0]
        job_link[index]=job[2]
        job_letter[index]=letter.format(company_name=job[3], job_title=job[1])
        index+=1

    job_data = pd.DataFrame({'ID': ID,'job_link': job_link, 'job_letter': job_letter})
    return job_data

if __name__ == "__main__":
    main()
