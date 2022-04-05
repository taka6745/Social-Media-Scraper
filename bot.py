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
        self.base = 'https://www.instagram.com'

        self.driver = webdriver.Chrome(ChromeDriverManager().install())

        self.login()

    def login(self):

        self.driver.get('{}/accounts/login/'.format(self.base))
        time.sleep(2)
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[3]/button').click()
        time.sleep(5)
        self.driver.get(self.base)
        not_now = self.driver.find_elements_by_class_name('aOOlW.HoLwm')
        not_now[0].click()

        # you can find the like button using class name too

    def nav_user(self, user):

        self.driver.get('{}/{}/'.format(self.base, user))

    def toggle_follow(self, user):
        self.nav_user(user)
        try:
            follow_list = self.driver.find_elements_by_xpath(
                "//button[contains(text(), 'Follow')]")
            follow_list[0].click()
        except:
            unfollow = self.driver.find_elements_by_class_name('vBF20._1OSdk')
            unfollow[0].click()
            confirm = self.driver.find_element_by_class_name(
                'aOOlW.-Cab_').click()

    def follow_user(self, user):
        self.nav_user(user)
        global liking
        liking = random.randint(2, 20)
        if liking > 6:
            tolike = 7
        else:
            tolike = liking
        time.sleep(87-(tolike*11))
        try:
            follow_list = self.driver.find_elements_by_xpath(
                "//button[contains(text(), 'Follow')]")
            follow_list[0].click()
        except:
            pass

    def unfollow_user(self):
        try:
            time.sleep(1)
            unfollow = self.driver.find_element_by_class_name(
                '_5f5mN.-fzfL._6VtSN.yZn4P').click()

            confirm = self.driver.find_element_by_class_name(
                'aOOlW.-Cab_').click()
        except:
            pass

    def followers(self):

        self.unfollow_user()
        try:
            self.driver.find_element_by_xpath(
                "//a[contains(@href,'/followers')]").click()
            time.sleep(5)
            scroll_box = self.driver.find_element_by_class_name("isgrP")
            prev_height, height = 0, 1
            while prev_height != height:
                prev_height = height
                time.sleep(3)
                height = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
                """, scroll_box)
            links = scroll_box.find_elements_by_tag_name('a')
            time.sleep(0.1)
            names = [name.text for name in links if name.text != '']
            time.sleep(12)
            global comments
            for i in names:
                self.follow_user(i)
                self.first_picture()

                self.like_pic()
                self.continue_liking()
                time.sleep(random.randint(0, 15))

            self.driver.get('{}/explore/tags/love/'.format(self.base))
            self.driver.find_element_by_class_name('v1Nh3.kIKUG._bz0w').click()
            self.driver.find_element_by_class_name('PQo_0 ').click()
            self.followers()
        except:
            self.driver.get('{}/explore/tags/love/'.format(self.base))
            self.driver.find_element_by_class_name('v1Nh3.kIKUG._bz0w').click()
            self.driver.find_element_by_class_name('PQo_0 ').click()
            self.followers()

    def first_picture(self):
        global check
        time.sleep(1)
        try:
            # finds the first picture
            yeet = self.driver.find_elements_by_class_name("v1Nh3.kIKUG._bz0w")
            # clicks on the first picture
            yeet[0].click()
            check = True
        except:
            check = False

    def like_pic(self):
        if check == True:
            time.sleep(5)
            like = self.driver.find_element_by_class_name('fr66n')

            # you can find the like button using class name too

            like.click()   # clicking the like button

    def continue_liking(self):
        global liking
        if check == True:

            for i in range(1, liking):
                time.sleep(5)
                try:

                    # finds the button which gives the next picture
                    self.driver.find_element_by_class_name(
                        "_65Bje.coreSpriteRightPaginationArrow").click()
                    time.sleep(1)
                    rand = random.randint(0, 100)
                    comments = ['Love it!', ' #Love', '💖🔥', 'love the post', 'Legend',
                                'Come check out outer', 'I\'m loving it', 'Finger Licking Good', 'Keep it up']

                    if rand <= odds:

                        print('comment hit')
                        time.sleep(1)
                        comment_random = random.randint(0, 8)
                        commentSection = ui.WebDriverWait(self.driver, 10).until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.Ypffh")))
                        self.driver.execute_script(
                            "arguments[0].scrollIntoView(true);", commentSection)
                        five = 0
                        while(1 == 1) and five != 5:
                            try:
                                commentSection = ui.WebDriverWait(self.driver, 10).until(
                                    EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.Ypffh")))

                                commentSection.send_keys(
                                    comments[comment_random])
                                commentSection.send_keys(Keys.ENTER)

                                break
                            except:
                                print('broken')
                                five += 1
                                pass

                    else:
                        print(str(rand) + ' Comment miss')
                    self.like_pic()

                except:
                    pass


if __name__ == '__main__':
    while odds > 100:
        try:
            odds = int(
                input('What percentage odds do you want for comment on post [0-100]: '))
        except:
            pass
    userinput = input('What user to follow all of their followers: ')
    ig_bot = Instagrambot('outer.meming', 'Lucas1203!')
    time.sleep(2)
    ig_bot.nav_user(userinput)
    ig_bot.followers()
