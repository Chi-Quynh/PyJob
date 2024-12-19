# PyJob - Job Data Scraper and Analysis Tool

## Overview

**PyJob** is a Data Science project that can scrape job listings and output as analysis report following the ETL model 

![Program Results](https://github.com/Chi-Quynh/PyJob/blob/Final/Screenshot%202024-12-18%20160011.png)

## Features

- Web scraping of job data from topCV using Python and Selenium.
- Automated extraction of job-related data, including job title, company, location, salary range, and job description.
- Data storage in PostgreSQL database for scalability and performance.
- Export as CSV Excel file format for convenient viewing

## Extract
Selenium and Python are used to access the website and extract DOM elements for data. We used web driver here because web crawler are blocked by many websites.

## Transform
The data are then filtered using code, 

## Load
The data are then saved in Relational databases on PostgreSQL 
Then, pulled from PostgreSQL to export as CSV file

## Technologies Used

- **Python**
- The primary programming language for scraping and data manipulation.
- **Selenium**
- A web driver used for web scraping and data extraction.
- **PostgreSQL**
- A relational database used to store job data.

## Installation

Clone the repository:
   ```bash
   git clone https://github.com/Chi-Quynh/PyJob.git
   ```


Set up dependicies:
   ```bash
   pip install -r requirements.txt
   ```



