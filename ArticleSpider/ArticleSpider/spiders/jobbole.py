# -*- coding: utf-8 -*-
import scrapy
import re


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/112783/']

    def parse(self, response):
        title = response.xpath('//div[@class="entry-header"]/h1/text()').extract()[0]
        create_date = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()').extract()[0].strip().replace('·','').strip()
        praise_nums = response.xpath("//span[contains(@class, 'vote-post-up')]/h10/text()").extract()[0]
        fav_nums = response.xpath("//span[contains(@class, 'bookmark-btn')]/text()").extract()[0]
        fav_nums =  response.css("span.bookmark-btn::text").extract()[0]
        match_re = re.match(r".*(\d+).*", fav_nums)
        if match_re:
            fav_nums = match_re.group(1)

        comment_num = response.xpath("//a[@href='#article-comment']/span").extract()[0]
        match_re = re.match(r".*(\d+).*", comment_num)
        if match_re:
            comment_num = match_re.group(1)

        contetn = response.xpath("//div[@class='entry']").extract()[0]

        print(contetn)

        #css选择
        title1 = response.css(".entry-header h1::text").extract_first()
        create_date1 = response.css(".entry-meta-hide-on-mobile::text").extract()[0].strip().replace('·', '').strip()
        praise_nums1 = response.css(".vote-post-up h10::text").extract_first().strip()
        fav_nums1 = response.css("span.bookmark-btn::text").extract_first()
        match_re = re.match(r".*(\d+).*", fav_nums1)
        if match_re:
            fav_nums1 = match_re.group(1)

        comment_num1 = response.css('a[href="#article-comment"] span::text').extract_first()
        match_re = re.match(r".*(\d+).*", comment_num1)
        if match_re:
            comment_num1 = match_re.group(1)

        content1 = response.css("div.entry").extract_first()
        tag1 = response.css("p.entry-meta-hide-on-mobile a::text").extract_first()
        tag_list = [element for element in tag1 if not element.strip().endswith('\0')]
        tag_list = ",".join(tag_list)
        pass
