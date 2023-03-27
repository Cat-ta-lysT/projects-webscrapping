import requests
from bs4 import BeautifulSoup
import mysql.connector

# Set up database connection
mydb = mysql.connector.connect(
  host="localhost",
  user="username",
  password="password",
  database="database_name"
)


mycursor = mydb.cursor()

# Send request to website and parse HTML
url = "https://example.com"

try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Error requesting data:", e)
    exit()

try:
    soup = BeautifulSoup(response.text, "html.parser")
except Exception as e:
    print("Error parsing HTML:", e)
    exit()

# Extract data from HTML.
data = []
for item in soup.find_all("div", {"class": "item"}):
    try:
        title = item.find("h2").text.strip()
        description = item.find("p").text.strip()
        data.append((title, description))
    except Exception as e:
        print("Error extracting data:", e)

# Save data in databases
if data:
    try:
        sql = "INSERT INTO items (title, description) VALUES (%s, %s)"
        mycursor.executemany(sql, data)
        mydb.commit()
        print(mycursor.rowcount, "records inserted.")
    except mysql.connector.Error as e:
        print("Error saving data to database:", e)
else:
    print("No data to save.")
