#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

"""
思路
    1. 发送请求,获取疫情首页
    2. 从疫情首页中提取最近一日各国疫情字符串
    3. 从最近一日各国疫情字符串中,提取json格式字符串
    4. 把json格式字符串，转换为Python类型
    5. 把Python类型的数据,以json格式存入文件中


    》重构原来代码,以提高扩展性
      把功能封装到一个类中
      每一个小功能变成一个方法
      通过run方法启动爬虫

    》实现采集从01月23日以来的世界各国疫情数据
      》加载最近一日各国疫情数据
      》遍历各国疫情数据，获取从01月23日以来的各个国家疫情的URL
      》发送请求,获取获取从01月23日以来的各个国家疫情的json字符串
      》解析各个国家疫情的json字符串,添加到列表
      》以json格式保存从01月23日以来的各个国家疫情数据
"""

import requests
from bs4 import BeautifulSoup
import re
import json
# 需要先导入tqdm模块才可使用，可以直接通过 pip install tqdm 安装命令进行安装
from tqdm import tqdm    # 进度条美化的模块

class CoronaVirusSpider(object):
    
    def __init__(self):  #定义一个URL的方法
        self.home_url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'
    
    def get_content_from_url(self, url):  #定义一个发送请求的方法
        """
        根据URL获取响应的字符串数据
        :param url:请求的URL
        :return:响应内容的字符串
        """
        # 1. 发送请求,获取疫情首页
        response = requests.get(url)
        return response.content.decode()
      
    def parse_home_page(self, home_page, tag_id):
        """
        解析首页内容，获取解析后的python数据
        :param home_page: 首页内容
        :return: 解析后的 python 数据
        """      
        # 2. 从疫情首页中提取最近一日各国疫情字符串
        soup = BeautifulSoup(home_page, 'lxml')
        script = soup.find(id=tag_id)
        # text = script.text
        text = script.string
        # print(text)

        # 3. 从最近一日各国疫情字符串中,提取json格式字符串
        json_str = re.findall(r'\[.+\]', text)[0]
        # print(json_str)

        # 4. 把json格式字符串，转换为Python类型
        data = json.loads(json_str)
        return data

    def parse_corone_virus(self, last_day_corona_virus_of_china, desc):
        # 定义列表，用于存储全国各省疫情数据
        corona_virus = []
        
        # 遍历最近一日全国疫情信息,获取全国各省疫情URL
        for country in tqdm(last_day_corona_virus_of_china, desc):
            # 1.发送请求，获取全国各省从1月23号至今的 json 数据
            statistics_data_url = country['statisticsData']
            statistics_data_json_str = self.get_content_from_url(statistics_data_url)
            # print(statistics_data_json_str)
            # 2.把 json 数据转换为 python 类型的数据，添加到列表中
            statistics_data = json.loads(statistics_data_json_str)['data']
            # print(statistics_data)
            for one_day in statistics_data:
                one_day['provinceName'] = country['provinceName']   # 向 statistics_data 字典中添加数据 国名
                if country.get('countryShortCode'):
                    one_day['countryShortCode'] = country['countryShortCode']
            # print(statistics_data)
            corona_virus.extend(statistics_data)
            # print(corona_virus)
            
        return corona_virus  # 返回获取取的数据
    
    def load(self, path):
        """
        根据路径加载数据
        :param path:
        """
        with open(path, 'r', encoding='utf-8') as fp:
            data = json.load(fp)
        return data        
        
    def save(self, data, path):
        # print(last_day_corona_virus)
        # 5. 把Python类型的数据,以json格式存入文件中
        with open(path, mode='w', encoding='utf-8') as fp:
            json.dump(data, fp, ensure_ascii=False)
            
    def crawl_last_day_corona_virus(self):
        """
        采集最近一天的各国疫情信息
        :return:
        """
        # 1.发送请求，获取首页内容
        home_page = self.get_content_from_url(self.home_url)
        # 2.解析首页内容，获取最近一天的各国疫情数据
        last_day_corona_virus = self.parse_home_page(home_page, tag_id='getListByCountryTypeService2true')
        # 3.保存数据
        self.save(last_day_corona_virus, 'data/last_day_corona_virus.json')

    def crawl_corona_virus(self):
        """
        采集从1月23号以来各国疫情数据
        :return:
        """
        # 1.加载各国疫情数据
        last_day_corona_virus = self.load('data/last_day_corona_virus.json')
        
        ##### 以下被优化掉 改为 load 方式加载
        # with open('data/last_day_corona_virus.json', 'r', encoding='utf-8') as fp:
        #     last_day_corona_virus = json.load(fp)
        # print(last_day_corona_virus)
        
        corona_virus = self.parse_corone_virus(last_day_corona_virus, '采集各国疫情数据')
        
        ### 以下代码优化为 parse_corone_virus 方法
        
        # # 定义列表，用于存储各国疫情数据
        # corona_virus = []        
        # # 2.遍历国国疫情数据，获取统计的URL
        # for country in tqdm(last_day_corona_virus, '采集各国疫情数据'):
        #     # 3.发送请求，获取各国从1月23号至今的 json 数据
        #     statistics_data_url = country['statisticsData']
        #     statistics_data_json_str = self.get_content_from_url(statistics_data_url)
        #     # print(statistics_data_json_str)
        #     # 4.把 json 数据转换为 python 类型的数据，添加到列表中
        #     statistics_data = json.loads(statistics_data_json_str)['data']
        #     # print(statistics_data)
        #     for one_day in statistics_data:
        #         one_day['provinceName'] = country['provinceName']   # 向 statistics_data 字典中添加数据 国名
        #         one_day['countryShortCode'] = country['countryShortCode']  # 向 statistics_data 字典中添加数据 国名缩写
        #     # print(statistics_data)
        #     corona_virus.extend(statistics_data)
            
        # 5.把列表以 json 格式保存为文件
        self.save(corona_virus, 'data/corona_virus.json')
        
    def crawl_last_day_corona_virus_of_china(self):
        """
        采集最近一日各省疫情数据
        """
        # 1.发送请求，获取疫情首页
        home_page = self.get_content_from_url(self.home_url)
        # 2.解析疫情首页，获取最近一日各省疫情数据
        crawl_last_day_corona_virus_of_china = self.parse_home_page(home_page, tag_id='getAreaStat')
        # 3.保存疫情数据
        self.save(crawl_last_day_corona_virus_of_china, 'data/last_day_corona_virus_of_china.json')
        
    def crawl_corona_virus_of_china(self):
        """
        采集历史以来全国各省的疫情数据
        :return:
        """
        # 加载最近一日全国各省疫情信息
        last_day_corona_virus_of_china = self.load('data/last_day_corona_virus_of_china.json')
        
        ##### 以下被优化掉 改为 load 方式加载
        # with open('data/crawl_last_day_corona_virus_of_china.json', mode='r', encoding='utf-8') as fp:
        #     last_day_corona_virus_of_china = json.load(fp)

        # 遍历最近一日全国疫情信息,获取全国各省疫情URL
        corona_virus = self.parse_corone_virus(last_day_corona_virus_of_china, '采集各省疫情数据')
        # print(corona_virus)
        
        # 5.把列表以 json 格式保存为文件
        self.save(corona_virus, 'data/corona_virus_of_china.json')
        
    def run(self):  #定义一个run方法
        # self.crawl_last_day_corona_virus()  #运行获取各国当日数据
        self.crawl_corona_virus()  # 运行获取各国所有数据
        # self.crawl_last_day_corona_virus_of_china()  #运行获取各省当日数据
        self.crawl_corona_virus_of_china()  # 运行获取各省所有数据
        

if __name__ == '__main__':
    spider = CoronaVirusSpider()  #创建一个爬虫对象
    spider.run()