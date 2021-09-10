
import requests


proxies = {
  'http': 'http://192.168.0.125:8080',
  'https': 'http://192.168.0.125:8080',
}


class ParsingVideos:
    def __init__(self, user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0'):
        self.user_agent = user_agent
        self.session = requests.Session()

    def start(self, username):
        url = 'https://www.tiktok.com/@{}'.format(username)
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
        if '"items":[{"id":"' in r.text:
            id_video = r.text.split('"items":[{"id":"')[1].split('"')[0]
            video_link = "https://www.tiktok.com/@{}/video/{}?is_copy_url=1&is_from_webapp=v1".format(username, id_video)

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
            r = self.session.get(video_link, headers=headers, proxies=proxies, verify=False)
            stat = r.text.split('"stats":{')[1].split('"isActivityItem"')[0]
            likes = stat.split('"diggCount":')[1].split(',')[0]
            comments = stat.split('"commentCount":')[1].split(',')[0]
            print(video_link)
            print(stat)
            if int(likes) < 50:
                if int(comments) < 50:
                with open('out_videos.txt', 'a') as f:
                    f.write(video_link + '\n')


with open('input.txt', 'r') as f:
    logins = f.readlines()


for i in logins:
    parsing_videos = ParsingVideos()
    parsing_videos.start(i.strip())


