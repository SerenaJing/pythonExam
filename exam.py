# -*- coding:utf-8 -*-
###
# File: exam.py
# Project: main
# Created Date: Thursday, November 14th 2019, 15:23:04 PM
# Author: shiyujing
# -----
# Last Modified: Thursday, November 14th 2019, 15:59:56 PM
# Modified By: shiyujing
# -----
# |---------------------|
# |  LIFE IS FANTASTIC  |
# |---------------------|
# -----
# HISTORY:
# Date      	By	Comments
# ----------	---	----------------------------------------------------------
###
import requests
import re
from pyquery import PyQuery as pq

def start():


    url = "http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=石宇菁&rqlang=cn&rsv_enter=1&rsv_dl=ib&rsv_n=2&rsv_sug3=1"

    response = requests.get(url)

    doc = pq(response.text)

    containers = doc(".c-container")

    with open("result.txt", "a",encoding="utf8") as fop:
        for each in containers.items():
            title = each.find(".t").text()
            link = each.find('.t a').attr("href")
            fop.write(title + ":\t" + link + "\n")

if __name__ == "__main__":
    start()