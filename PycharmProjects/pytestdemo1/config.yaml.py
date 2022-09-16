# -*- coding: utf-8 -*-
# @Time : 2022/7/18 13:49
# @Author : joel
# @Email : 770546904@qq.com
# @File : config.yaml.py
# - name: $csv{name}
#   base_url: ${get_base_url(base_gzh_url)}
#   parameters:
#     name-appid-secret-grant_type-assert_str: data/get_token.csv
#   request:
#     method: get
#     url: http:11111?token=${get_extract_data(token)}
#     params:
#       "appid": $csv{appid}
#       "secret": $csv{secret}
#       "grant_type": $csv{grant_type}
#     #json表达式提取，正则表达式提取和json提取
#     extract:
#       token: '"token":"(.*?)"'
#
#   validate:
#   -   equals: {status_code: 200}
#   -   contains: $csv{assert_str}
# #
# #
# - name:test_batch_create
#   base_url: ${get_base_url(base_gzh_url)}
#   request:
#     method: post
#     url: http:11111?token=${get_extract_data(token)}
#     files:
#       media: "E:\\shu.png"
#   validate:
#   -   equals: {status_code: 200}
#   -    contains: url