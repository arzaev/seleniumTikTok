
import undetected_chromedriver as uc
import time


class TikTokSelenium:
    def __init__(self, proxy):
        host = proxy.split(':')[0]
        port = proxy.split(':')[1]
        chrome_options = uc.ChromeOptions()
        chrome_options.add_argument(f'--proxy-server=http://{host}:{port}')
        self.driver = uc.Chrome(options=chrome_options)

    def start(self, email, password):
        self.driver.get('https://www.tiktok.com/login/phone-or-email/email')
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/form/div[2]/div/input').send_keys(email)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/form/div[3]/div/input').send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/form/button').click()

    def get_main_page(self):
        self.driver.get('https://www.tiktok.com/')

    def follow(self, parsing_list):
        for user in parsing_list:
            try:
                self.driver.get("https://www.tiktok.com/@{}?".format(user))
                time.sleep(1)
                self.driver.find_element_by_xpath(
                    '//*[@id="main"]/div[2]/div[2]/div/header/div[1]/div[2]/div/div[1]/button').click()
                time.sleep(1)
            except Exception as error:
                print(error)
                print('error: ' + user)