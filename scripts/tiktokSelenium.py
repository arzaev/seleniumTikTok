
import undetected_chromedriver as uc


class TikTokSelenium:
    def __init__(self):
        self.driver = uc.Chrome()

    def start(self):
        self.driver.get('https://www.tiktok.com/login/phone-or-email/email')

    def get_main_page(self):
        self.driver.get('https://www.tiktok.com/')