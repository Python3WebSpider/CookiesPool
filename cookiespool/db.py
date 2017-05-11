import random

import redis

from cookiespool.config import *
from cookiespool.error import *


class RedisClient(object):
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD):
        """
        初始化Redis连接
        :param host: 地址
        :param port: 端口
        :param password: 密码
        """
        if password:
            self._db = redis.Redis(host=host, port=port, password=password)
        else:
            self._db = redis.Redis(host=host, port=port)
        self.domain = REDIS_DOMAIN
        self.name = REDIS_NAME

    def _key(self, key):
        """
        得到格式化的key
        :param key: 最后一个参数key
        :return:
        """
        return "{domain}:{name}:{key}".format(domain=self.domain, name=self.name, key=key)

    def set(self, key, value):
        """
        设置键值对
        :param key:
        :param value:
        :return:
        """
        raise NotImplementedError

    def get(self, key):
        """
        根据键名获取键值
        :param key:
        :return:
        """
        raise NotImplementedError

    def delete(self, key):
        """
        根据键名删除键值对
        :param key:
        :return:
        """
        raise NotImplementedError

    def keys(self):
        """
        得到所有的键名
        :return:
        """
        return self._db.keys('{domain}:{name}:*'.format(domain=self.domain, name=self.name))

    def flush(self):
        """
        清空数据库, 慎用
        :return:
        """
        self._db.flushall()


class CookiesRedisClient(RedisClient):
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, domain='cookies', name='default'):
        """
        管理Cookies的对象
        :param host: 地址
        :param port: 端口
        :param password: 密码
        :param domain: 域, 如cookies, account等
        :param name: 名称, 一般为站点名, 如 weibo, 默认 default
        """
        RedisClient.__init__(self, host, port, password)
        self.domain = domain
        self.name = name

    def set(self, key, value):
        try:
            self._db.set(self._key(key), value)
        except:
            raise SetCookieError

    def get(self, key):
        try:
            return self._db.get(self._key(key)).decode('utf-8')
        except:
            return None

    def delete(self, key):
        try:
            print('Delete', key)
            return self._db.delete(self._key(key))
        except:
            raise DeleteCookieError

    def random(self):
        """
        随机得到一Cookies
        :return:
        """
        try:
            keys = self.keys()
            return self._db.get(random.choice(keys))
        except:
            raise GetRandomCookieError

    def all(self):
        """
        获取所有账户, 以字典形式返回
        :return:
        """
        try:
            for key in self._db.keys('{domain}:{name}:*'.format(domain=self.domain, name=self.name)):
                group = key.decode('utf-8').split(':')
                if len(group) == 3:
                    username = group[2]
                    yield {
                        'username': username,
                        'cookies': self.get(username)
                    }
        except Exception as e:
            print(e.args)
            raise GetAllCookieError

    def count(self):
        """
        获取当前Cookies数目
        :return: 数目
        """
        return len(self.keys())



class AccountRedisClient(RedisClient):
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, domain='account', name='default'):
        RedisClient.__init__(self, host, port, password)
        self.domain = domain
        self.name = name

    def set(self, key, value):
        try:
            return self._db.set(self._key(key), value)
        except:
            raise SetAccountError

    def get(self, key):
        try:
            return self._db.get(self._key(key)).decode('utf-8')
        except:
            raise GetAccountError

    def all(self):
        """
        获取所有账户, 以字典形式返回
        :return:
        """
        try:
            for key in self._db.keys('{domain}:{name}:*'.format(domain=self.domain, name=self.name)):
                group = key.decode('utf-8').split(':')
                if len(group) == 3:
                    username = group[2]
                    yield {
                        'username': username,
                        'password': self.get(username)
                    }
        except Exception as e:
            print(e.args)
            raise GetAllAccountError

    def delete(self, key):
        """
        通过用户名删除用户
        :param key:
        :return:
        """
        try:
            return self._db.delete(self._key(key))
        except:
            raise DeleteAccountError


if __name__ == '__main__':
    """
    conn = CookiesRedisClient()
    conn.set('name', 'Mike')
    conn.set('name2', 'Bob')
    conn.set('name3', 'Amy')
    print(conn.get('name'))
    conn.delete('name')
    print(conn.keys())
    print(conn.random())
    """
    # 测试
    conn = AccountRedisClient(name='weibo')
    conn2 = AccountRedisClient(name='mweibo')


    accounts = conn.all()
    for account in accounts:
        conn2.set(account['username'], account['password'])
