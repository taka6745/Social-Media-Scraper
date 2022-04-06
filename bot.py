from cgi import print_arguments
from os import kill
from selenium import webdriver
import time
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import ui
from webdriver_manager.chrome import ChromeDriverManager
#import pyautogui


class Instagrambot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.base = 'https://m.facebook.com/'
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        #self.driver = webdriver.Chrome('chromedriver.exe')
        #self.driver = webdriver.Edge('msedgedriver.exe')
        #self.driver = webdriver.Firefox('geckodriver.exe')
        self.login()

    def login(self):
        for i in range(3):
            print("\n")

        self.driver.get('{}login'.format(self.base))
        time.sleep(3)
        self.driver.find_element(
            by=By.XPATH, value='//*[@id="m_login_email"]').send_keys(self.username)

        self.driver.find_element(
            by=By.XPATH, value='//*[@id="m_login_password"]').send_keys(self.password)
        # self.driver.find_element_by_tag_name('body').send_keys(Keys.RETURN)
        self.driver.find_element(
            by=By.XPATH, value='//*[@id="login_password_step_element"]/button').click()

    def nav_user(self, userinput):
        time.sleep(2)
        self.driver.get('{}{}/'.format(self.base, userinput))

    def scroll(self):

        # try:

        time.sleep(3)
        for i in range(5):
            time.sleep(1)
            self.driver.find_element(
                by=By.TAG_NAME, value='body').send_keys(Keys.END)

        links = self.driver.find_elements(by=By.CLASS_NAME, value='_5msj')
        f = open('{}_links.txt'.format(userinput), "a")
        for i in links:
            f.write(str(i.get_attribute('href')))
            f.write("\n")
        f.close()
        self.likes()
        # except:
     #   pass

    def likes(self):

        # try:
        posts = open('{}_links.txt'.format(userinput), 'r')
        for line in posts:
            self.driver.get(line)
            for i in range(3):
                time.sleep(1)
                self.driver.find_element(
                    by=By.TAG_NAME, value='body').send_keys(Keys.END)
            clickable = self.driver.find_elements(
                by=By.CLASS_NAME, value='_4ayj')
            for i in clickable:
                i.click()
            for i in range(3):
                time.sleep(1)
                self.driver.find_element(
                    by=By.TAG_NAME, value='body').send_keys(Keys.END)
            try:
                commentornames = self.driver.find_elements(
                    by=By.TAG_NAME, value='a')
                commentorname = []
                for i in range(len(commentornames)-1):
                    commentorname.append(commentornames[i].text)

                commentfile = open("{}_comment.txt".format(userinput), 'a')
                for commentor in range((len(commentorname)-1)):
                    number = False
                    banned = ["Like", "Labor For Fisher", "LEARN MORE", ' ', '',
                              "Reply", "More", "Share", "Comment", " View more comments…"]
                    for i in range(len(banned)-1):
                        if commentorname[commentor] == banned[i]:
                            number = True
                    for letter in commentorname[commentor]:

                        if number == False:
                            if ord(letter) <= 64 and letter != " " and letter != "-" and letter != "'":
                                number = True

                                break

                    if number == False:
                        commentfile.write(
                            str(commentorname[commentor]) + "\n")
                commentfile.close()

            except:
                print("ERROR: Probably no comments")

            likebutton = self.driver.find_element(
                by=By.CLASS_NAME, value='_45m8').get_attribute('href')
            self.driver.get(likebutton)
            for i in range(10):
                time.sleep(0.5)
                self.driver.find_element(
                    by=By.TAG_NAME, value='body').send_keys(Keys.END)
                try:
                    self.driver.find_element(
                        by=By.XPATH, value='//*[@id="reaction_profile_pager"]/a').click()
                except:
                    pass

            names = self.driver.find_elements(by=By.TAG_NAME, value='span')
            namefile = open("{}_likes.txt".format(userinput), 'a')
            for name in range(0, (len(names)-1), 2):
                number = False
                trycast = 0

                for letter in names[name].text:

                    try:

                        if number == False:
                            if ord(letter) <= 64 and letter != " " and letter != "-" and letter != "'":
                                number = True

                                break
                    except:
                        pass
                if number == False:
                    namefile.write(str(names[name].text) + "\n")
            namefile.close()
            time.sleep(1)

            # #try:
            # if(True):
            #     self.driver.get(line)
            #     for i in range(3):
            #         time.sleep(1)
            #         self.driver.find_element(
            #             by=By.TAG_NAME, value='body').send_keys(Keys.END)
            #     sharebutton = self.driver.find_elements(
            #         by=By.CLASS_NAME, value='_43lx _55wr')
            #     print(sharebutton[0])

            #     time.sleep(100)
            #     self.driver.get(sharebutton)
            #     for i in range(10):
            #         time.sleep(0.5)
            #         self.driver.find_element(
            #             by=By.TAG_NAME, value='body').send_keys(Keys.END)

            #     sharenames = self.driver.find_elements_by_tag_name('span')
            #     sharefile = open("{}_shares.txt".format(userinput), 'a')
            #     for name in range(0, (len(sharenames)-1), 2):
            #         number = False
            #         for letter in sharenames[name].text:

            #             try:

            #                 if number == False:
            #                     if ord(letter) <= 64 and letter != " " and letter != "-" and letter != "'":
            #                         number = True

            #                         break
            #             except:
            #                 pass
            #         if number == False:
            #             sharefile.write(str(sharenames[name].text) + "\n")
            #     sharefile.close()
            #     time.sleep(1)
            #     # except:
            #     #     print("ERROR: Probably no share button")

            # # except:
            #     pass

        posts.close()


if __name__ == '__main__':
    userinput = "laborforfisher"
    ig_bot = Instagrambot('takamundy@gmail.com', 'Lollyman2002!@#')
    time.sleep(2)
    ig_bot.nav_user(userinput)
    ig_bot.scroll()
