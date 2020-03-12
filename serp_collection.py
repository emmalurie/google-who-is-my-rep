# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 11:51:00 2020

@author: emma
"""

import requests
import os
import pandas as pd
import time
from lxml.html import fromstring
from itertools import cycle
import traceback

def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            #Grabbing IP and corresponding PORT
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies

def writefile(path_to_write, filename, data):
    with open('{}/{}'.format(path_to_write, filename),'wb') as f: 
        f.write(data)

def collect_cd_queries(d, exp_name):
# =============================================================================
#     proxies = get_proxies()
#     proxy_pool = cycle(proxies)
#     proxy = next(proxy_pool)
# =============================================================================

    for ID in d.id:
        
        path_to_file = 'results/{}/{}'.format(exp_name, ID)
        
        #     #make sure folder exists for that ID
        if not os.path.isdir(path_to_file):
            os.makedirs(path_to_file)
        if len(os.listdir(path_to_file)) < 40: #folder mu
            time.sleep(5)
        
    #     #make sure folder exists for that ID
    
        
            for i in range(1, 41):
                query_column = 'query{}'.format(i)
                q = d.loc[d.id == ID, query_column].item()
                r = requests.get("https://www.google.com/search?q={}".format(q))#, proxies={"http": proxy, "https": proxy})
                serp_source = r.content
                writefile(path_to_file, query_column + '.html', serp_source)
                time.sleep(0.5)

        print(ID)
    print("Done with CA data collection")
    
#
d = pd.read_excel('data/queries.xlsx')
d = d.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
#
ca = d[d.state == 'CA']
#
#    
collect_cd_queries(ca, '1_16_NY')
##### Zip Queries
#
#d = pd.read_excel('data/zip_queries.xlsx')
#d = d.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
#
#zip_query_name_dict = {0: 'rep', 1: 'representative', 2: 'congress', 3: 'congressperson'}
#x = 0
#for i, row in d.set_index('zip').iterrows():
#    z = (5 - len(str(i))) * '0' + str(i)
#    path_to_file = 'results/1_14_zipcode/{}'.format(z)
#    
#    #make sure folder exists for that zipcode
#    if not os.path.isdir(path_to_file):
#        os.makedirs(path_to_file)
#    
#    if len(os.listdir(path_to_file)) < 4: #folder mu
#        
#        for j in range(len(row.values)):
#            r = requests.get("https://www.google.com/search?q={}".format(row.values[j]))
#            serp_source = r.content
#            writefile(path_to_file, zip_query_name_dict[j] + '.html', serp_source)
#        time.sleep(5)
#    x+=1
#    if x % 100 == 0: 
#        print(x,)



