from selenium.webdriver.common.by import By
from time import sleep
from base.configuretest import BaseClass
from test.amazon_setup import BasePage

class AmazonLogin:
    """Website login page for users to logging in"""

    email = 'alpaylui78@gmail.com'
    password = 'Zemmenilone123'
    EMAIL = (By.ID, 'ap_email')
    PASS_EMAIL = (By.ID, 'continue')
    PASSWORD = (By.ID, 'ap_password')
    PASS_PASSWORD = (By.ID, 'signInSubmit')

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver) # Self driver is being sent, because YOU NEED it. It cant benefit from the driver definition which is in BaseClass?

    
    def amazon_login(self):
        """Logging into the account."""
        sleep(2)
        BasePage
        self.methods.wait_for_element(self.EMAIL).send_keys(self.email)
        self.methods.wait_for_element(self.PASS_EMAIL).click()
        self.methods.wait_for_element(self.PASSWORD).send_keys(self.password)
        self.methods.wait_for_element(self.PASS_PASSWORD).click()
    


        