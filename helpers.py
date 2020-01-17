# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 19:11:25 2020

@author: emma
"""
import pandas as pd 
from bs4 import BeautifulSoup
from urllib.parse import urlparse


# ----- Creates a new data frame ----- # 
def createTextDf(div_df):
    return div_df.applymap(lambda x: x.text)


def creatURLDf(div_df):
    return div_df.applymap(getURL)

def createBoolNameDf(text_df):
    '''return Dataframe that returns True where the appropriate congressperson's
    name is in the div text'''
    name_dict = {}
    for i, row in text_df.iterrows():
           name_dict[i] = [isNameInResult(result_text,i) for result_text in row]

    return pd.DataFrame.from_dict(name_dict, orient='index')

    
def createZipcodeDivDf(df, experiment_dir_name):
    div_dict = {}
    file_names = ['congress', 'congressperson', 'rep', 'representative']
    zips = df.zip.values
    i=0
    for z in zips: 
        div_results = [] 
        z = (5 - len(str(z))) * '0' + str(z)

        for file_name in file_names: 
            with open('results/{}/{}/{}.html'.format(experiment_dir_name, z, file_name)) as f: 
                soup = BeautifulSoup(f, 'html.parser')
            div_results.append(getFirstResult(soup))
        div_dict[z] = div_results

    return pd.DataFrame.from_dict(div_dict, orient='index', columns= file_names)


def createDiststrictDivDf(df, experiment_dir_name):
    '''create a dataframe where each representative is a row and each column is a query. 
    The cells contain the div element of the top result'''
    div_dict = {}
    file_names = ['query{}'.format(i) for i in range(1, 41)]
    ids  = df.id.values 
    
    for an_id in ids: 
        div_results = [] 

        for file_name in file_names:
            
            with open('results/{}/{}/{}.html'.format(experiment_dir_name, an_id, file_name)) as f: 
                soup = BeautifulSoup(f, 'html.parser')
                
            div_results.append(getFirstResult(soup)) #create list of dictionary items
        print(an_id, end=" ")

        div_dict[an_id] = div_results #append to dictionary 
    
    return pd.DataFrame.from_dict(div_dict, orient='index', columns= file_names) #return dataframe

### --- Processing/Analysis of Beautiful Soup elements --- #### 

def isNameInResultCD(div_text,cong_id):
    '''test if the congressperson's last name appears in the text of the result div
    if this is an analysis based on congressional district expect a string for cong_id,
    if this is an analysis based on zipcode, expect a list for cong_id'''

    last_name = d.loc[d.id == cong_id, 'last_name'].iloc[0]
    return last_name in div_text


def getFirstResult(soup):
    '''get div of first result in SERP'''
    results = soup.find_all("div", class_="ZINbbc xpd O9g5cc uUPGi")
    text = results[0].text
    if "Did you mean:" not in text and 'Images' not in text and 'Including results' not in text:
        return results[0]
    else:
        return results[1]
    
def getURL(result_div):
    href = result_div.find("a", href=True)
    if href: 
        href = href['href']
    else: 
        return -1
    if href.startswith("/url?q="):
        href =  href.split("/url?q=")[1]
    netloc = urlparse(href).netloc
    return netloc
