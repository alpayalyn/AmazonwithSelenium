from selenium.webdriver.common.by import By
from time import sleep
from base.configuretest import BaseClass

class AmazonHome:
    """  Website login page for users to logging in """


    def __init__(self, driver):
        
        self.driver = driver
        self.methods = BaseClass(self.driver) # Self driver is being sent, because YOU NEED it. It cant benefit from the driver definition which is in BaseClass?

    def homepage_check(self):

        URL = self.methods.driver.getCurrentUrl()


        

    