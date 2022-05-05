# -*- coding: utf-8 -*-
"""Telus_Task1_Submission.ipynb

"""

#!pip3 install wikipedia-api

import wikipediaapi
from bs4 import BeautifulSoup
import re
import csv
import requests
import pandas as pd
from urllib.request import urlopen

wiki = wikipediaapi.Wikipedia('en')

#This function uses wikipediaapi to extract the summary directly from the url using company_name
def wikipedia_call(company_name,limit):
  summary = wiki.page(company_name).summary[0:limit]
  return summary


"""This custom function is made for those entries whose url pattern is different with the company_name. Ex: AHEAD. URL of this company is: '/wiki/AHED_(company)' 
This function also extracts the summary from the company's webpage
"""
def custom_wikipedia_call(href,limit):
  static_url = 'https://en.wikipedia.org/'
  total_url = ''
  total_url = static_url + href
  page = urlopen(total_url).read()
  soup = BeautifulSoup(page)
  total_text = ''
  for item in soup.findAll('p'):
    total_text += item.text
  
  return total_text[0:limit]

""" This function is the page parser, where it takes the entire table as an input and call the scrapper function internally to retrieve the summary of each page
It returns a dictionary in {'company_name':'summary'} format.
"""
def page_parse(table,idx,limit):
  body = table.find_all("tr")
  head = body[0]
  body_rows = body[1:] 
  dic={}
  c=0
  for row_num in range(len(body_rows)):
    c=c+1 
    row = [] 
    c3 = 0
    var = ''
    var_comp = ''
    temp_dic = {}
    for row_item in body_rows[row_num].find_all("a"):
      c3 = c3+1
      aa = re.sub("(\xa0)|(\n)|,","",row_item.text)
      if (len(aa.splitlines())>=1):
        var_comp = aa.splitlines()[0]

      var=row_item['href']
      temp_dic[var_comp] = var

    keys_list = list(temp_dic)
    company_name = keys_list[idx]

    summary = wikipedia_call(company_name,limit)

    if (summary == ""):
      summary = custom_wikipedia_call(temp_dic[company_name],limit)

    dic[company_name] = summary


  return dic

""" This is the main driver function. It calls the page_parse function internally and saves the returned data into a csv file"""
def driver():
  url='https://en.wikipedia.org/wiki/List_of_companies_of_Canada'
  limit = 300
  req=requests.get(url)
  content=req.text  
  soup=BeautifulSoup(content)
  contentTable  = soup.find_all('table', { "class" : "wikitable sortable"})
  idx_list = [1,0]
  global_dic = {'Company Name':'Summary'}
  for i in range (len(contentTable)):
    returned_dic = page_parse(contentTable[i],idx_list[i],limit)
    global_dic.update(returned_dic)
  new_path = open("Canadian_Company_Details.csv", "w")
  z = csv.writer(new_path)
  for new_k, new_v in global_dic.items():
    z.writerow([new_k, new_v])

  new_path.close()

if __name__ == '__main__':
  driver()




