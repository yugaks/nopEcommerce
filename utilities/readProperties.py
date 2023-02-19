import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class Readcongid:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getusername():
        username=config.get('common info', 'Username')
        return username

    @staticmethod
    def getPassword():
        password=config.get('common info', 'Password')
        return password


