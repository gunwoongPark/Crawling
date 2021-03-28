from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

chromedriver = './chromedriver.exe'
driver = webdriver.Chrome(chromedriver)

driver.maximize_window()

driver.get('https://software.naver.com/software/fontList.nhn?categoryId=I0000000')

# 로그인 절차
# driver.find_element_by_xpath('//*[@id="gnb_login_button"]').click()
#
# driver.find_element_by_xpath('//*[@id="id"]').send_keys("olympiodoros")
# driver.find_element_by_xpath('//*[@id="pw"]').send_keys('park1561413@')
#
# driver.find_element_by_xpath('//*[@id="log.login"]').click()
# input()

a_href_list = []

time.sleep(1)

for index in range(0, 100):
    try:
        target = driver.find_element_by_xpath('//*[@id="slot{}"]'.format(index))
        a_href = target.find_element_by_tag_name("a").get_attribute("href")
        a_href_list.append(a_href)
        print(a_href)
    except NoSuchElementException as error:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

print(a_href_list)

