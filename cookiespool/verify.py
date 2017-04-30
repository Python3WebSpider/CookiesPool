import time

import requests
from requests.exceptions import ConnectionError

from cookiespool.config import *


class Yundama():
    def __init__(self, username, password, app_id, app_key, api_url=YUNDAMA_API_URL):
        self.username = username
        self.password = password
        self.app_id = str(app_id) if not isinstance(app_id, str) else app_id
        self.app_key = app_key
        self.api_url = api_url

    def login(self):
        """
        登录云打码账户
        :return:
        """
        try:
            data = {'method': 'login', 'username': self.username, 'password': self.password, 'appid': self.app_id,
                    'appkey': self.app_key}
            response = requests.post(self.api_url, data=data)
            if response.status_code == 200:
                result = response.json()
                print(result)
                if 'ret' in result.keys() and result.get('ret') < 0:
                    return self.error(result.get('ret'))
                else:
                    return result
            return None
        except ConnectionError:
            return None

    def upload(self, files, timeout, code_type):
        """
        上传验证码得到识别结果
        :param files:
        :param timeout:
        :param code_type:
        :return:
        """
        try:
            data = {'method': 'upload', 'username': self.username, 'password': self.password, 'appid': self.app_id,
                    'appkey': self.app_key, 'codetype': str(code_type), 'timeout': str(timeout)}
            response = requests.post(self.api_url, data=data, files=files)
            if response.status_code == 200:
                return response.json()
            return None
        except ConnectionError:
            return None

    def retry(self, cid, try_count=1):
        """
        临时识别不出, 传入cid重试
        :param cid: 验证码ID
        :param try_count: 重试次数
        :return: 验证码结果
        """
        if try_count >= YUNDAMA_MAX_RETRY:
            return None
        print('Retrying: ', cid, 'Count: ', try_count)
        time.sleep(2)
        try:
            data = {'method': 'result', 'cid': cid}
            print(data)
            response = requests.post(self.api_url, data=data)
            if response.status_code == 200:
                result = response.json()
                print(result)
                if 'ret' in result.keys() and result.get('ret') < 0:
                    print(self.error(result.get('ret')))
                if result.get('ret') == 0 and 'text' in result.keys():
                    return result.get('text')
                else:
                    return self.retry(cid, try_count + 1)
            return None
        except ConnectionError:
            return None

    def identify(self, file=None, stream=None, timeout=60, code_type=5000):
        """
        主函数
        :param file: 文件名
        :param stream: 文件流, 优先于文件名
        :param timeout: 超时时间
        :param code_type: 验证码类型
        :return: 识别结果
        """
        if stream:
            files = {'file': stream}
        elif file:
            files = {'file': open(file, 'rb')}
        else:
            return None
        result = self.upload(files, timeout, code_type)
        if 'ret' in result.keys() and result.get('ret') < 0:
            print(self.error(result.get('ret')))
        if result.get('text'):
            print('验证码识别成功', result.get('text'))
            return result.get('text')
        else:
            return self.retry(result.get('cid'))

    def error(self, code):
        """
        报错原因
        :param code: 错误码
        :return: 错误原因
        """
        map = {
            -1001: '密码错误',
            -1002: '软件ID/密钥有误',
            -1003: '用户被封',
            -1004: 'IP被封',
            -1005: '软件被封',
            -1006: '登录IP与绑定的区域不匹配',
            -1007: '账号余额为零',
            -2001: '验证码类型有误',
            -2002: '验证码图片太大',
            -2003: '验证码图片损坏',
            -2004: '上传验证码图片失败',
            -3001: '验证码ID不存在	',
            -3002: '验证码还在识别',
            -3003: '验证码识别超时',
            -3004: '验证码看不清',
            -3005: '验证码报错失败',
            -4001: '充值卡号不正确或已使用',
            -5001: '注册用户失败'
        }
        return '云打码' + map.get(code)


if __name__ == '__main__':
    ydm = Yundama(YUNDAMA_USERNAME, YUNDAMA_PASSWORD, YUNDAMA_APP_ID, YUNDAMA_APP_KEY)
    result = ydm.identify(file='getimage.jpg')
    print(result)
