# install the required libraries:
# pip install beatifulsoup4
# pip install selenium

from bs4 import BeautifulSoup
from get_soup import get_soup

# also works for NASDAQ 100: "https://www.slickcharts.com/nasdaq100"
soup = get_soup("https://www.slickcharts.com/sp500")

# this `table-responsive` class should uniquely identify the div that contains
# our table. Note that although we do have a `<table>` tag, the real parent tag
# of the cells is `tbody` (which is a child of the `<table>` tag)
tbody = soup.find("div", {"class": "table-responsive"}).find("tbody")

SP500_symbols = []

for tr in tbody.find_all("tr"):
  # the fifth item of each `<tr>` contains a `<href>`, which then
  # contains the symbol string. Note that the third table cell is the one that
  # contains the symbol string, but the cells are delineated by newlines
  # in each `<tr>` for some reason (needs more investigation)
  SP500_symbols.append(tr.contents[5].contents[0].contents[0])

print(SP500_symbols)
