import random
import redis
from cookiespool.config import *


class RedisClient(object):
    def __init__(self, type, website, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD):
        """
        初始化Redis连接
        :param host: 地址
        :param port: 端口
        :param password: 密码
        """
        self.db = redis.Redis(host=host, port=port, password=password, decode_responses=True)
        self.type = type
        self.website = website

    def key(self):
        """
        得到格式化的username
        :param username: 最后一个参数username
        :return:
        """
        return "{type}:{website}".format(type=self.type, website=self.website)

    def set(self, username, value):
        """
        设置键值对
        :param username:
        :param value:
        :return:
        """
        return self.db.hset(self.key(), username, value)

    def get(self, username):
        """
        根据键名获取键值
        :param username:
        :return:
        """
        return self.db.hget(self.key(), username)

    def delete(self, username):
        """
        根据键名删除键值对
        :param username:
        :return:
        """
        return self.db.hdel(self.key(), username)

    def count(self):
        """
        获取数目
        :return: 数目
        """
        return self.db.hlen(self.key())

    def random(self):
        """
        随机得到键值
        :return:
        """
        return random.choice(self.db.hvals(self.key()))

    def usernames(self):
        """
        获取所有账户信息
        :return:
        """
        return self.db.hkeys(self.key())

    def all(self):
        """
        获取所有键值对
        :return:
        """
        return self.db.hgetall(self.key())


if __name__ == '__main__':
    conn = RedisClient('accounts', 'weibo')
    result = conn.set('hell2o', 'sss3s')
    print(result)
