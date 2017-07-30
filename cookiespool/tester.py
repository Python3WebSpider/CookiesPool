import json
import requests
from requests.exceptions import ConnectionError
from cookiespool.db import *


class ValidTester(object):
    def __init__(self, name='default'):
        self.name = name
        self.cookies_db = RedisClient('cookies', self.name)
        self.account_db = RedisClient('accounts', self.name)
    
    def test(self, account, cookies):
        raise NotImplementedError
    
    def run(self):
        accounts = self.cookies_db.all()
        print(accounts)
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
            print('Invalid Cookies Value', account.get('username'))
            self.cookies_db.delete(account.get('username'))
            print('Deleted User', account.get('username'))
            return None
        try:
            test_url = TEST_URL_MAP[self.name]
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

