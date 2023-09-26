import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

class Grisa:
    def __init__(self):
        self.init_options()

    # options
    def init_options(self):
        self._op = webdriver.ChromeOptions() 
    
    def set_default_options(self):
        self.op_add_argument('--headless')
        self.op_add_argument('--no-sandbox')
        self.op_add_argument('--disable-dev-shm-usage')

    def op_add_argument(self, arg):
        self._op.add_argument(arg)
    
    def get_options(self):
        return self._op
    
    # service
    def init_path(self, path):
        service = Service(executable_path=os.environ.get(path))
        self.set_service(service)

    def set_service(self, service):
        self._service = service
    def get_service(self):
        return self._service
    # binary
    def init_binary(self, path):
        self.get_options().binary_location = os.environ.get(path)

    # driver
    def init_driver(self):
        driver = webdriver.Chrome(service=self.get_service(), options=self.get_options())
        self.set_driver(driver)
    
    def driver_set_url(self, url):
        self.get_driver().get(url)
    
    def driver_quit(self):
        self.get_driver().quit()
    
    def set_driver(self, driver):
        self._driver = driver

    def get_driver(self):
        return self._driver
    
    # timeout 
    def set_wait(self, sec):
        self._wait = WebDriverWait(self.get_driver(), sec)
    
    def get_wait(self):
        return self._wait

    # sleep
    @staticmethod
    def sleep(sec):
        sleep(sec)
    
    # find element by
    def find_element_by(self, type_, value):
        return self.get_wait().until(EC.presence_of_element_located((type_, value)))
    
    def accept_cookies(self):
        self.find_element_by(By.ID, 'L2AGLb').click()
    
    def search_by_image(self):
        self.find_element_by(By.CLASS_NAME, 'nDcEnd').click()
    
    

