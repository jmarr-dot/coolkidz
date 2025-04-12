# coolkidz

This repository is used to collect US-published articles about vaccines. 
Articles are restricted to pushing date from December 1, 2020 through November 30, 2021.

## Sputnik News

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

## Install

Python 3.12.3

Create a virtual environment
- `python -m venv .venv`

Activate the virtual environment
- in git bash `source .venv/Scripts/activate`
- in windows powershell `.venv/Scripts/activate`
- in mac  `source venv/bin/activate`

Install requirements
- `pip install -r requirements.txt`

Deactivate the environment as needed
- `deactivate`