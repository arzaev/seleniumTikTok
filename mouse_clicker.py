from pynput.mouse import Button, Controller
import time
from selenium import webdriver
import pickle


class SenTiktok:

    def auth(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-blink-features=AutomationControlled')
        self.driver = webdriver.Chrome(options=options)
        self.driver.get('https://www.tiktok.com/@charlidamelio?')

    def start(self, parsing):
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

    def save_cookies(self, name_cookies):
        pickle.dump(self.driver.get_cookies(), open("{}.pkl".format(name_cookies), "wb"))

    def set_cookies(self, name_cookies):
        cookies = pickle.load(open("{}.pkl".format(name_cookies), "rb"))
        for cookie in cookies:
            print(cookie)
            self.driver.add_cookie(cookie)


tiktok = SenTiktok()

if __name__ == "__main__":
    while True:
        command = input("tiktok> ")
        print(command)
        if 'auth' in command:
            tiktok.auth()
        if 'start' in command:
            parsing_list = command.split('-p ')[1]
            tiktok.start(parsing_list)
        if 'save cookies' in command:
            name_cookies = command.split('-n ')[1]
            tiktok.save_cookies(name_cookies)
        if 'set cookies' in command:
            name_cookies = command.split('-n ')[1]
            tiktok.set_cookies(name_cookies)



