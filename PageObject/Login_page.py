from selenium import webdriver
from selenium.webdriver.common.by import By

from Locators.Locators import SwagLabslocators
from Test_Data.Data import SwagLabsData

class SwaglabsLogin:

    driver = webdriver.Chrome()

    def start(self):
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get(SwagLabsData.url)
        return True
    
    def Login(self):
        self.driver.find_element(by=By.ID, value=SwagLabslocators.username_locator).send_keys(SwagLabsData.username)
        self.driver.find_element(by=By.ID,value=SwagLabslocators.password_locator).send_keys(SwagLabsData.password)
        self.driver.find_element(by=By.ID,value=SwagLabslocators.login_button_locator).click()
        return True
    
    def backpack_add(self):
        backpack_element=self.driver.find_element(by=By.XPATH,value=SwagLabslocators.backpack_locator)
        

    
    def shutdown(self):
        self.driver.quit()
        return None


