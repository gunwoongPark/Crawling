from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
import time

chromedriver = './chromedriver.exe'
driver = None
a_href_list = []

def openBrowser():
    global driver
    if not isinstance(driver, type(None)):
        driver.close()

    driver = webdriver.Chrome(chromedriver)
    driver.maximize_window()

    time.sleep(1)
    driver.get('https://software.naver.com/software/fontList.nhn?categoryId=I0000000')
    time.sleep(1)

    # 로그인 절차
    driver.find_element_by_xpath('//*[@id="gnb_login_button"]').click()

    driver.find_element_by_xpath('//*[@id="id"]').send_keys("olympiodoros")
    driver.find_element_by_xpath('//*[@id="pw"]').send_keys('park1561413@')

    driver.find_element_by_xpath('//*[@id="log.login"]').click()
    input()

def urlCrawling():
    time.sleep(1)

    # url 긁어오기
    for index in range(0, 100):
        try:
            target = driver.find_element_by_xpath('//*[@id="slot{}"]'.format(index))
            a_href = target.find_element_by_tag_name("a").get_attribute("href")
            a_href_list.append(a_href)
        except NoSuchElementException:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)

def Download():
    # 다운로드

    while a_href_list:
        page = a_href_list.pop(0)
        try:
            time.sleep(2)
            driver.get(page)
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="_sticked_guide"]/div[1]/a').click()
            time.sleep(0.5)
            driver.find_element_by_xpath('//*[@id="showUseRangeLayerDownloadLink"]').click()
            time.sleep(0.5)
            driver.find_element_by_xpath('//*[@id="downloaderAlert"]/a[3]').click()

        # 비정상적인 접근
        except WebDriverException:
            return

def main():
    openBrowser()
    urlCrawling()

    while True:
        Download()
        if not a_href_list:
            break
        openBrowser()

if __name__ == "__main__":
    main()


