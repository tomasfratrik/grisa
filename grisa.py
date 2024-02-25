# global
import os
import re
# selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
# local_dev
from .utils import Utils
from .identificators import PageNav, SourceImgPage  
from .scraper import Scraper

class Grisa:
    GOOGLE_REVERSE_IMG_ENGINE = 'https://www.google.com/imghp?hl=en'
    def __init__(self):
        self._op = webdriver.ChromeOptions() 
    
    def run(self, img, accept_cookies=True, local_dev=False):

        if accept_cookies:
            self._accept_cookies(local_dev=local_dev)
        Utils.sleep(2)
        self._search_by_image(local_dev=local_dev)
        if Utils.is_url(img):
            self._find_element_by(By.CLASS_NAME, PageNav.SEARCH_URL.value).send_keys(img)
            self._find_element_by(By.CLASS_NAME, PageNav.SEARCH_URL_BTN.value).click()

        else:
            self._find_element_by(By.XPATH, PageNav.SEARCH_IMG.value).send_keys(img)
        Utils.sleep(1)

    def scrape_similiar(self, page_src):
        return Scraper.scrape_similiar(page_src)
    
    def scrape_source(self, page_src):
        return Scraper.scrape_source(page_src)
    
    def go_to_source(self):
        self._find_element_by(By.CLASS_NAME, PageNav.FIND_IMG_SRC.value).click()
        self._find_element_by(By.CLASS_NAME, SourceImgPage.CONTAINER.value)

    # option
    def options_add_argument(self, arg):
        self._op.add_argument(arg)
    
    def get_options(self):
        return self._op
    
    # service
    def set_driver_path(self, path):
        service = Service(executable_path=os.environ.get(path))
        self.set_service(service)
    def set_service(self, service):
        self._service = service
    def get_service(self):
        return self._service

    # binary
    def set_binary_path(self, path):
        self.get_options().binary_location = os.environ.get(path)

    # driver
    def init_driver(self):
        driver = webdriver.Chrome(service=self.get_service(), options=self.get_options())
        self.set_driver(driver)
        self.get_driver().get(self.GOOGLE_REVERSE_IMG_ENGINE)
        self.set_wait(10)
    
    def driver_quit(self):
        self.get_driver().quit()
    
    def get_page_source(self):
        return self.get_driver().page_source
    
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
    
    def _accept_cookies(self, local_dev=False):
        elem = self._find_element_by(By.ID, PageNav.ACCEPT_COOKIES.value)
        if local_dev:
            elem.click()
        else:
            driver = self.get_driver()
            driver.execute_script("arguments[0].click();", elem)
        Utils.sleep(1)
    
    def _search_by_image(self, local_dev=False):
        elem = self._find_element_by(By.CLASS_NAME, PageNav.SEARCH_BY_IMAGE.value)
        if local_dev:
            elem.click()
        else:
            driver = self.get_driver()
            driver.execute_script("arguments[0].click();", elem)
    
    

