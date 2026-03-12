\# Company Intelligence Scraper



A modular Python web scraping pipeline that extracts structured datasets from both static websites and JavaScript-rendered pages.  

The project demonstrates multi-level scraping, automated validation, and a clean data extraction workflow.



---



\## Features



\- Multi-level web scraping (category → item → details)

\- Pagination handling across multiple pages

\- Structured dataset generation

\- Automated dataset validation

\- Modular scraper architecture

\- JavaScript-rendered page scraping using Selenium

\- Clean pipeline execution



---



\## Project Structure



company\_intelligence\_scraper



scrapers  

 multi\_level\_scraper.py  

 quotes\_scraper.py  

 selenium\_scraper.py  



output  

 company\_intelligence\_dataset.csv  



run.py  

validator.py  

requirements.txt  

README.md  



---



\## Scraping Approaches



\### Static Website Scraping



Uses:



\- Requests  

\- BeautifulSoup  

\- LXML  



Capabilities:



\- multi-page navigation  

\- hierarchical data extraction  

\- structured dataset generation  



Example flow:



Category Page → Item Listing → Item Details → Dataset



---



\### JavaScript-Rendered Scraping



Modern websites often load content dynamically with JavaScript.  

The repository includes a Selenium-based scraper capable of:



\- loading JavaScript-rendered pages

\- interacting with the DOM

\- extracting rendered elements



Example flow:



Browser Automation → DOM Extraction → Structured Data



---



\## Data Pipeline



The scraping system follows a structured pipeline:



Scraper Module  

↓  

Data Extraction  

↓  

Dataset Generation  

↓  

Validation Checks  

↓  

Structured Output



Running the pipeline automatically performs both extraction and validation.



---



\## Dataset Schema



The generated dataset contains the following fields:



category – item category  

title – item title  

price – item price  

availability – stock availability  

rating – item rating  

book\_url – source page URL  



Example dataset:



Rows: 163  

Columns: 6



---



\## Data Validation



After extraction, the dataset is automatically validated for:



\- missing values

\- duplicate rows

\- column integrity

\- dataset size

\- sample preview



Example validation result:



Rows: 163  

Missing values: 0  

Duplicate rows: 0



---



\## Proxy Support



The scraper architecture supports proxy configuration through request settings or environment variables.



Example:



requests.get(url, proxies=proxy\_config)



This allows integration with scraping proxy providers such as Apify.



---



\## Technologies Used



Python  

Requests  

BeautifulSoup  

Pandas  

LXML  

Selenium  

Git  



---



\## Installation



Clone the repository:



git clone https://github.com/onyinyechi3/company-intelligence-scraper.git



Install dependencies:



pip install -r requirements.txt



---



\## Running the Pipeline



Execute the full scraping workflow:



python run.py



The pipeline will:



1\. Scrape hierarchical website data  

2\. Generate a structured dataset  

3\. Run dataset validation checks  



---



\## Output



The resulting dataset is stored in:



output/company\_intelligence\_dataset.csv



---



\## Purpose of the Project



This project demonstrates the ability to:



\- build modular scraping architectures  

\- extract structured datasets from websites  

\- handle dynamic JavaScript-rendered content  

\- implement automated data validation pipelines  

\- design reproducible data extraction workflows

