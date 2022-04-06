from selenium import webdriver
import time
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import ui
from webdriver_manager.chrome import ChromeDriverManager


class Instagrambot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.base = 'https://m.facebook.com/'
        #self.driver = webdriver.Chrome(ChromeDriverManager().install())
        #self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver = webdriver.Edge('msedgedriver.exe')
        #self.driver = webdriver.Firefox('geckodriver.exe')
        self.login()

    def login(self):
        for i in range(2):
            print("\n")
        self.driver.get('{}login'.format(self.base))
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="m_login_email"]').send_keys(self.username)

        self.driver.find_element_by_xpath(
            '//*[@id="m_login_password"]').send_keys(self.password)

        self.driver.find_element_by_xpath(
            '//*[@id="login_password_step_element"]/button').click()
        print("\n\n\nbutton clicked\n\n\n\n")

    def nav_user(self, user):

        self.driver.get('{}/{}/'.format(self.base, user))

    def scroll(self):

        try:

            time.sleep(2)
            for i in range(5):
                time.sleep(1)
                self.driver.find_element_by_tag_name(
                    'body').send_keys(Keys.END)

            links = self.driver.find_elements_by_class_name('_5msj')
            f = open('{}_links.txt'.format(userinput), "a")
            for i in links:
                f.write(str(i.get_attribute('href')))
                f.write("\n")
            f.close()
            self.likes()
        except:
            pass

    def likes(self):

        # try:
        posts = open('{}_links.txt'.format(userinput), 'r')
        for line in posts:
            self.driver.get(line)
            for i in range(3):
                time.sleep(1)
                self.driver.find_element_by_tag_name(
                    'body').send_keys(Keys.END)
            commentreplybutton = self.driver.find_elements_by_class_name('_4ayj')
            for i in commentreplybutton:
                i.click()
            commentorname = self.driver.find_elements_by_class_name('_2b05')
            commentfile = open("{}_comment.txt".format(userinput), 'a')
            for commentor in range(0, (len(commentorname)-1), 2):
                for letter in commentorname[commentor].text:
                        print("the word is " + commentorname[commentor].text + " the letter is " + str(letter) +
                            " the ascii is " + str(ord(letter)))
                        try:

                            if number == False:
                                if ord(letter) <= 64 and letter != " " and letter != "-":
                                    number = True
                                    print("There was a number, skipped")
                                    break
                        except:
                            pass
                if number == False:
                    commentfile.write(str(names[name].text) + "\n")
            commentfile.close()
            likebutton = self.driver.find_element_by_class_name(
                '_45m8').get_attribute('href')
            self.driver.get(likebutton)
            for i in range(4):
                time.sleep(1)
                self.driver.find_element_by_tag_name(
                    'body').send_keys(Keys.END)
            names = self.driver.find_elements_by_tag_name('span')
            namefile = open("{}_likes.txt".format(userinput), 'a')
            for name in range(0, (len(names)-1), 2):
                number = False
                trycast = 0
                print("\n\n\n")
                for letter in names[name].text:
                    print("the word is " + names[name].text + " the letter is " + str(letter) +
                          " the ascii is " + str(ord(letter)))
                    try:

                        if number == False:
                            if ord(letter) <= 64 and letter != " " and letter != "-":
                                number = True
                                print("There was a number, skipped")
                                break
                    except:
                        pass
                if number == False:
                    namefile.write(str(names[name].text) + "\n")
            namefile.close()
            time.sleep(20)
        posts.close()
        # except:
        #     pass


if __name__ == '__main__':
    userinput = "laborforfisher"
    ig_bot = Instagrambot('takamundy@gmail.com', 'Taka6745!')
    time.sleep(2)
    ig_bot.nav_user(userinput)
    ig_bot.scroll()
