from time import sleep
import re

class Utils:
    @staticmethod
    def is_url(string):
        URL_REGEX = r'^(http|https):\/\/.*'
        if re.match(URL_REGEX, string):
            return True
        return False

    @staticmethod
    def sleep(sec):
        sleep(sec)