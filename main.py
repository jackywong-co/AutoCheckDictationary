# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os
import time

from selenium import webdriver

def driver(imput):
    chromedriver = './webdriver/chromedriver'
    driver = webdriver.Chrome(chromedriver)
    driver.get('https://dictionary.cambridge.org/')
    driver.minimize_window()
    searchword = driver.find_element_by_xpath('//*[@id="searchword"]')
    searchword.send_keys(imput)
    # driver.implicitly_wait(5)
    time.sleep(1)
    button = driver.find_element_by_css_selector('button.cdo-search-button')
    button.click()
    # word = driver.find_element_by_link_text(imput).text
    # word = driver.find_element_by_css_selector('span.').text
    word = driver.find_element_by_xpath("//meta[@name='og:title']").text
    time.sleep(5)
    driver.close()
    print(word)
    # print(imput)
    print('finished')
    # return word


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    driver('apple')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
