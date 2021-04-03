from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
import time

chromedriver = './chromedriver.exe'
driver = None
a_href_list = []

def openBrowser():
    global driver

    driver = webdriver.Chrome(chromedriver)
    driver.maximize_window()

    time.sleep(1)
    driver.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')

def urlCrawling():
    time.sleep(1)
    # url 긁어오기

    tbody = driver.find_element_by_xpath('//*[@id="old_content"]/table/tbody')
    tr = tbody.find_element_by_xpath('//*[@id="old_content"]/table/tbody/tr[2]')
    td = tr.find_element_by_class_name("title")
    div = td.find_element_by_tag_name("div")
    a_href = div.find_element_by_tag_name("a").get_attribute("href")
    print(a_href)

    print(td)

def main():
    openBrowser()
    urlCrawling()


if __name__ == "__main__":
    main()