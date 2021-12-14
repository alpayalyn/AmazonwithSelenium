from selenium.webdriver.common.by import By
from time import sleep
from base.configuretest import BaseClass # Thanks to this importing process, I can benefit from the methods defined in BaseClass.

class AmazonProduct:
    """Website login page for users to logging in"""

    WISH_LIST = (By.ID, 'wishlistButtonStack')
    WISH_LIST_LINK = (By.ID, "WLHUC_result_listName")
    STORAGE = []
    PRODUCT_TITLE_PP = (By.CSS_SELECTOR, "span[@id='productTitle']").text


    def __init__(self, driver):
        
        self.driver = driver
        self.methods = BaseClass(self.driver) # Self driver is being sent, because YOU NEED it. It cant benefit from the driver definition which is in BaseClass?

    def product_add(self):
        
        self.methods.wait_for_element(self.WISH_LIST).click()
        self.methods.wait_for_element(self.WISH_LIST_LINK).click()


    