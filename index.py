from selenium import webdriver
import time

chromedriver = './chromedriver.exe'
driver = webdriver.Chrome(chromedriver)

driver.get('https://software.naver.com/software/fontList.nhn?categoryId=I0000000')

driver.find_element_by_xpath('//*[@id="gnb_login_button"]').click()

driver.find_element_by_xpath('//*[@id="id"]').send_keys("olympiodoros")
driver.find_element_by_xpath('//*[@id="pw"]').send_keys('park1561413@')

driver.find_element_by_xpath('//*[@id="log.login"]').click()

font_list = driver.find_element_by_xpath('//*[@id="_list"]')


input()

