# CookiesPool / Cookies池

可扩展的Cookies池，目前对接了新浪微博，[m.weibo.cn](https://m.weibo.cn)，可自行扩展其他站点


## 安装

```
pip3 install -r requirements.txt
```

## 基础配置 

在config.py修改

```python
# Redis数据库地址
REDIS_HOST = 'localhost'

# Redis端口
REDIS_PORT = 6379

# Redis密码，如无填None
REDIS_PASSWORD = 'foobared'

# 产生器使用的浏览器
BROWSER_TYPE = 'Chrome'

# 产生器类，如扩展其他站点，请在此配置
GENERATOR_MAP = {
    'weibo': 'WeiboCookiesGenerator'
}

# 测试类，如扩展其他站点，请在此配置
TESTER_MAP = {
    'weibo': 'WeiboValidTester'
}

TEST_URL_MAP = {
    'weibo': 'https://m.weibo.cn/api/container/getIndex?uid=1804544030&type=uid&page=1&containerid=1076031804544030'
}

# 产生器和验证器循环周期
CYCLE = 120

# API地址和端口
API_HOST = '0.0.0.0'
API_PORT = 5000


```


### 进程开关

在config.py修改

```python
# 产生器开关，模拟登录添加Cookies
GENERATOR_PROCESS = True
# 验证器开关，循环检测数据库中Cookies是否可用，不可用删除
VALID_PROCESS = True
# API接口服务
API_PROCESS = True
```


## 账号购买

账号可在淘宝购买

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

三个进程全部开启：


```
API接口开始运行
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
Cookies生成进程开始运行
Cookies检测进程开始运行
正在生成Cookies 账号 14747223314 密码 asdf1129
正在测试Cookies 用户名 14747219309
Cookies有效 14747219309
部分测试结果 {"cardlistInfo":{"containerid":"1076031804544030",
正在测试Cookies 用户名 14740626332
Cookies有效 14740626332
部分测试结果 {"cardlistInfo":{"containerid":"1076031804544030",
正在测试Cookies 用户名 14740691419
Cookies有效 14740691419
部分测试结果 {"cardlistInfo":{"containerid":"1076031804544030",
正在测试Cookies 用户名 14740618009
Cookies有效 14740618009
部分测试结果 {"cardlistInfo":{"containerid":"1076031804544030",
Cookies有效 14740636046
部分测试结果 {"cardlistInfo":{"containerid":"1076031804544030",
正在测试Cookies 用户名 14747222472
Cookies有效 14747222472
部分测试结果 {"cardlistInfo":{"containerid":"1076031804544030",
Cookies检测完成
验证码位置 420 580 384 544
成功匹配
拖动顺序 [1, 4, 2, 3]
成功获取到Cookies {'SUHB': '08J77UIj4w5n_T', 'SCF': 'AimcUCUVvHjswSBmTswKh0g4kNj4K7_U9k57YzxbqFt4SFBhXq3Lx4YSNO9VuBV841BMHFIaH4ipnfqZnK7W6Qs.', 'SSOLoginState': '1501439488', '_T_WM': '99b7d656220aeb9207b5db97743adc02', 'M_WEIBOCN_PARAMS': 'uicode%3D20000174', 'SUB': '_2A250elZQDeRhGeBM6VAR8ifEzTuIHXVXhXoYrDV6PUJbkdBeLXTxkW17ZoYhhJ92N_RGCjmHpfv9TB8OJQ..'}
成功保存Cookies
```

## 运行

```
python3 run.py
```