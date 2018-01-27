#!/usr/bin/python
# encoding: utf-8
# -*- coding: utf8 -*-
"""
Created by PyCharm.
File:               Progress_bar
User:               firefoxhome
Create Date:        2018/1/24
Create Time:        12:40
Theme:              Progress bar display
 """
import requests
import progressbar
import requests.packages.urllib3
 
requests.packages.urllib3.disable_warnings()
 
url = "https://raw.githubusercontent.com/racaljk/hosts/master/hosts"
 
response = requests.request("GET", url, stream=True, data=None, headers=None)
 
save_path = "/home/factory/hosts"
 
total_length = int(response.headers.get("Content-Length"))
with open(save_path, 'wb') as f:
    # widgets = ['Processed: ', progressbar.Counter(), ' lines (', progressbar.Timer(), ')']
    # pbar = progressbar.ProgressBar(widgets=widgets)
    # for chunk in pbar((i for i in response.iter_content(chunk_size=1))):
    #     if chunk:
    #         f.write(chunk)
    #         f.flush()
 
    widgets = ['Progress: ', progressbar.Percentage(), ' ',
               progressbar.Bar(marker='#', left='[', right=']'),
               ' ', progressbar.ETA(), ' ', progressbar.FileTransferSpeed()]
    pbar = progressbar.ProgressBar(widgets=widgets, maxval=total_length).start()
    for chunk in response.iter_content(chunk_size=1):
        if chunk:
            f.write(chunk)
            f.flush()
        pbar.update(len(chunk) + 1)
    pbar.finish()
