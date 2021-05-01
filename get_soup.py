from bs4 import BeautifulSoup
from selenium import webdriver

def get_soup(url):
  driver = webdriver.Chrome("./chromedriver.exe")
  driver.get(url)

  # wait some time so the table finishes loading
  # commented out because it seems redundant (it seems the opened
  # window from ChromeDriver won't be closed until the page gets
  # fully loaded)
  # driver.implicitly_wait(5)

  soup = BeautifulSoup(driver.page_source, "html.parser")
  driver.quit()

  return soup
