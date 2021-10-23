import numpy as np # linear algebra
import pandas as pd # pandas for dataframe based data processing and CSV file I/Oimport requests # for http requests
from bs4 import BeautifulSoup # for html parsing and scraping
import bs4
from fastnumbers import isfloat 
from fastnumbers import fast_float
from multiprocessing.dummy import Pool as ThreadPool 
import requests

import matplotlib.pyplot as plt
import seaborn as sns
import json
from tidylib import tidy_document # for tidying incorrect html
from IPython.core.display import HTML

# sns.set_style('whitegrid')
# %matplotlib inline
# from IPython.core.interactiveshell import InteractiveShell
# InteractiveShell.ast_node_interactivity = "all"

def ffloat(string):
    if string is None:
        return np.nan
    if type(string)==float or type(string)==np.float64:
        return string
    if type(string)==int or type(string)==np.int64:
        return string
    return fast_float(string.split(" ")[0].replace(',','').replace('%',''),
                      default=np.nan)

def ffloat_list(string_list):
    return list(map(ffloat,string_list))

url = "https://dmarket.com/ingame-items/item-list/csgo-skins"
response = requests.get(url, timeout=240)
# response.status_code
page_content = BeautifulSoup(response.content, "html.parser")
print(HTML("<b>Rendered HTML</b>"))
print(HTML(str(page_content.find("h1"))))