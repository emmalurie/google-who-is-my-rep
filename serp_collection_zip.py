# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 18:51:01 2020

@author: emma
"""
import requests
import os
import pandas as pd
import time
import sys

def writefile(path_to_write, filename, data):
    with open('{}/{}'.format(path_to_write, filename),'wb') as f: 
        f.write(data)


d = pd.read_excel('data/zip_queries.xlsx')
d = d.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

zip_query_name_dict = {0: 'rep', 1: 'representative', 2: 'congress', 3: 'congressperson'}
x = 0
for i, row in d.set_index('zip').iterrows():
    z = (5 - len(str(i))) * '0' + str(i)
    path_to_file = 'results/3_9_zipcode/{}'.format(z)
    
    #make sure folder exists for that zipcode
    if not os.path.isdir(path_to_file):
        os.makedirs(path_to_file)
    
    if len(os.listdir(path_to_file)) < 4: #folder mu
        
        for j in range(len(row.values)):
            r = requests.get("https://www.google.com/search?q={}".format(row.values[j]))
            serp_source = r.content
            if len(serp_source) <= 3000: 
                print('uhoh')
                sys.exit()
            else:
                writefile(path_to_file, zip_query_name_dict[j] + '.html', serp_source)
            time.sleep(1)
        time.sleep(3)
        x+=1
        if x % 100 == 0: 
            print(x,)
