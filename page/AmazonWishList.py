from selenium.webdriver.common.by import By
from time import sleep
from base.configuretest import BaseClass # Thanks to this importing process, I can benefit from the methods defined in BaseClass.
from page.AmazonProductPage import AmazonProduct

class AmazonWishList:

    PRODUCT_TITLE_WP = (By.CSS_SELECTOR, "//h3[@class='a-size-base']/a").text # Always will take the upper.   
    DELETE_ITEM = (By.NAME, 'submit.deleteItem')

    def __init__(self, driver): # I added driver after self, pass the argumant of the driver also.
        
        self.driver = driver # homePage = HomePage(self.driver) should be added into the test_E2E
        self.methods = BaseClass(self.driver) # Self driver is being sent, because YOU NEED it. It cant benefit from the driver definition which is in BaseClass?

    def wish_list_check(self):
    
        # Acilan sayfada bir onceki sayfada izlemeye alinmis urunun bulundugunu onaylayacak asser PRODUCT TITLE WP ASSERT TEXT PP

        assert self.PRODUCT_TITLE_PP == self.PRODUCT_TITLE_WP, "Items were added are not the same"
        self.methods.wait_for_element(self.DELETE_ITEM).click()
