import configparser

config = configparser.RawConfigParser()
config.read('.\\Configurations\\config.ini')


class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('common Info', 'baseURL')
        return url