import scrapy
from scrapy.spider import Spider
from scrapy.selector import Selector
#from tutorial.items import DmozItem


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    #allowed_domains = ["hps.mep.gov.cn"]
    start_urls = ["http://hps.mep.gov.cn/jsxm/npzxmgs/201704/t20170405_409325.shtml"]

    def parse(self, response):
        sel = Selector(response)
        p_1 = "/html/body/div[1]/div[2]/div[1]/div[2]/div/table/tbody/tr["
        p_2 = "]/td["
        p_3 = "]/p/span/text()"
        p_time = "/html/body/div[1]/div[2]/div[1]/div[1]/span/p/text()"
        items = []
        for i in [2]:
            u_name = [p_1,str(i),p_2,str(2),p_3]
            u_n = "".join(u_name)
            item['name'] = sel.xpath(u_name).extract()
            u_location = [p_1, str(i), p_2, str(3), p_3]
            u_l = "".join(u_location)
            item['location'] = sel.xpath(u_l).extract()
            u_company = [p_1, str(i), p_2, str(4), p_3]
            u_c = "".join(u_company)
            item['company'] = sel.xpath(u_c).extract()
            u_Overview = [p_1, str(i), p_2, str(6), p_3]
            u_o = "".join(u_Overview)
            item['Overview'] = sel.xpath(u_o).extract()
            item['publishtime'] = sel.xpath(p_time)
            items.append(item)
        return items
