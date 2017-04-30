# CookiesPool / Cookies池

## 安装

```
pip3 install -r requirements.txt
```

## 基础配置 

修改cookiespool/config.py

### 数据库配置

account:weibo:账号

cookies:weibo:账号

类型都是list，内容分别为密码和Cookies

![](https://ww1.sinaimg.cn/large/006tNbRwly1ff506wv38aj30jj05sq32.jpg)

![](https://ww4.sinaimg.cn/large/006tNbRwly1ff507mobqcj30ra06sweu.jpg)

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

![](https://ww2.sinaimg.cn/large/006tNbRwly1ff50gt9j0hj30r20jy763.jpg)
