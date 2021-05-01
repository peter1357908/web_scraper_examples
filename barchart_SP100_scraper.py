# install the required libraries:
# pip install beatifulsoup4
# pip install selenium

from bs4 import BeautifulSoup
from get_soup import get_soup

soup = get_soup("https://www.barchart.com/stocks/indices/sp/sp100")

# the second `<table>` should have what we want
# TODO: find out how to search for an attribute with an object as
# value
tbody = soup.find_all("table")[1].find("tbody")

SP100_symbols = []

for tr in tbody.find_all("tr"):
  # the first `<td>` of each `<tr>` contains a `<div>` as the second elements
  # (the first element is, again, for some reason, a newline character)
  # whose second `<span>` contains an `<a>` which contains our string...
  # the HTML source has A LOT OF redundant comments that bs4 considers also
  # as elements, which is really a nuisance...
  td = tr.find("td")
  div = td.contents[1]
  target_span = div.find_all("span")[1]
  symbol_string = target_span.find("a").contents[0]

  SP100_symbols.append(symbol_string)

print(SP100_symbols)

