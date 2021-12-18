from selenium.webdriver.common.by import By
from time import sleep
from base.configuretest import BaseClass

class AmazonCategory:
    """  Website login page for users to logging in """

    PAGES = (By.CLASS_NAME ,'a-normal') # There will be more than 1 class with this name so. It should be a list.
    PRODUCT_THIRD = (By.CSS_SELECTOR, "div[data-cel-widget='search_result_0']")
    

    def __init__(self, driver):
        
        self.driver = driver
        self.methods = BaseClass(self.driver) # Self driver is being sent, because YOU NEED it. It cant benefit from the driver definition which is in BaseClass?

    def category_page_add(self):
        
        for PAGE in self.PAGES:
            PAGE = self.PAGES.text # IMPORTANT! if you will start with // again it will start from the top of the HTML so, you should start with "" 
            if PAGE == "2":
                self.methods.wait_for_element(self.PAGE).click()
                        
        self.methods.wait_for_element(self.PRODUCT_THIRD).click()
        
    