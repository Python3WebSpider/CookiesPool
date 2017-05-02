# CookiesPool / Cookies池

可扩展的Cookies池，目前对接了新浪微博，可自行扩展其他站点

亲测可用，利用它已经3天成功抓取1亿条微博数据

## 安装

```
pip3 install -r requirements.txt
```

## 基础配置 

修改cookiespool/config.py

### 数据库配置

account:weibo:账号

cookies:weibo:账号

Value分别为密码和Cookies

账号自行某宝购买

Redis连接信息到cookiespool/config文件修改

### 云打码平台配置

到yundama.com注册开发者和普通用户。

开发者申请应用ID和KEY，普通用户用于充值登录。

配置信息到cookiespool/config文件修改


### 进程开关

配置信息到cookiespool/config文件修改

## 运行

```
python3 run.py
```

## 批量导入

```
python3 importer.py
```

```
请输入账号密码组, 输入exit退出读入
18459748505----astvar3647
14760253606----gmidy8470
14760253607----uoyuic8427
18459749258----rktfye8937
账号 18459748505 密码 astvar3647
录入成功
账号 14760253606 密码 gmidy8470
录入成功
账号 14760253607 密码 uoyuic8427
录入成功
账号 18459749258 密码 rktfye8937
录入成功
exit
```

## 运行效果

开启Generator、API，关闭Tester为例：

```
Generating Cookies
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
Getting 526 accounts from Redis
Getting Cookies of  weibo uva68312006hao@163.com 1nr0nkwes7
Generating Cookies of uva68312006hao@163.com
出现验证码，开始识别验证码
Retrying:  1400009488 Count:  1
{'cid': 1400009488, 'method': 'result'}
{'cid': 1400009488, 'ret': -3002, 'text': ''}
云打码验证码还在识别
Retrying:  1400009488 Count:  2
{'cid': 1400009488, 'method': 'result'}
{'cid': 1400009488, 'ret': -3002, 'text': ''}
云打码验证码还在识别
Retrying:  1400009488 Count:  3
{'cid': 1400009488, 'method': 'result'}
{'cid': 1400009488, 'ret': -3002, 'text': ''}
云打码验证码还在识别
Retrying:  1400009488 Count:  4
{'cid': 1400009488, 'method': 'result'}
{'cid': 1400009488, 'ret': -3002, 'text': ''}
云打码验证码还在识别
Retrying:  1400009488 Count:  5
{'cid': 1400009488, 'method': 'result'}
{'cid': 1400009488, 'ret': 0, 'text': '4uh4h'}
登录成功
[{'expiry': 1525092087.375918, 'secure': False, 'value': '0cS3YKcgWrDRsV', 'httpOnly': False, 'name': 'SUHB', 'path': '/', 'domain': '.weibo.cn'}, {'expiry': 1525092087.374765, 'secure': False, 'value': '0033WrSXqPxfM725Ws9jqgMF55529P9D9W5H8du8O9J-.X.2Zd-6LbEK5JpX5o2p5NHD95QfS0ecSKe7e0n4Ws4Dqcj.i--fiK.7iKn4i--ci-z7i-zRi--fi-2fiK.ci--4i-2pi-i2', 'httpOnly': False, 'name': 'SUBP', 'path': '/', 'domain': '.weibo.cn'}, {'expiry': 1525092087.373734, 'secure': False, 'value': '_2A250AasnDeThGeNJ6FQU8y7PwzWIHXVXDTVvrDV6PUJbktBeLRfukW0wFLR2922NnApkDOZb_eNrRfNBZQ..', 'httpOnly': True, 'name': 'SUB', 'path': '/', 'domain': '.weibo.cn'}, {'expiry': 1496148087.677672, 'secure': False, 'value': 'b2d2d84c5aafcc02c0dac2faa4acc43f', 'httpOnly': True, 'name': '_T_WM', 'path': '/', 'domain': '.weibo.cn'}, {'secure': False, 'value': '1493556087', 'httpOnly': False, 'name': 'SSOLoginState', 'path': '/', 'domain': '.weibo.cn'}, {'expiry': 1808916087.372439, 'secure': False, 'value': 'AnPRL-vKWx_-0LWAO4Mk79GSyD6FxNqsFzhSNFOZI1MxKni8Ok7C3thzDOuIdEdh-0SvYb25zbF-znxYY_Z5hK4.', 'httpOnly': True, 'name': 'SCF', 'path': '/', 'domain': '.weibo.cn'}, {'expiry': 1496148083.263736, 'secure': False, 'value': '1496148083', 'httpOnly': False, 'name': 'ALF', 'path': '/', 'domain': '.weibo.cn'}]
{'SUHB': '0cS3YKcgWrDRsV', 'SUB': '_2A250AasnDeThGeNJ6FQU8y7PwzWIHXVXDTVvrDV6PUJbktBeLRfukW0wFLR2922NnApkDOZb_eNrRfNBZQ..', 'SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9W5H8du8O9J-.X.2Zd-6LbEK5JpX5o2p5NHD95QfS0ecSKe7e0n4Ws4Dqcj.i--fiK.7iKn4i--ci-z7i-zRi--fi-2fiK.ci--4i-2pi-i2', 'SCF': 'AnPRL-vKWx_-0LWAO4Mk79GSyD6FxNqsFzhSNFOZI1MxKni8Ok7C3thzDOuIdEdh-0SvYb25zbF-znxYY_Z5hK4.', 'SSOLoginState': '1493556087', '_T_WM': 'b2d2d84c5aafcc02c0dac2faa4acc43f', 'ALF': '1496148083'}
成功获取到Cookies
Saving Cookies to Redis uva68312006hao@163.com {"SUHB": "0cS3YKcgWrDRsV", "SUB": "_2A250AasnDeThGeNJ6FQU8y7PwzWIHXVXDTVvrDV6PUJbktBeLRfukW0wFLR2922NnApkDOZb_eNrRfNBZQ..", "SUBP": "0033WrSXqPxfM725Ws9jqgMF55529P9D9W5H8du8O9J-.X.2Zd-6LbEK5JpX5o2p5NHD95QfS0ecSKe7e0n4Ws4Dqcj.i--fiK.7iKn4i--ci-z7i-zRi--fi-2fiK.ci--4i-2pi-i2", "SCF": "AnPRL-vKWx_-0LWAO4Mk79GSyD6FxNqsFzhSNFOZI1MxKni8Ok7C3thzDOuIdEdh-0SvYb25zbF-znxYY_Z5hK4.", "SSOLoginState": "1493556087", "_T_WM": "b2d2d84c5aafcc02c0dac2faa4acc43f", "ALF": "1496148083"}
```