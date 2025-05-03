# coolkidz

This repository is used to collect US-published articles about vaccines. 
Articles are restricted to pushing date from December 1, 2020 through November 30, 2021.

## Getting Started

### Install

Create a virtual environment
- `python -m venv .venv`

Activate the virtual environment
- in git terminal `source .venv/Scripts/activate`
- in windows terminals `.venv/Scripts/activate`
- in mac terminal `source .venv/bin/activate`

Install requirements
- `pip install -r requirements.txt`

Deactivate the environment as needed
- `deactivate`

Note that Python 3.12.3 was used in this repo. 
Much older versions are probably sufficient.

### Running the Scraper

1. Open `code/get_full_sputnik_results.py`. 
2. Set `from_scratch` to `True` or `False`:
    - Set `from_scratch` to `True` if you want to try to pull all urls from scratch. 
    - Set `from_scratch` to `False` if you want to continue an earlier pull with partial results.
3. In a terminal window, run `python code/get_full_sputnik_results.py`.
4. Final resuults will be saved to `../data/sputnik_full_results_<date>.csv`

## Background on Sputnik News

[sputnikglobe.com](https://sputnikglobe.com/search/?query=vaccine)

On March 22, a search using the keyword 'vaccine' returns 4505 results in the time range 
we are investigating (and 9180 total). 
It is unclear how many of the results are articles and how many are podcasts or other 
media.
This search lists tags that may help to filter the results.

potential tags
- keyword: 'Vaccine'
- keyword: 'vaccine'
- product: 'vaccine'
- tag: 'vaccine'
- 'vaccine-hestitancy'
- common: 'vaccine-mandate'
- tag: 'flu_vaccine'
- product: 'Ebola_vaccine'

Filtering by tag and keyword gives many results. 
These results were returned on March 16, 2025. 
Note:
- Results may include articles and other media (e.g., podcasts)
- The results across keywords may be duplicated. 
- It is unclear why the tags with the same name give different results, 
there appears to be multiple types of tags. 
- These results appear to include articles not about the US; 
they may still all be published in the US. 

| tag | count |
|-----|-------|
| vaccine | 449 |
| Vaccine | 327 |
| vaccine | 307 |
| vaccine | 182 |
| Vaccines | 150 |
| vaccines | 202 |
| vaccination | 478 |
| vaccinations | 79 |
| vaccine hesitancy | 15 | 
| Vaccination Legislation | 0 |
| anti-vaccination | 19 |
| Joint Committee on Vaccination and Immunisation (JCVI) | 1 |
| Russian Introduces First Coronavirus Vaccine | 2 |
| low-quality vaccine | 2 |