# global
import os
import re
from time import sleep
# selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
# local
from .utils import Utils
from .identificators import PageNav, SimiliarImgPage, SourceImgPage

class Grisa:
    def __init__(self):
        self.init_options()

    # options
    def init_options(self):
        self._op = webdriver.ChromeOptions() 
    
    def set_default_options(self):
        # self.options_add_argument('--headless')
        self.options_add_argument('--no-sandbox')
        self.options_add_argument('--disable-dev-shm-usage')

    def options_add_argument(self, arg):
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

    # find element by
    def _find_element_by(self, type_, value):
        return self.get_wait().until(EC.presence_of_element_located((type_, value)))
    
    def accept_cookies(self):
        self._find_element_by(By.ID, PageNav.ACCEPT_COOKIES.value).click()
        Utils.sleep(1)
    
    def search_by_image(self):
        self._find_element_by(By.CLASS_NAME, PageNav.SEARCH_BY_IMAGE.value).click()

    def search(self, img):

        if Utils.is_url(img):
            self._find_element_by(By.CLASS_NAME, PageNav.SEARCH_URL.value).send_keys(img)
            self._find_element_by(By.CLASS_NAME, PageNav.SEARCH_URL_BTN.value).click()

        else:
            self._find_element_by(By.CLASS_NAME, PageNav.SEARCH_IMG).send_keys(img)
    

