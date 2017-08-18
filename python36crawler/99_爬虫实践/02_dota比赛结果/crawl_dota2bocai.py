#!/usr/bin/env python
# encoding: utf-8

# pthon 3.6

import os
import sys
import requests
from bs4 import BeautifulSoup

ENCODING = 'utf-8'


def get_html(url):
    r = requests.get(url, timeout=30)
    r.raise_for_status()

    # r.encoding = ENCODING
    r.encoding = r.apparent_encoding
    html = r.text

    # print(html)

    open('dota2match.html', 'w', encoding=ENCODING).write(html)
    return html


def get_match_result(url):
    """
    生成 dota2 比赛信息

    :param url: url
    :return:
    """

    """
    # html = open('dota2match.html', 'r', encoding='gbk').read()

    python 读取文件时报错UnicodeDecodeError: 'gbk' codec can't decode byte 0x80 in position 205: illegal multibyte sequence

    解决办法1.
    FILE_OBJECT= open('order.log','r', encoding='UTF-8')
    解决办法2.
    FILE_OBJECT= open('order.log','rb')
    """

    # html = open('dota2match.html', 'r', encoding='utf-8').read()
    # html = open('dota2match.html', 'rb').read()

    """从网页读取数据"""
    html = get_html(url)

    soup = BeautifulSoup(html, 'lxml')

    match_tags = soup.find_all('div', attrs={'class': 'matchmain bisai_qukuai'})
    # print(match_tags)

    """比赛时间
    <div class="whenm">比赛延时</div>
    """

    for match in match_tags:
        # print(match)

        """获取比赛时间"""
        match_time = match.find('div', attrs={'class': "whenm"}).text.strip()
        # print(match_time)

        # right_team = match.find('div', attrs={'style': 'width: 36%; float: left; text-align: right'})
        # right_team_name = right_team.find('span', attrs={'class': 'team_name'}).text.strip()
        # right_team_zhichi = right_team.find('div', attrs={'class': 'zhichilv1'})
        #
        # zhichi1 = right_team_zhichi.span.text.strip()
        # zhichi2 = right_team_zhichi.span.text.strip()
        #
        # if len(right_team_name) != 0:
        #     print(right_team_name)
        # else:
        #     print("name nil")
        # print(zhichi1, zhichi2)

        """获取队伍信息"""
        left_teamname, left_zhichi1, left_zhichi2 = team_info(match, 'left')
        right_teamname, right_zhichi1, right_zhichi2 = team_info(match, 'right')

        # print(left_teamname, right_teamname)

        match_info2 = """比赛时间：\t{}
        \t{} <- 队伍名称 -> {}
        \t{} <- 物品支持 -> {}
        \t{} <- 积分支持 -> {}
        """.format(match_time,
                   left_teamname, right_teamname,
                   left_zhichi1, right_zhichi1,
                   left_zhichi2, right_zhichi2)

        print(match_info2)
        # sys.exit(0)


def team_info(match, team_side):
    """
    队伍信息结构一下，只有左右之分
    :param match:   html
    :param team_side:   left,right
    :return: teamname, zhichi1, zhichi2
    """
    if team_side == 'right':
        zhichilv = 'zhichilv1'
    if team_side == 'left':
        zhichilv = 'zhichilv2'

    team = match.find('div', attrs={'style': 'width: 36%; float: left; text-align: {}'.format(team_side)})
    team_name = team.find('span', attrs={'class': 'team_name'}).text.strip()

    if len(team_name) == 0:
        team_name = 'nil'

    team_zhichi = team.find('div', attrs={'class': '{}'.format(zhichilv)})

    zhichi1 = team_zhichi.span.text.strip()
    zhichi2 = team_zhichi.span.text.strip()

    return team_name, zhichi1, zhichi2


if __name__ == '__main__':
    url = 'http://dota2bocai.com/match'
    get_match_result(url)
    # get_html(url)
