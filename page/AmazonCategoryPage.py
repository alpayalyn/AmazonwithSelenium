from selenium.webdriver.common.by import By
from time import sleep
from base.configuretest import BaseClass # Thanks to this importing process, I can benefit from the methods defined in BaseClass.

class AmazonCategoryPage:
    """ Website login page for users to logging in """

    SECOND_PAGE = (By.CLASS_NAME, 'a-normal')


    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver) # Self driver is being sent, because YOU NEED it. It cant benefit from the driver definition which is in BaseClass?

    def category_page_add(self):
        

    