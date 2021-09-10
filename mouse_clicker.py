from pynput.mouse import Button, Controller
from pynput.keyboard import Controller as keycontr
from pynput.keyboard import Key
import undetected_chromedriver as uc
import time
from selenium import webdriver

import pickle


class SenTiktok:

    def auth(self):
        options = uc.ChromeOptions()
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        self.driver = uc.Chrome(options=options)
        self.driver.get('https://www.tiktok.com/@charlidamelio?')

    def follow(self, parsing):
        with open(parsing, 'r') as f:
            parsing_list = f.readlines()
        count = 0
        for user in parsing_list:
            try:
                self.driver.get("https://www.tiktok.com/@{}?".format(user))
                time.sleep(5)
                mouse = Controller()
                mouse.position = (1125, 266)
                mouse.click(Button.left, 10)
                time.sleep(5)
                print('username {}: {}'.format(str(user), str(count)))
            except Exception as error:
                print(error)
                print('error: ' + user)
            count += 1

    def like(self, parsing):
        with open(parsing, 'r') as f:
            parsing_list = f.readlines()
        count = 0
        for video in parsing_list:
            try:
                self.driver.get(video)
                time.sleep(5)
                # self.driver.find_element_by_tag_name("body").send_keys("l")
                keyboard = keycontr()
                keyboard.press('l')
                keyboard.release('l')
                time.sleep(5)
                print('video {}: {}'.format(str(video), str(count)))
            except Exception as error:
                print(error)
                print('error: ' + video)
            count += 1

    def comment(self, parsing):
        with open(parsing, 'r') as f:
            parsing_list = f.readlines()
        count = 0
        for video in parsing_list:
            try:
                self.driver.get(video)
                time.sleep(5)
                button_comments = self.driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[2]/div/div/main/div/div[1]/span[1]/div/div[1]/div[5]/div[2]/div[2]/div')
                button_comments.click()
                time.sleep(5)

                mouse = Controller()
                mouse.position = (1500, 1000)
                mouse.click(Button.left, 1)
                time.sleep(2)
                keyboard = keycontr()
                keyboard.type("hello")
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
                time.sleep(2)

                print('video {}: {}'.format(str(video), str(count)))
            except Exception as error:
                print(error)
                print('error: ' + video)
            count += 1

    def save_cookies(self, name_cookies):
        pickle.dump(self.driver.get_cookies(), open("{}.pkl".format(name_cookies), "wb"))

    def set_cookies(self, name_cookies):
        cookies = pickle.load(open("{}.pkl".format(name_cookies), "rb"))
        for cookie in cookies:
            print(cookie)
            if 'sameSite' in cookie:
                if cookie['sameSite'] == 'None':
                    cookie['sameSite'] = 'Strict'
            self.driver.add_cookie(cookie)


tiktok = SenTiktok()

if __name__ == "__main__":
    while True:
        command = input("tiktok> ")
        print(command)
        if 'auth' in command:
            tiktok.auth()
        if 'follow' in command:
            parsing_list = command.split('-p ')[1]
            tiktok.follow(parsing_list)
        if 'like' in command:
            parsing_list = command.split('-p ')[1]
            tiktok.like(parsing_list)
        if 'comment' in command:
            parsing_list = command.split('-p ')[1]
            tiktok.comment(parsing_list)
        if 'save cookies' in command:
            name_cookies = command.split('-n ')[1]
            tiktok.save_cookies(name_cookies)
        if 'set cookies' in command:
            name_cookies = command.split('-n ')[1]
            tiktok.set_cookies(name_cookies)



