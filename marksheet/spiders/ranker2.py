# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

class Ranker2Spider(scrapy.Spider):
    name = 'ranker2'
    allowed_domains = ['www.kgmu.org']
    start_urls = ['https://www.kgmu.org/kgmu_result/get_results.php?course_id=1&exam_id=2&res_id=1111']

    def parse(self, response):
        for roll_no in range(2001012135,2001012245):
            driver_options = Options()
            driver_options.add_argument("--headless")
            driver = webdriver.Chrome(executable_path="./chromedriver.exe", options=driver_options)
            driver.get("https://www.kgmu.org/kgmu_result/get_results.php?course_id=1&exam_id=2&res_id=1111")
            input = driver.find_element_by_xpath('//input[@id="roll_no"]')
            input.send_keys(str(roll_no))
            search = driver.find_element_by_xpath('//input[@name="get_result"]')
            search.click()
            rollNo = driver.find_element_by_xpath("//*[contains(@id, 'pr1')]/table[6]/tbody/tr/td[6]/font").text
            stuId = driver.find_element_by_xpath("//*[contains(@id, 'pr1')]/table[6]/tbody/tr/td[3]/font").text
            name = driver.find_element_by_xpath("//*[contains(@id, 'pr1')]/table[7]/tbody/tr/td[3]/font").text
            pAggr = driver.find_element_by_xpath("//*[contains(@id, 'pr1')]/table[17]/tbody/tr/td[3]/b/font").text
            mAggr = driver.find_element_by_xpath("//*[contains(@id, 'pr1')]/table[17]/tbody/tr/td[5]/b/font").text
            phAggr = driver.find_element_by_xpath("//*[contains(@id, 'pr1')]/table[17]/tbody/tr/td[7]/b/font").text
            fmAggr = driver.find_element_by_xpath("//*[contains(@id, 'pr1')]/table[17]/tbody/tr/td[9]/b/font").text
            if pAggr!="NA" or phAggr!="NA" or mAggr!="NA" or fmAggr!="NA":
                if pAggr=="NA":
                    pAggr=0
                else:
                    pAggr=float(pAggr)
                if phAggr=="NA":
                    phAggr=0
                else:
                    phAggr=float(phAggr)
                if mAggr=="NA":
                    mAggr=0
                else:
                    mAggr=float(mAggr)
                if fmAggr=="NA":
                    fmAggr=0
                else:
                    fmAggr=float(fmAggr)
                total = (pAggr+phAggr+mAggr+fmAggr)
                yield {
                    "Roll No." : rollNo,
                    "Student ID" : stuId,
                    "Name" : name,
                    "Pathology Aggregate" : pAggr,
                    "Microbiology Aggregate" : mAggr,
                    "Pharmacology Aggregate" : phAggr,
                    "Forensic Medicine Aggregate" : fmAggr,
                    "Total" : total
                }
            driver.close()