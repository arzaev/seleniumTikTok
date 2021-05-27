
import undetected_chromedriver as uc
import time


class TikTokSelenium:
    def __init__(self):
        self.driver = uc.Chrome()

    def start(self, email, password):
        self.driver.get('https://www.tiktok.com/login/phone-or-email/email')
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/form/div[2]/div/input').send_keys(email)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/form/div[3]/div/input').send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/form/button').click()

    def get_main_page(self):
        self.driver.get('https://www.tiktok.com/')