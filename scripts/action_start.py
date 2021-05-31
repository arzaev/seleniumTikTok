import threading
import time
from .tiktokSelenium import TikTokSelenium


class Data:
    def __init__(self, action, id_item, email, password, proxy):
        self.action = action
        self.id = id_item
        self.email = email
        self.password = password
        self.tiktok = TikTokSelenium(proxy)
        self.parsing_list = []

    def start(self):
        self.tiktok.start(self.email, self.password)

    def get_main_page(self):
        self.tiktok.get_main_page()

    def follow(self):
        self.tiktok.follow(self.parsing_list, self.id)


def some_function(data):
    while True:
        time.sleep(1)
        if data.action == 'start':
            data.start()
        elif data.action == 'get main page':
            data.get_main_page()
        elif data.action == 'follow':
            data.follow()
        data.action = '-'


def thread_action(data):
    th = threading.Thread(target=some_function, args=(data, ))
    th.start()