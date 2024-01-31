
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

from selenium.webdriver.firefox.options import Options

from functools import cache 
#from webdriver_manager.firefox import GeckoDriverManager  # Note "GeckoDriverManager"

class fox:
    
    def __init__(self):
        self.instance=False
    def launch(self):
        options=Options()
        options.add_argument("--headless")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        driver = webdriver.Firefox(options=options)#,service=Service(GeckoDriverManager().install()))
        driver.get("http://127.0.0.1:5500/scarp-1.html")
        self.driver=driver
        print("Window created")
        self.instance = True
        
# =============================================================================
#     @cache
# =============================================================================
    def login(self):
        elem=self.driver.find_element(By.ID,'username')
        elem2=self.driver.find_element(By.ID,'password')
        elem3=self.driver.find_element(By.ID,'loginbutton')
        elem.clear()
        elem2.clear()
        elem.send_keys("")
        elem2.send_keys("")
        elem3.click()
        print("Logged-IN")
        



