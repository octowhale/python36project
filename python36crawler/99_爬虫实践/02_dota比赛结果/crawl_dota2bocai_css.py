#!/usr/bin/env python
# encoding: utf-8

# python 3.6

import os
import sys
import requests
from bs4 import BeautifulSoup, element

"""
https://zhuanlan.zhihu.com/p/26747717

这里使用 css 选择器

"""


def get_html(url):
    r = requests.get(url, timeout=30)
    r.raise_for_status()

    r.encoding = r.apparent_encoding

    return r.text


def get_match(url):
    """解析比赛结果"""

    """文件获取"""
    html = open('dota2match.html', 'rb')

    """网页获取"""
    # html=get_html(url)

    """"""
    soup = BeautifulSoup(html, 'lxml')

    """
    这个方法的的确是很方便的帮我们定位元素，
    之前的查询中，我们只用到attrs={}字典中的一个class值。
    如果单单通过class属性来定位我们有更好的方式：css选择器：

    语法：
    soup.find_all("a", class_="xxx")
    """
    for match in soup.find_all('div', class_='matchmain bisai_qukuai'):
        # print(match)

        match_time = match.find('div', class_='whenm').text.strip()
        # print(match_time)

        team_names = match.find_all('span', class_='team_name')

        green_team = team_names[0].text.strip()
        red_team = team_names[1].text.strip()

        if green_team == "":
            green_team = "未知队伍"

        green_rate = match.find('span', class_='team_number_green').text.strip()
        red_rate = match.find('span', class_='team_number_red').text.strip()

        match_info = """比赛时间: \t{}
            {} \t胜率：{}
            {} \t胜率：{}
        """.format(match_time, green_team, green_rate, red_team, red_rate)

        print(match_info)
        sys.exit(0)


if __name__ == '__main__':
    url = 'http://dota2bocai.com/match'
    get_match(url)

"""
html = '''
<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>
'''
#可以看到，a标签下的内容是一个注释类型，但是如果我们直接输出它的话
#会输把注释符号去掉的 Elsie：

print(soup.a.string) #Elsie

#所以为了过滤掉注释类型，我们可以这样做：

if type(soup.a.string)==bs4.element.Comment:
    //TO DO
#上面通过一个简单的类型判断解决了这个问题。

"""
