
import requests


proxies = {
  'http': 'http://192.168.0.125:8080',
  'https': 'http://192.168.0.125:8080',
}

class Login:
    def __init__(self, proxy=True,
                 item_proxy='192.168.0.125:8080',
                 type_proxy='https',
                 user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
                 verify=False, timeout=10):
        self.user_agent = user_agent
        self.session = requests.Session()
        self.item_proxy = item_proxy
        self.type_proxy = type_proxy
        if type_proxy == 'socks5':
            self.proxies = {
                'http': 'socks5://{}'.format(item_proxy),
                'https': 'socks5://{}'.format(item_proxy)
            }
        else:
            if '@' in item_proxy:
                self.proxies = {'http': 'http://{}'.format(item_proxy),
                                'https': 'https://{}'.format(item_proxy)}
            else:
                self.proxies = {'http': item_proxy, 'https': item_proxy}
        self.verify = verify
        self.timeout = timeout
        self.list = []
     #   self.proxies = None

    def start(self, login):
        url = 'https://www.tiktok.com/@{}?'.format(login)
        headers = {'Host': 'www.tiktok.com',
                    'User-Agent': self.user_agent,
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Accept-Encoding': 'gzip, deflate',
                    'Upgrade-Insecure-Requests': '1',
                    'Sec-Fetch-Dest': 'document',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-Site': 'none',
                    'Sec-Fetch-User': '?1',
                    'Te': 'trailers',
                    }
        r = self.session.get(url, headers=headers, proxies=proxies, verify=False)
        if 'blogspot' in r.text:
            print('good: ' + login)
            with open('blogspotaccs.txt', 'a') as f:
                f.write(login + '\n')

with open('input.txt', 'r') as f:
    logins = f.read().split('\n')


for i in logins:
    login = Login()
    l = i.split(':')[1]
    print(l)
    login.start(l)


