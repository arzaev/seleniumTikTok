
# import undetected_chromedriver as uc
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys


class TikTokSelenium:
    def __init__(self, proxy):
        # options = webdriver.ChromeOptions()
        # options.add_argument("start-maximized")
        # options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # options.add_experimental_option('useAutomationExtension', False)
        # self.driver = webdriver.Chrome(options=options)
        # self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        # self.driver.execute_cdp_cmd('Network.setUserAgentOverride', {
        #     "userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
        # print(self.driver.execute_script("return navigator.userAgent;"))

        # chrome_options = uc.ChromeOptions()
        # if ':' in proxy:
        #     host = proxy.split(':')[0]
        #     port = proxy.split(':')[1]
        #     chrome_options.add_argument(f'--proxy-server=http://{host}:{port}')
        # chrome_options.add_argument("user-agent=" + "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36")
        # self.driver = uc.Chrome(options=chrome_options)

        options = webdriver.ChromeOptions()
        if ':' in proxy:
            host = proxy.split(':')[0]
            port = proxy.split(':')[1]
            options.add_argument(f'--proxy-server=http://{host}:{port}')
        options.add_argument('--disable-blink-features=AutomationControlled')
        self.driver = webdriver.Chrome(options=options)

        # profile = webdriver.FirefoxProfile()
        # profile.set_preference("dom.webdriver.enabled", False)
        # self.driver = webdriver.Firefox(executable_path=r'{}/geckodriver.exe'.format(str(sys.path[0])), firefox_profile=profile)

    def start(self, email, password):
        # self.driver.get('https://www.tiktok.com/login/phone-or-email/email')
        # time.sleep(1)
        # self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/form/div[2]/div/input').send_keys(email)
        # self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/form/div[3]/div/input').send_keys(password)
        # self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/form/button').click()
        # self.driver.get('https://www.tiktok.com/')
        self.driver.get('https://www.tiktok.com/@charlidamelio?')
        # html = self.driver.find_element_by_tag_name('html')
        # html.send_keys(Keys.END)

        # time.sleep(5)
        # try:
        #     self.driver.find_element_by_xpath('//*[@id="app"]/div[3]/div[2]/button').click()
        # except:
        #     print('no accept cookies')
        # self.driver.get('https://www.tiktok.com/login/phone-or-email/email')
        # time.sleep(1)
        # self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/form/div[2]/div/input').send_keys(email)
        # self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/form/div[3]/div/input').send_keys(password)
        # self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/form/button').click()


    def get_main_page(self):
        self.driver.get('https://www.tiktok.com/')

    def follow_action(self):
        xpathfollow1 = '//*[@id="main"]/div[2]/div[2]/div/header/div[1]/div[2]/div/div[1]/button'
        xpathfollow2 = '//*[@id="main"]/div[3]/div[2]/div/header/div[1]/div[2]/div/div[1]/button'
        try:
            self.driver.find_element_by_xpath(xpathfollow1).click()
        except:
            self.driver.find_element_by_xpath(xpathfollow2).click()

    # def follow(self, parsing_list, _id):
    #     print(len(parsing_list))
    #     count = 0
    #     for user in parsing_list:
    #         try:
    #             self.driver.get("https://www.tiktok.com/@{}?".format(user))
    #             time.sleep(random.randint(1, 4))
    #             self.follow_action()
    #
    #             for i in range(20):
    #                 self.driver.get("https://www.tiktok.com/@{}?".format(user))
    #                 time.sleep(1)
    #                 el_xpath =      '//*[@id="main"]/div[2]/div[2]/div/header/div[1]/div[2]/div/div[1]/button'
    #                 text = self.driver.find_element_by_xpath(el_xpath).text
    #                 print(text)
    #                 if text == 'Follow':
    #                     self.follow_action()
    #                 else:
    #                     count += 1
    #                     print('_id {}: {}'.format(str(_id), str(count)))
    #                     with open('log.txt', 'w') as f:
    #                         f.write(str(count))
    #                     break
    #
    #
    #         except Exception as error:
    #             print(error)
    #             print('error: ' + user)

    def follow(self, parsing_list, _id):
        print(len(parsing_list))
        count = 0
        for user in parsing_list:
            try:
                self.driver.get("https://www.tiktok.com/@{}?".format(user))
                time.sleep(random.randint(1, 5))
                # self.follow_action()
                print('_id {}: {}'.format(str(_id), str(count)))
                with open('log.txt', 'w') as f:
                    f.write(str(count))
                count += 1
            except Exception as error:
                print(error)
                print('error: ' + user)