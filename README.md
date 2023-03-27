# Web Scraper for Extracting Data and Saving to MySQL Database
This is a basic Python code for a web scraper that extracts data from a website and saves it in a MySQL database. This code is for educational purposes only and should not be used for any commercial purposes.

## Requirements
- Python 3.6+
- MySQL server and client installed
## Required Python libraries:
- requests
- beautifulsoup4
- mysql-connector-python



## Usage

### Clone this repository or download the code.

Install the required Python libraries by running the following command in the terminal:

``` pip install requests beautifulsoup4 mysql-connector-python ```

### Open the main.py file and edit the following variables according to your requirements:

url = 'https://example.com'
database = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'example_database'
}


### Run the scraper by running the following command in the terminal:

``` python scraper.py ```

### The data will be extracted from the specified website and saved to the specified MySQL database.
