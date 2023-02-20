# Parser clothes shop

This Python script allows the user to scrape product data from the clothes shop website. The script uses the BeautifulSoup library to parse the HTML of the website, and the requests library to send HTTP requests. The script also uses the fake_useragent library to generate random User-Agent headers to avoid detection.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install bs4
requests
lxml
fake_useragent

```bash
pip install bs4
pip install requests
pip install lxml
pip install fake_useragent
```

## Usage
To run the script, the user must navigate to the directory where the script is saved using the command prompt or terminal. Then, the user can enter the following command:
```python
python parser.py
```
The script will start running and will scrape data from the website. The scraped data will be saved in JSON files, with each page of the website saved in a separate file.

Note: the script is set up to scrape data from the "odezhda" category of the issaplus.com website. If the user wants to scrape data from a different category, they must modify the URL in the get_data() function.

## Disclaimer

This script is for educational purposes only. The user should be aware of the website's terms of use and should not use the script to scrape data in violation of those terms.
