# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest

class RankerSpider(scrapy.Spider):
    name = 'ranker1'
    allowed_domains = ['www.kgmu.org']
    #start_urls = ['https://www.kgmu.org/kgmu_result/get_results.php?course_id=1&exam_id=2&res_id=1111']
    script = """
            function main(splash, args)
                url = args.url
                headers = {
                    ["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"
                }
                splash:set_custom_headers(headers)
                assert(splash:go(url))
                assert(splash:wait(1))
                roll_no = %s
                input_no = splash:select("#roll_no")
                input_no:focus()
                input_no:send_text(roll_no)
                input_no:send_keys("<Enter>")
                assert(splash:wait(5))
                splash:set_viewport_full()
                assert(splash:wait(1))
                return {
                    splash:html()
                }
            end
        """

    def start_requests(self):
        for roll_no in range(2001012001,2001012245):
            lua_script = self.script % ("\'" + str(roll_no) + "\'")
            yield SplashRequest(url = "https://www.kgmu.org/kgmu_result/get_results.php?course_id=1&exam_id=2&res_id=1111", callback = self.parse, endpoint = "execute", args = {
                "lua_source": lua_script
            })

    def parse(self, response):
        for selector in response.xpath('//*[contains(@id, "pr1")]'):
            rollNo = selector.xpath(".//table[6]/tbody/tr/td[6]/font/text()").get()
            stuId = selector.xpath(".//table[6]/tbody/tr/td[3]/font/text()").get()
            name = selector.xpath(".//table[7]/tbody/tr/td[3]/font/text()").get()
            pAggr = selector.xpath(".//table[17]/tbody/tr/td[3]/b/font/text()").get()
            mAggr = selector.xpath(".//table[17]/tbody/tr/td[5]/b/font/text()").get()
            phAggr = selector.xpath(".//table[17]/tbody/tr/td[7]/b/font/text()").get()
            fmAggr = selector.xpath(".//table[17]/tbody/tr/td[9]/b/font/text()").get()
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
