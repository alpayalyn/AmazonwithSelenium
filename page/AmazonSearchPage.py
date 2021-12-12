from selenium.webdriver.common.by import By
from time import sleep
from base.configuretest import BaseClass # Thanks to this importing process, I can benefit from the methods defined in BaseClass.

class AmazonLogin:
    """Website login page for users to logging in"""

    textToSearch = 'samsung'
    SEARCH_BOX = (By.ID, 'twotabsearchtextbox')
    SEARCH_BUTTON = (By.ID, 'nav-search-submit-button')
    SEARCH_RESULTS = (By.CLASS_NAME, ".s-include-content-margin.s-latency-cf-section")

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver) # Self driver is being sent, because YOU NEED it. It cant benefit from the driver definition which is in BaseClass?
    
    def searching_keys(self):
        """
        
        
        """
        sleep(2)
        self.methods.wait_for_element(self.SEARCH_BOX).send_keys(self.textToSearch)
        self.methods.wait_for_element(self.SEARCH_BUTTON).click()

        # Nasıl samsung page'de olup olmadığı kesinleştirilebilir?
        for product in products:
        productName = product.find_element_by_xpath("div/h4/a").text # IMPORTANT! if you will start with // again it will start from the top of the HTML so, you should start with "" 
        if productName == "Blackberry":
            product.find_element_by_xpath("div/button").click()

        
