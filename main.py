# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os
import time

from selenium import webdriver

def driver(imput):
    chromedriver = './webdriver/chromedriver'
    driver = webdriver.Chrome(chromedriver)
    path = 'https://dictionary.cambridge.org/'
    driver.get(path)
    # driver.minimize_window()
    searchword = driver.find_element_by_xpath('//*[@id="searchword"]')
    searchword.send_keys(imput)
    time.sleep(1)
    # get click the button
    button = driver.find_element_by_css_selector('button.cdo-search-button')
    button.click()
    # get the word from meta tag
    word = driver.find_element_by_xpath("//meta[@property='og:title']").get_attribute("content")
    time.sleep(3)
    driver.close()
    print(word)
    print('finished')

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    driver('apple')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
