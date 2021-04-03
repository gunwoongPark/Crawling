from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

chromedriver = './chromedriver.exe'
driver = None
a_href_list = []
movie_list = []

def openBrowser():
    global driver

    driver = webdriver.Chrome(chromedriver)
    driver.maximize_window()

    driver.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')

def urlCrawling():
    # url 긁어오기
    tbody = driver.find_element_by_xpath('//*[@id="old_content"]/table/tbody')

    index = 0

    while len(a_href_list) < 50:
        index+=1
        try:
            tr = tbody.find_element_by_xpath('//*[@id="old_content"]/table/tbody/tr[{}]'.format(index))
            td = tr.find_element_by_class_name("title")
            div = td.find_element_by_tag_name("div")
            a_href = div.find_element_by_tag_name("a").get_attribute("href")
            a_href_list.append(a_href)

        except NoSuchElementException:
            continue

def getMovie():
    while(a_href_list):
        try:
            page = a_href_list.pop(0)
            driver.get(page)

            h3 = driver.find_element_by_class_name("h_movie")
            title = h3.find_element_by_tag_name("a").text
            sub_title = driver.find_element_by_class_name("h_movie2").text
            story = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[4]/div[1]/div/div[1]/p').text

            movie_list.append({"title": title, "sub_title": sub_title, "story": story})
        except NoSuchElementException:
            movie_list.append({"title": title, "en_title": sub_title})


    print(movie_list)

def main():
    openBrowser()
    print("url crawling...")
    urlCrawling()
    print("get movie...")
    getMovie()


if __name__ == "__main__":
    main()