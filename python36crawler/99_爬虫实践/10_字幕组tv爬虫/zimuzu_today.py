#!/usr/bin/env python
# encoding: utf-8

# python 3.6

import os
import sys
import json
import time

"""
保存网页源代码
https://www.oschina.net/question/2348825_232244
"""

from random import randint

the_date = '08-21'

# time.sleep(randint(1, 120))

# # 模拟浏览器
from selenium import webdriver

# # 设置 user-agent headers
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# # 登录发送账号密码用
from selenium.webdriver.common.keys import Keys

"""解析账号密码"""
userinfo = json.load(open('user.json', 'r', encoding='utf-8'))
account = userinfo['account']
password = userinfo['password']

"""创建 headers"""

user_agent = ["Mozilla/5.0 (Windows NT 6.1; Win64; x64)", "AppleWebKit/537.36 (KHTML, like Gecko)",
              "Chrome/60.0.3112.101 Safari/537.36"]
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36"
)

"""创建一个全局的 browser"""
browser = webdriver.PhantomJS(desired_capabilities=dcap)

cookies = [
    {'domain': 'www.zimuzu.tv', 'expires': '周三, 21 二月 2018 06:55:04 GMT', 'expiry': 1519196104, 'httponly': False,
     'name': 'CNZZDATA1254180690', 'path': '/', 'secure': False, 'value': '336740493-1503466177-%7C1503466177'}, {
        'domain': 'www.zimuzu.tv', 'expires': '周四, 23 八月 2018 06:55:04 GMT', 'expiry': 1535007304,
        'httponly': False, 'name': 'ctrip', 'path': '/', 'secure': False, 'value': 'ctrip%2F1503471304'}, {
        'domain': 'www.zimuzu.tv', 'expires': '周四, 23 八月 2018 06:55:04 GMT', 'expiry': 1535007304,
        'httponly': False, 'name': 'cps3', 'path': '/', 'secure': False, 'value': 'yhd%2F1503471304'}, {
        'domain': '.zimuzu.tv', 'expires': '周六, 21 八月 2027 06:54:56 GMT', 'expiry': 1818831296, 'httponly': True,
        'name': 'GKEY', 'path': '/', 'secure': False, 'value': '6295ace4c7385e3201d705a5d451220f'}, {
        'domain': '.zimuzu.tv', 'expires': '周六, 21 八月 2027 06:54:56 GMT', 'expiry': 1818831296, 'httponly': False,
        'name': 'GINFO', 'path': '/', 'secure': False,
        'value': 'uid%3D3939181%26nickname%3DZz5Rkwu%26group_id%3D1%26avatar_t%3Dhttp%3A%2F%2Ftu.zmzjstu.com%2Fftp%2Favatar%2Ff_noavatar_t.gif%26main_group_id%3D0%26common_group_id%3D56'},
    {
        'domain': '.zimuzu.tv', 'expires': '周三, 21 二月 2018 06:54:49 GMT', 'expiry': 1519196089, 'httponly': False,
        'name': 'UM_distinctid', 'path': '/', 'secure': False,
        'value': '15e0ddf45382-0ad9d852-373e0834-1fa400-15e0ddf4539f9'}, {'domain': 'www.zimuzu.tv',
                                                                          'httponly': False, 'name': 'PHPSESSID',
                                                                          'path': '/', 'secure': False,
                                                                          'value': 'k5o2t0etbojbtn7386j64l18g4'}]
cookie = {
             'domain': '.zimuzu.tv', 'expires': '周六, 21 八月 2027 06:54:56 GMT', 'expiry': 1818831296, 'httponly': False,
             'name': 'GINFO', 'path': '/', 'secure': False,
             'value': 'uid%3D3939181%26nickname%3DZz5Rkwu%26group_id%3D1%26avatar_t%3Dhttp%3A%2F%2Ftu.zmzjstu.com%2Fftp%2Favatar%2Ff_noavatar_t.gif%26main_group_id%3D0%26common_group_id%3D56'},


# for cookie in cookies:
#     browser.add_cookie(cookie_dict=cookie)

# browser.add_cookie(cookie_dict=cookie)


def login():
    """
    用户登录
    """
    print("浏览器初始化完毕，开始登录")
    browser.get('http://www.zimuzu.com/user/login')
    browser.implicitly_wait(3)

    """定位元素"""
    login_content = browser.find_element_by_class_name("user-login")

    a_text = login_content.find_element_by_xpath("./ul/form/li[1]/label/input")
    p_text = login_content.find_element_by_xpath("./ul/form/li[2]/label/input")
    botton = login_content.find_element_by_xpath("./ul/form/li[4]/input")

    """ 在发送账号密码的时候，不是用赋值的方式。下面这种方式是错误的
    # a_text.send_keys = account
    # p_text.send_keys = password
    """

    """清空账号输入框，输入账号"""
    a_text.clear()
    a_text.send_keys(account)

    """清空密码输入框，输入密码并重新发送密码的不可见字符
    如果使用 `p_text.send_keys(Keys.RETURN)` 则无法登陆
    """
    p_text.clear()
    p_text.send_keys(password)
    p_text.send_keys(Keys.RETURN)

    time.sleep(1)

    """模拟点击"""
    botton.submit()

    """调试信息
    <label>
        <strong>帐号</strong>
        <input type="text" class="input-txt" size="30" name="email" placeholder="輸入用戶名或者郵箱">
    </label>

    1. 在标签内的属性，应该使用 `driver.get_attribute('name')` 的方式获取值。
       例如 driver.input.get_attribute('placeholder')
    2. 在标签之间的文本属性，应该使用 `driver.text` 的方式获取值。
       例如 `driver.strong.text`

    """
    # print(login_content.find_element_by_xpath("./ul/form/li[1]/label/strong").text)
    # print('botton_value=', botton.get_attribute('value'))



    time.sleep(2)
    # browser.save_screenshot('login_after.png')

    print(" " * 2, "登录完成")

    print("cookies: ", browser.get_cookies())


def get_today():
    """抓取今日更新信息"""
    print('开始爬取今日列表')

    items = []

    """ 访问页面 """
    browser.get('http://www.zimuzu.tv/today')

    open('today.html', 'w', encoding='utf-8').write(browser.page_source)

    """等待 JS 加载时间"""
    browser.implicitly_wait(3)

    """将当前 browser 访问的页面保存为图片"""
    # browser.save_screenshot('today.png')

    # res_list = browser.find_element_by_class_name("d_r_t")
    """
    driver.find_element_by_xpath('//div/td[1]')
    """

    try:
        res_list = browser.find_element_by_xpath('//table[@class="d_r_t"]')

        print(" " * 2, "资源主体加载成功")
        # print(res_list.text)

        movies = res_list.find_elements_by_xpath('./tbody/tr[@day="{}"]'.format(the_date))

        # print(len(movies))
        print("  共有 {} 个资源更新".format(len(movies)))

        # open('res_list.html', 'w', encoding='utf-8').write(res_list.location_once_scrolled_into_view)
    except:
        print("  - ERROR: 爬去资源失败，请稍后再试")
        sys.exit(1)


        # print(movies)
    for movie in movies:

        print(movie)

        movie.screenshot('movie.png')

        print(dir(movie))
        m_dict = {}

        print("""-------------""")
        print(movie.text)
        # exit(0)
        # print("area: {}".format(movie.get_attribute('area')))
        m_area = movie.get_attribute('area')

        # print("channel: {}".format(movie.get_attribute('channel')))
        # print("format: {}".format(movie.get_attribute('format')))

        """ 以下 type 和 format 查找方式都可以"""
        m_type = movie.find_element_by_class_name('d1').text.strip()
        m_format = movie.find_element_by_class_name('d2').text.strip()

        # m_type = movie.find_element_by_xpath('./td[1]').text
        # m_format = movie.find_element_by_xpath('./td[2]').text

        m_title = movie.find_element_by_xpath('./td[3]/a').text.strip()

        m_dict['title'] = m_title
        m_dict['area'] = m_area
        m_dict['type'] = m_type
        m_dict['format'] = m_format

        print(m_title, m_type, m_format, )

        # print(m_title)
        m_dict['dl'] = []
        for a_tag in movie.find_elements_by_xpath('./td[4]/a'):
            dl_name = a_tag.text.strip()
            # dl_url = repr(a_tag.get_attribute('href')).strip("'")
            dl_url = a_tag.get_attribute('href')

            if dl_name == '驴':
                print('{} : {}'.format(dl_name, dl_url))

            m_dict['dl'].append({"dl_name": dl_name, "dl_url": dl_url})

        # print(m_type, m_format, m_title)

        # print(json.dumps(m_dict))
        items.append(m_dict)

        exit(0)
    return items


def main():
    login()
    get_today()


if __name__ == '__main__':
    main()
