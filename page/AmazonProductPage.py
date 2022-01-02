from selenium.webdriver.common.by import By
from time import sleep
from base.configuretest import BaseClass # Thanks to this importing process, I can benefit from the methods defined in BaseClass.
from page.AmazonHomePage import AmazonHome

class AmazonProduct(AmazonHome):
    """Website login page for users to logging in"""

    WISH_LIST = (By.ID, 'wishlistButtonStack')
    WISH_LIST_LINK = (By.ID, "WLHUC_result_listName")
    STORAGE = []



    def __init__(self):
        super().__init__()

    def product_add(self):
        
        self.methods.wait_for_element(self.WISH_LIST).click()
        self.methods.wait_for_element(self.WISH_LIST_LINK).click()




    