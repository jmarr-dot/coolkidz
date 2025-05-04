"""
The purpose of this scipt is to scrape the text from urls in spunikglobe's website. 

@Author: cliffbridges5

@Date: April 14, 2025
"""
import numpy as np
import pandas as pd
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

# If you want to start from a previous incomplete pull, set from_scratch to false
from_scratch = True
## JMP: is this used to loop through 250 row limit in addition to looping through failed webdriver exception,
## or is the 250 limit only for article text?

# Get urls
if from_scratch: # Create a brand new df
    df = pd.read_csv('../data/results_sputnikglobe_20201201_20211130.csv')
    df['text'] = None
    df['pull_time'] = None
    df['keywords'] = None
    df['analytics_keywords'] = None
else: # Read in the latest partial results from a previous pull
    df = pd.read_csv('/temp/sputnik_partial_results_latest.csv')

# Set sleep times
mu, sigma = 0.5, 1. # mean and standard deviation
s = np.random.lognormal(mu, sigma, df.shape[0])
## JMP: why is sleep time variable?

# Optionally plot sleep times
def plot_sleep_times(s=s):
    import matplotlib.pyplot as plt
    count, bins, ignored = plt.hist(s, 600, density=True, align='mid')

## JMP: what is the function being plotted below?
    x = np.linspace(min(bins), max(bins), 10000)
    pdf = (np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2))
        / (x * sigma * np.sqrt(2 * np.pi)))

    plt.plot(x, pdf, linewidth=2, color='r')
    plt.axis('tight')
    plt.show()
    return
if False:
    plot_sleep_times()

def refresh_driver(driver:webdriver.Firefox=None, e:Exception=None):
    """Create a (Firefox) driver, quiting the old driver if one is passed."""
    if e:
        print(f'Refreshing driver after exception {e}.')
    else:
        print('Refreshing driver.')
    if driver:
        try:
            driver.quit()
        except WebDriverException as e:
            print('No driver to quit.')
    new_driver = webdriver.Firefox()
    return new_driver

def main():
    # Initialize driver
    driver = refresh_driver()
## JMP: how often does driver have to refresh?

    # filter out the urls that have successfully been pulled already and store in temporary dataframe
    temp_df = df.loc[(df['text'].isna()) | (df['pull_time'].isna()) | (df['keywords'].isna()) | (df['analytics_keywords'].isna())]
## JMP: what is "isna"?

    # one by one, visit site, pull source, and store tags of interest in the original dataframe
    for i, row_url in enumerate(temp_df['url']):
        # Get the index of the current url
        df_index = df.loc[df['url']==row_url].index.values[0]

        # Set the pull time to now
        df.at[df_index, 'pull_time'] = time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime())

        # Try to pull the html from the url
        try:
            driver.get(row_url)
        # If page is unreachable, fill in all cells saying so, restart the driver, then skip to the next url
        except WebDriverException as e:
            df.at[df_index, 'text'] = f'[ERROR] The url is not reachable at this time.'
            df.at[df_index, 'keywords'] = f'[ERROR] The url is not reachable at this time.'
            df.at[df_index, 'analytics_keywords'] = f'[ERROR] The url is not reachable at this time.'
            driver = refresh_driver(driver=driver, e=e)
            continue

        # Convert the html into "soup" for parsing
        soup = BeautifulSoup(driver.page_source)

        # Get keywords from soup
        url_keywords = soup.find(name='meta', attrs={'name':'keywords'})
        if url_keywords:
            df.at[df_index, 'keywords'] = url_keywords['content']
        else:
            df.at[df_index, 'keywords'] = 'No keywords found.'

        # Get analytics keywords from soup
        url_analytics_keywords = soup.find(name='meta', attrs={'name':'analytics:keyw'})
        if url_analytics_keywords:
            df.at[df_index, 'analytics_keywords'] = url_analytics_keywords['content']
        else:
            df.at[df_index, 'analytics_keywords'] = 'No analytics keywords found.'

        # Get text header from soup
## JMP: can we go through a page's html together to learn how to identify these components?
        text_header = soup.find(name='div', attrs={'class':'article__announce-text'})

        # Get text body from soup
        text_body = soup.find(name='div', attrs={'class':'article__body'})

        # Join text header with text body if header exists
        if text_header:
            text = text_header.text
        else:
            text = ''
        if text_body:
## JMP: what is += ?
            text += text_body.text
        df.at[df_index, 'text'] = text

        # print progress ever 300 urls
## JMP: is 300 an arbitrary value?
        if i%300 == 0:
            print(f'{round(i/temp_df.shape[0]*100)}% of {temp_df.shape[0]} completed...')
            driver = refresh_driver(driver=driver)
        
        # As a precaution, sleep variable amount of time
## JMP: does driver time-out after going to sleep or can you "wake" (restart) a sleeping driver?
        time.sleep(s[i])
    driver.quit()

    # Save results
    #If there are missing results, save in the temp folder and report that results are missing
## JMP: how can temp folder be accessed?
    if sum(df['text'].isna()) or sum(df['pull_time'].isna()) or sum(df['keywords'].isna()):
        df.drop('Unnamed: 0', axis=1).to_csv(f'../temp/sputnik_partial_results_{time.strftime('%Y_%m_%d_%H%M%S', time.gmtime())}.csv', index=False)
        df.drop('Unnamed: 0', axis=1).to_csv(f'../temp/sputnik_partial_results_latest.csv', index=False)
        print('[WARNING] Some results were not pulled. Partial results were saved to "../temp/sputnik_partial_results_latest.csv".')
        print('Please run this script again after correcting the errors and setting "from_scratch" to False.')
    # If no results are missing, save in the data folder
    else:
        df.drop('Unnamed: 0', axis=1).to_csv(f'../data/sputnik_full_results_{time.strftime('%Y_%m_%d_%H%M%S', time.gmtime())}.csv', index=False)
        print('[SUCCESS] Results were saved to "../data/sputnik_full_results_<date>.csv".')

if __name__=='__main__':
    main()