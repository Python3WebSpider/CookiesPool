# Redis数据库地址
REDIS_HOST = 'localhost'

REDIS_PORT = 6379

REDIS_PASSWORD = 'foobared'

REDIS_DOMAIN = '*'

REDIS_NAME = '*'

# 云打码相关配置到yundama.com申请注册
YUNDAMA_USERNAME = 'Germey'

YUNDAMA_PASSWORD = ''

YUNDAMA_APP_ID = '3372'

YUNDAMA_APP_KEY = '1b586a30bfda5c7fa71c881075ba49d0'

YUNDAMA_API_URL = 'http://api.yundama.com/api.php'

YUNDAMA_MAX_RETRY = 20

# 产生器默认使用的浏览器
DEFAULT_BROWSER = 'PhantomJS'

# 产生器类
GENERATOR_MAP = {
    'weibo': 'WeiboCookiesGenerator'
}

# 测试类
TESTER_MAP = {
    'weibo': 'WeiboValidTester'
}

# 产生器和验证器循环周期
CYCLE = 120

# API地址和端口
API_HOST = '127.0.0.1'

API_PORT = 5000

# 进程开关
# 产生器
GENERATOR_PROCESS = True
# 验证器
VALID_PROCESS = False
# API
API_PROCESS = True
