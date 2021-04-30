# install the required libraries:
# pip install beatifulsoup4
# pip install selenium

from bs4 import BeautifulSoup
from selenium import webdriver
# download the appropriate ChromeDriver
# and place it in the same directory as this script
# https://chromedriver.chromium.org/downloads
driver = webdriver.Chrome("./chromedriver.exe")
driver.get("https://www.slickcharts.com/sp500")

# wait some time so the table finishes loading (NOT rigorous)
driver.implicitly_wait(3)

soup = BeautifulSoup(driver.page_source, "html.parser")
driver.quit()

# this `table-responsive` class should uniquely identify the div that contains
# our table. Note that although we do have a `<table>` tag, the real parent tag
# of the cells is `tbody` (which is a child of the `<table>` tag)
table = soup.find("div", {"class": "table-responsive"}).find("tbody")

SP500_symbols = []

for row in table.find_all("tr"):
  # the fifth item of each `row` object contains a `<href>`, which then
  # contains the symbol string. Note that the third table cell is the one that
  # contains the symbol string, but there are two additional newline elements
  # for some reason (needs more investigation)
  SP500_symbols.append(row.contents[5].contents[0].contents[0])

print(SP500_symbols)
