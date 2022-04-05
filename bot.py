from multiprocessing.sharedctypes import Value
from selenium import webdriver
import os
import time
import random
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import ui
from webdriver_manager.chrome import ChromeDriverManager


global odds
odds = 110


class Instagrambot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.base = 'https://m.facebook.com/'
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

        self.login()

    def login(self):
        for i in range(10):
            print("\n")
        self.driver.get('{}/login'.format(self.base))
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="m_login_email"]').send_keys(self.username)

        self.driver.find_element_by_xpath(
            '//*[@id="m_login_password"]').send_keys(self.password)

        self.driver.find_element_by_xpath(
            '//*[@id="login_password_step_element"]/button').click()
        time.sleep(5)
        self.driver.get(self.base)

        # you can find the like button using class name too

    def nav_user(self, user):

        self.driver.get('{}/{}/'.format(self.base, user))

    def scroll(self):

        try:

            time.sleep(2)
            for i in range(10):
                time.sleep(1)
                self.driver.find_element_by_tag_name(
                    'body').send_keys(Keys.END)

            links = self.driver.find_elements_by_class_name('_5msj')
            f = open("links.txt", "a")
            for i in links:
                f.write(str(i.get_attribute('href')))
                f.write("\n")
            f.close()
            print("finished \n\n\n\n\n\n\n\n\n")
        except:
            pass


if __name__ == '__main__':
    userinput = "laborforfisher" #input('What user to follow all of their followers: ')
    ig_bot = Instagrambot('takamundy@gmail.com', 'Taka6745!')
    time.sleep(2)
    ig_bot.nav_user(userinput)
    ig_bot.scroll()
