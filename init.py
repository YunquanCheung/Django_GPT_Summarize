"""
该文件为配置系统参数文件
"""
#  数据库配置
IS_MYSQL = True            # 是否选择MYSQL数据库，false时为sqlite
DATABASES_NAME = "GPTDJANGO"         # 数据库名
DATABASES_USER = "admin"         # 数据库用户名
DATABASES_PWD = "abcd1234"          # 数据库密码
DATABASES_HOST = "aws-rds-mysql.cy6lipekp9bd.us-east-1.rds.amazonaws.com"         # 数据库地址
DATABASES_PORT = "3306"     # 数据库端口

#   GPT配置
TEXT_LENG = 500              # 输入文本长度
GPT_KEY = "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"                 # GPT密钥
GPT_MODELS = "gpt-3.5-turbo"         # GPT模型:gpt-3.5-turbo,gpt-4
