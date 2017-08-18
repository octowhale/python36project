#!/usr/bin/env python
# encoding: utf-8

"""
@python_version: python3.6
@file: crawl_baidutieba.py
@time: 2017/8/18 10:03
"""

import os
import sys
import requests
from bs4 import BeautifulSoup


def get_html(url):
    """
    查询网页，返回 html 网页结果
    :param url:
    :return:
    """
    try:
        r = requests.get(url, timeout=30)  # 30 秒超时
        r.raise_for_status()

        r.encoding = 'utf-8'
        # 这里我们知道百度贴吧的编码是utf-8，所以手动设置的。爬去其他的页面时建议使用：
        # r.endcodding = r.apparent_endconding

        return r.text

    except:
        return "ERROR"


def get_content(url):
    """
    分析贴吧的网页文件，整理信息，保存在列表变量中
    :param url:  baidutiba_url
    :return:  dict
    """

    """ 标题与地址
    <a href="/p/5264880782" title="第一季第十集" target="_blank" class="j_th_tit ">第一季第十集</a>
    """

    """主题作者
    <span class="tb_icon_author " title="主题作者: 🐨猪猪的你" data-field="{&quot;user_id&quot;:308280638}">
        <i class="icon_author"></i>
        <span class="frs-author-name-wrap">
            <a data-field="{&quot;un&quot;:&quot;237102576&quot;}"
                class="frs-author-name j_user_card "
                href="/home/main/?un=237102576&amp;ie=utf-8&amp;fr=frs"
                target="_blank">
                <img src="//tb1.bdstatic.com/tb/cms/nickemoji/2-5.png"
                class="nicknameEmoji" style="width:13px;height:13px">猪猪的你
            </a>
        </span>
    </span>
    """

    """创建时间
    <span class="pull-right is_show_create_time" title="创建时间">8-14</span>
    """

    """回复数量
    """

    contents = []

    # 获取网页内容
    html = get_html(url)

    # open('tbbt.html', 'w', encoding='utf-8').write(html)
    # html = open('tbbt.html', 'r', encoding='utf-8').read()
    # 解析网页
    soup = BeautifulSoup(html, 'lxml')

    # 找到最上层一个的 li tag，包含每个帖子的信息
    liTags = soup.find_all('li', attrs={'class': ' j_thread_list clearfix'})

    # print(type(liTags))

    # 初始化一个字典来存储帖子信息
    comment = {}
    for li in liTags:

        try:
            # comment['title'] = li.find('a', attrs={'class': 'j_th_tit '}).test.strip()
            # comment['title'] = li.find('a', attrs={'class': 'j_th_tit '}).text.strip()
            # comment['title'] = li.find('a', attrs={'class': 'j_th_tit '}).text.strip()
            # print(li.find('a', attrs={'class': 'j_th_tit '}).text.strip())
            # print(li.find('a', attrs={'class': 'j_th_tit '}))
            # print(comment['title'])

            """采集文章标题与"""
            title_tag = li.find('a', attrs={'class': 'j_th_tit '})
            # print(title_tag)
            # print(title_tag.text.strip())
            # print(title_tag.text)  # 取 <a> 标签的文本信息，内容与 title 同。
            # print(title_tag['title'])
            # print('{}{}'.format('http://tieba.baidu.com', title_tag['href']))
            tie_title = title_tag['title'].strip()
            comment[tie_title] = {}

            comment[tie_title]['title'] = title_tag.text.strip()
            comment[tie_title]['link'] = '{}{}'.format('http://tieba.baidu.com', title_tag['href'])

            """采集作者名字"""
            """
            <a data-field="{&quot;un&quot;:&quot;237102576&quot;}"
                class="frs-author-name j_user_card "
                href="/home/main/?un=237102576&amp;ie=utf-8&amp;fr=frs"
                target="_blank">
                <img src="//tb1.bdstatic.com/tb/cms/nickemoji/2-5.png"
                class="nicknameEmoji" style="width:13px;height:13px">猪猪的你
            </a>
            """
            # author_tag = soup.find('span', attrs={'class': 'tb_icon_author '})
            # comment[tie_title]['author'] = author_tag['title'].strip()
            author_tag = soup.find('a', attrs={'class': 'frs-author-name j_user_card '})
            comment[tie_title]['author'] = author_tag.text.strip()

            """采集文章创建时间"""
            create_time_tag = soup.find('span', attrs={'class': 'pull-right is_show_create_time'})
            comment[tie_title]['create_time'] = create_time_tag.text.strip()

            """采集帖子回复数量"""
            """回复数量
            <span class="threadlist_rep_num center_text" title="回复">1</span>
            """
            reply_tag = soup.find('span', attrs={'class': "threadlist_rep_num center_text"})
            # repy_num = reply_tag.text.strip()
            comment[tie_title]['reply_num'] = reply_tag.text.strip()

            # print('{}\t{}\t{}\t{}\t{}'.format(comment[tie_title]['title']))

            # print("=========")
            result = ''
            for k in comment[tie_title]:
                # print(k)
                result += "{}\t".format(comment[tie_title][k])

            print(result)

        except Exception as e:
            print(e)

            # print(comment)
            # sys.exit(0)
            # sys.exit(0)
            # return comment


def threading_mode(url):
    import threading
    import time
    from random import randint, random
    deep = 10

    for dp in range(0, deep):
        url_tmp = "{}&pn={}".format(url, dp * 50)
        print(url_tmp)
        # time.sleep(randint(1, 3))
        time.sleep(random())

        t = threading.Thread(target=get_content, args=(url_tmp,))
        t.start()


if __name__ == "__main__":
    url = "http://tieba.baidu.com/f?kw=%E7%94%9F%E6%B4%BB%E5%A4%A7%E7%88%86%E7%82%B8&ie=utf-8"
    # get_content(url)
    threading_mode(url)
