import threading
import time


class Data:
    def __init__(self, action, id_item, email, password):
        self.action = action
        self.id = id_item
        self.email = email
        self.password = password


def some_function(data):
    while True:
        print(data.action)
        time.sleep(1)


def thread_action(data):
    th = threading.Thread(target=some_function, args=(data, ))
    th.start()