from selenium import webdriver
import pytest
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary



@pytest.fixture(scope="function")
def start_browser(request):
	binary = FirefoxBinary('/Users/Paul/Downloads/geckodriver')
	driver = webdriver.Firefox(firefox_binary = binary)
	return driver



#driver = webdriver.Chrome('/usr/local/bin/chromedriver')
#driver = webdriver.Chrome('/chromedriver')
#driver.get("http://www.imdb.com"