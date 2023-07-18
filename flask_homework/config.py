import os
from dotenv import load_dotenv

load_dotenv()


class AppConfigData:

    DEBUG = os.getenv('DEBUG') == 'True'
    SECRET_KEY = os.getenv('SECRET_KEY')
    HOST = os.getenv('HOST')
    PORT = int(os.getenv('PORT'))
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE')

    def __init__(self):
        self.config = self.set_config()

    def set_config(self):
        config = {
            'debug': self.DEBUG,
            'host': self.HOST,
            'port': self.PORT,
            'secret_key': self.SECRET_KEY,
            'SQLALCHEMY_DATABASE_URI': self.SQLALCHEMY_DATABASE_URI
        }
        return config


if __name__ == '__main__':
    print(AppConfigData().config)
