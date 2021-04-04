from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome('./chromedriver.exe')
driver.maximize_window()
driver.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')

# url 긁어오기
tbody = driver.find_element_by_xpath('//*[@id="old_content"]/table/tbody')

a_href_list = []
index = 0

while len(a_href_list) < 50:
    index += 1
    try:
        tr = tbody.find_element_by_xpath('//*[@id="old_content"]/table/tbody/tr[{}]'.format(index))
        td = tr.find_element_by_class_name("title")
        div = td.find_element_by_tag_name("div")
        a_href = div.find_element_by_tag_name("a").get_attribute("href")
        a_href_list.append(a_href)

    except NoSuchElementException:
        continue

# 영화 긁어오기
movie_list = []

while(a_href_list):
        try:
            page = a_href_list.pop(0)
            driver.get(page)

            h3 = driver.find_element_by_class_name("h_movie")
            title = h3.find_element_by_tag_name("a").text
            story = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[4]/div[1]/div/div[1]/p').text

            movie_list.append({"title": title, "story": story})
        except NoSuchElementException:
            movie_list.append({"title": title, "story": "줄거리가 없습니다."})

# 파일로 쓰기
f = open("인기영화.txt", 'w')
while(movie_list):
    movie = movie_list.pop(0)

    f.write("영화 제목 : {}\n줄거리 : {}\n\n".format(movie["title"], movie["story"]))