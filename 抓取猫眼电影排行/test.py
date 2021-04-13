# -*- coding: utf-8 -*-
# @Time     : 21:20
# @Author   : DoubleL2l
# @File     : test.py
# @Software : PyCharm
# items = [('1', 'https://p0.meituan.net/movie/414176cfa3fea8bed9b579e9f42766b9686649.jpg@160w_220h_1e_1c', '我不是药神', '\n                主演：徐峥,周一围,王传君\n        ', '上映时间：2018-07-05', '9.', '6'),
#        ('2', 'https://p0.meituan.net/movie/8112a8345d7f1d807d026282f2371008602126.jpg@160w_220h_1e_1c', '肖申克的救赎', '\n                主演：蒂姆·罗宾斯,摩根·弗里曼,鲍勃·冈顿\n        ', '上映时间：1994-09-10(加拿大)', '9.', '5'),
#        ('3', 'https://p1.meituan.net/movie/c9b280de01549fcb71913edec05880585769972.jpg@160w_220h_1e_1c', '绿皮书', '\n                主演：维果·莫腾森,马赫沙拉·阿里,琳达·卡德里尼\n        ', '上映时间：2019-03-01', '9.', '5'),
#        ('4', 'https://p0.meituan.net/movie/609e45bd40346eb8b927381be8fb27a61760914.jpg@160w_220h_1e_1c', '海上钢琴师', '\n                主演：蒂姆·罗斯,比尔·努恩,克兰伦斯·威廉姆斯三世\n        ', '上映时间：2019-11-15', '9.', '3'),
#        ('5', 'https://p1.meituan.net/movie/ac8f0004928fbce5a038a007b7c73cec746794.jpg@160w_220h_1e_1c', '小偷家族', '\n                主演：中川雅也,安藤樱,松冈茉优\n        ', '上映时间：2018-08-03', '8.', '1'),
#        ('6', 'https://p0.meituan.net/movie/61fea77024f83b3700603f6af93bf690585789.jpg@160w_220h_1e_1c', '霸王别姬', '\n                主演：张国荣,张丰毅,巩俐\n        ', '上映时间：1993-07-26', '9.', '4'),
#        ('7', 'https://p0.meituan.net/movie/005955214d5b3e50c910d7a511b0cb571445301.jpg@160w_220h_1e_1c', '哪吒之魔童降世', '\n                主演：吕艳婷,囧森瑟夫,瀚墨\n        ', '上映时间：2019-07-26', '9.', '6'),
#        ('8', 'https://p1.meituan.net/movie/580d81a2c78bf204f45323ddb4244b6c6821175.jpg@160w_220h_1e_1c', '美丽人生', '\n                主演：罗伯托·贝尼尼,朱斯蒂诺·杜拉诺,赛尔乔·比尼·布斯特里克\n        ', '上映时间：2020-01-03', '9.', '3'),
#        ('9', 'https://p1.meituan.net/movie/6bea9af4524dfbd0b668eaa7e187c3df767253.jpg@160w_220h_1e_1c', '这个杀手不太冷', '\n                主演：让·雷诺,加里·奥德曼,娜塔莉·波特曼\n        ', '上映时间：1994-09-14(法国)', '9.', '4'),
#        ('10', 'https://p0.meituan.net/moviemachine/c2496a7290a72eac6081321898c347693550574.jpg@160w_220h_1e_1c', '盗梦空间', '\n                主演：莱昂纳多·迪卡普里奥,渡边谦,约瑟夫·高登-莱维特\n        ', '上映时间：2010-09-01', '9.', '0')]
#
# def parse_one_page(items):
#     for item in items:
#         yield {
#             'index': item[0],
#             'image': item[1],
#             'title': item[2],
#             'actor': item[3].strip()[3:],
#             'time': item[4].strip()[5:],
#             'score': item[5]+item[6]
#     }
#
# for item in parse_one_page(items):
#     print(item)
#
import json
content = {'index': '1', 'image': 'https://p0.meituan.net/movie/414176cfa3fea8bed9b579e9f42766b9686649.jpg@160w_220h_1e_1c', 'title': '我不是药神', 'actor': '徐峥,周一围,王传君', 'time': '2018-07-05', 'score': '9.6'}
print(type(content))
print(json.dumps(content))
print(type(json.dumps(content)))
with open('result.txt','a',encoding='utf-8') as f:
    print(type(json.dumps(content)))
    f.write(json.dumps(content, ensure_ascii=False))

