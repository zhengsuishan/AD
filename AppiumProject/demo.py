import logging
from appium impor
class LogConfig:
    @staticmethod
    def init(path):
        global logger

        if not os.path.exists('./log'):
            os.mkdir('./log')

        nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(levelname)s %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S',
                            filename = './log/'+nowTime+'.log',
                            filemode='a')
        logger = logging.getLogger()


    @staticmethod
    def getLogger():
        return logger

if __name__ == '__main__':
    LogConfig.init()
    LogConfig.getLogger()

