import json
from bs4 import BeautifulSoup
import requests
from requests.exceptions import ConnectionError
from cookiespool.db import *
from cookiespool.generator import WeiboCookiesGenerator


class ValidTester(object):
    def __init__(self, name='default'):
        self.name = name
        self.cookies_db = CookiesRedisClient(name=self.name)
        self.account_db = AccountRedisClient(name=self.name)

    def test(self, account, cookies):
        raise NotImplementedError

    def run(self):
        accounts = self.cookies_db.all()
        for account in accounts:
            username = account.get('username')
            cookies = self.cookies_db.get(username)
            self.test(account, cookies)


class WeiboValidTester(ValidTester):
    def __init__(self, name='weibo'):
        ValidTester.__init__(self, name)

    def test(self, account, cookies):
        print('Testing Account', account.get('username'))
        try:
            cookies = json.loads(cookies)
        except TypeError:
            # Cookie 格式不正确
            print('Invalid Cookies Value', account.get('username'))
            self.cookies_db.delete(account.get('username'))
            print('Deleted User', account.get('username'))
            return None
        try:
            response = requests.get('http://weibo.cn', cookies=cookies)
            if response.status_code == 200:
                html = response.text
                soup = BeautifulSoup(html, 'lxml')
                title = soup.title.string
                if title == '我的首页':
                    print('Valid Cookies', account.get('username'))
                else:
                    print('Title is', title)
                    # Cookie已失效
                    print('Invalid Cookies', account.get('username'))
                    self.cookies_db.delete(account.get('username'))
                    print('Deleted User', account.get('username'))
        except ConnectionError as e:
            print('Error', e.args)
            print('Invalid Cookies', account.get('username'))


class MWeiboValidTester(ValidTester):
    def __init__(self, name='weibo'):
        ValidTester.__init__(self, name)

    def test(self, account, cookies):
        print('Testing Account', account.get('username'))
        try:
            cookies = json.loads(cookies)
        except TypeError:
            # Cookie 格式不正确
            print('Invalid Cookies Value', account.get('username'))
            self.cookies_db.delete(account.get('username'))
            print('Deleted User', account.get('username'))
            return None
        try:
            test_url = 'http://m.weibo.cn/api/container/getIndex?uid=1804544030&type=uid&page=1&containerid=1076031804544030'
            response = requests.get(test_url, cookies=cookies, timeout=5, allow_redirects=False)
            if response.status_code == 200:
                print('Valid Cookies', account.get('username'))
            else:
                print(response.status_code, response.headers)
                print('Invalid Cookies', account.get('username'))
                self.cookies_db.delete(account.get('username'))
                print('Deleted User', account.get('username'))
        except ConnectionError as e:
            print('Error', e.args)
            print('Invalid Cookies', account.get('username'))

if __name__ == '__main__':
    tester = WeiboValidTester()
    tester.run()
