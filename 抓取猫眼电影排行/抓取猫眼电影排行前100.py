# -*- coding: utf-8 -*-
# @Time     : 20:32
# @Author   : DoubleL2l
# @File     : 抓取猫眼电影排行前100.py
# @Software : PyCharm
import json
import time

import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
    'Cookie': '__mta=251444921.1616157131131.1616157271116.1616157273007.12; uuid_n_v=v1; uuid=1FDB445088AF11EB8D235D7A7A6C38165F86C9403BD14161B58AF14F6A56E0DF; _csrf=05e7094077718259659d39d4d5508fac1390efcdcf008c59ee9a270c94342570; _lx_utm=utm_source%3Dbaidu%26utm_medium%3Dorganic%26utm_term%3D%25E7%258C%25AB%25E7%259C%25BC%25E7%2594%25B5%25E5%25BD%25B1; _lxsdk_cuid=1784a78be49c8-006a06c801d7a5-5771133-144000-1784a78be49c8; _lxsdk=1FDB445088AF11EB8D235D7A7A6C38165F86C9403BD14161B58AF14F6A56E0DF; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1616157131; __mta=251444921.1616157131131.1616157139726.1616157145936.4; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1616157351; _lxsdk_s=1784a78be4a-a19-6bb-c94%7C%7C35'
}


def get_one_page(url):
    try:
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except requests.RequestException:
        return None


def parse_one_page(html):
    """解析一页的数据"""
    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',
                         re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5]+item[6]
        }


def write_to_file(content):
    """把内容写入文件"""
    with open('result.txt', 'a', encoding='utf-8') as f:
        # 转换为字符串字典形式再写入
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main(offset):
    url = 'https://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    # print(html)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    for i in range(10):
        j = i*10
        main(offset=j)
        time.sleep(1)