from selenium.webdriver.common.by import By
from time import sleep
from base.configuretest import BaseClass

class AmazonHome:
    """  Website login page for users to logging in """
    LOGIN_SCREEN = (By.ID, "nav-link-accountList")
    CHROME_EXECUTABLE_PATH = "C:/seleniumdriver/chromedriver"
    BASE_URL = "https://www.amazon.com"
    HOMEPAGE_TITLE = "Amazon.com"



    def __init__(self, driver): # bu driver nereden geliyor, bir noktadan gelmek zorunda mı?
        
        self.driver = driver
        self.methods = BaseClass(self.driver) # Self driver is being sent, because YOU NEED it. It cant benefit from the driver definition which is in BaseClass?
    
    def test_home_page_loaded_successfully(self):
        # instantiate an object of HomePage class. Remember when the constructor of HomePage class is called
        # it opens up the browser and navigates to Home Page of the site under test.
        self.methods.driver.get(self.BASE_URL) # Open the web page
        # assert if the title of Home Page contains Amazon.com

    def navigating_to_login_page(self):
        self.methods.wait_for_element(self.LOGIN_SCREEN).click()

        


        

    