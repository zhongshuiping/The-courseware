# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CompanyItem(scrapy.Item):

    # 公司id (url数字部分)
    info_id = scrapy.Field()
    # 公司名称
    company_name = scrapy.Field()
    # 公司口号
    slogan = scrapy.Field()
    # 分类
    scope = scrapy.Field()
    # 子分类
    sub_scope = scrapy.Field()

    # 所在城市
    city = scrapy.Field()
    # 所在区域
    area = scrapy.Field()
    # 公司主页
    home_page = scrapy.Field()
    # 公司标签
    tags = scrapy.Field()

    # 公司简介
    company_intro = scrapy.Field()
    # 公司全称：
    company_full_name = scrapy.Field()
    # 成立时间：
    found_time = scrapy.Field()
    # 公司规模：
    company_size = scrapy.Field()
    # 运营状态
    company_status = scrapy.Field()

    # 投资情况列表：包含获投时间、融资阶段、融资金额、投资公司
    tz_info = scrapy.Field()
    # 团队信息列表：包含成员姓名、成员职称、成员介绍
    tm_info = scrapy.Field()
    # 产品信息列表：包含产品名称、产品类型、产品介绍
    pdt_info = scrapy.Field()
