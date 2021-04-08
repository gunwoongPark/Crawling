from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

chromedriver = './chromedriver.exe'
driver = None
a_href_list = []
food_list = []

def openBrowser():
    global driver

    driver = webdriver.Chrome(chromedriver)
    driver.maximize_window()

    driver.get('https://haemukja.com/recipes?utf8=%E2%9C%93&category_group2%5B%5D=60&category_group2%5B%5D=70&category_group2%5B%5D=74')

def urlCrawling():
    cur_page = 1

    # while True:
    try:
        paging = driver.find_element_by_class_name("paging")
        page_url = paging.find_element_by_link_text(str(cur_page)).get_attribute("href")
        driver.get(page_url)
        time.sleep(1)

        for index in range(1, 6):
            recipe_list = driver.find_element_by_class_name("lst_recipe")
            recipe = recipe_list.find_element_by_xpath(
                '//*[@id="content"]/section/div[2]/div/ul/li[{}]'.format(index))
            span = recipe.find_element_by_class_name("judge")
            judge = span.find_element_by_tag_name("strong").text
            if (float(judge) < 2.5):
                continue
            a_href = recipe.find_element_by_tag_name("a").get_attribute("href")
            a_href_list.append(a_href)

        cur_page+=1

    except NoSuchElementException:
        pass
            # break

def getRecipe():

    while(a_href_list):
        page = a_href_list.pop(0)
        driver.get(page)

        # 요리명 긁기
        dish = driver.find_element_by_xpath('//*[@id="modal-content"]/div/div[1]/section[1]/div/div[1]/h1/strong').text

        # 재료 긁기
        lst_ingrd = driver.find_element_by_class_name("lst_ingrd")
        index = 1
        while True:
            try:
                li = lst_ingrd.find_element_by_xpath('//*[@id="modal-content"]/div/div[1]/section[1]/div/div[3]/ul/li[{}]'.format(index))
                ingrd = li.find_element_by_tag_name('span').text

                index += 1
            except NoSuchElementException:
                break

        food_list.append({"dish":dish, "ingrd":ingrd})






def main():
    openBrowser()
    print("url crawling...")
    urlCrawling()
    print("get url...")
    getRecipe()
    print("get recipe...")


if __name__ == "__main__":
    main()