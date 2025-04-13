"""
This file is intended be used to parse the results files in `data/` and create a csv with the required outputs.

@Author: cliffbridges5

@Date: April 6, 2025
"""
import glob
import pandas as pd
from bs4 import BeautifulSoup

def get_attr_from_tag(content, attribute:str)->str:
    if isinstance(content, str):
        tag = BeautifulSoup(content, 'html.parser').b
    else:
        tag = content
    return tag[attribute]

def clean_title(title:str)->str:
    cleaned = title.replace('&amp;', '&')
    return cleaned

def get_date_from_tag(content)->str:
    attr_val = get_attr_from_tag(content, attribute='href')
    date = attr_val.split('/')[1]
    return date

def get_url_from_tag(content)->str:
    attr_val = get_attr_from_tag(content, attribute='href')
    local_path = attr_val
    url = 'https://sputnikglobe.com' + local_path
    return url

def get_title_from_tag(content)->str:
    attr_val = get_attr_from_tag(content, attribute='title')
    title = clean_title(attr_val)
    return title

def main():
    # Get the filepaths that contain the results
    results_paths = glob.glob(pathname='../data/results_*.txt')

    # Set structure for output data
    data_dict = {'date':[], 'url':[], 'title':[]}
    for result_path in results_paths:
        with open(file=result_path, mode='r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read())
        results = soup.find_all(name='a', attrs={'href':True, 'title':True, 'class':False})
        for result in results:
            data_dict['date'].append(get_date_from_tag(result))
            data_dict['url'].append(get_url_from_tag(result))
            data_dict['title'].append(get_title_from_tag(result))
    
    # Convert data from dict to pandas dataframe then write as csv
    # NOTE: pandas is not necessary here, this was just a matter of convenience
    df = pd.DataFrame(data_dict)
    df.to_csv('../data/results_sputnikglobe_20201201_20211130.csv', index=False)