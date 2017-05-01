# Redis数据库地址
REDIS_HOST = 'localhost'

# Redis端口
REDIS_PORT = 6379

# Redis密码，如无填None
REDIS_PASSWORD = 'foobared'

# 配置信息，无需修改
REDIS_DOMAIN = '*'
REDIS_NAME = '*'

# 云打码相关配置到yundama.com申请注册
YUNDAMA_USERNAME = 'Germey'
YUNDAMA_PASSWORD = '940629cqc'
YUNDAMA_APP_ID = '3372'
YUNDAMA_APP_KEY = '1b586a30bfda5c7fa71c881075ba49d0'

YUNDAMA_API_URL = 'http://api.yundama.com/api.php'

# 云打码最大尝试次数
YUNDAMA_MAX_RETRY = 20

# 产生器默认使用的浏览器
DEFAULT_BROWSER = 'Chrome'

# 产生器类，如扩展其他站点，请在此配置
GENERATOR_MAP = {
    'weibo': 'WeiboCookiesGenerator'
}

# 测试类，如扩展其他站点，请在此配置
TESTER_MAP = {
    'weibo': 'WeiboValidTester'
}

# 产生器和验证器循环周期
CYCLE = 120

# API地址和端口
API_HOST = '127.0.0.1'
API_PORT = 5000

# 进程开关
# 产生器，模拟登录添加Cookies
GENERATOR_PROCESS = False
# 验证器，循环检测数据库中Cookies是否可用，不可用删除
VALID_PROCESS = False
# API接口服务
API_PROCESS = True
