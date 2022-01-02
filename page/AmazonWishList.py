from selenium.webdriver.common.by import By
from time import sleep
from base.configuretest import BaseClass # Thanks to this importing process, I can benefit from the methods defined in BaseClass.
from page.AmazonProductPage import AmazonProduct
from page.AmazonHomePage import AmazonHome

class AmazonWishList(AmazonHome):

    PRODUCT_TITLE_PP = (By.ID, 'productTitle').text()
    CART_PRODUCT_LIST = (By.CLASS_NAME, 'g-item-sortable')
    DELETE_ITEM = (By.NAME, 'submit.deleteItem')
    ITERATION = 0

    def __init__(self): # I added driver after self, pass the argumant of the driver also.
        super().__init__()

    def wish_list_check(self):

        print("hi")
        # Acilan sayfada bir onceki sayfada izlemeye alinmis urunun bulundugunu onaylayacak asser PRODUCT TITLE WP ASSERT TEXT PP

    def clicked_to_the_second(self): # Assert için gerekli
        for PRODUCT in self.CART_PRODUCT_LIST:
            PRODUCT = self.CART_PRODUCT_LIST[self.ITERATION].text() # IMPORTANT! if you will start with // again it will start from the top of the HTML so, you should start with "" 
            if PRODUCT == self.PRODUCT_TITLE_PP:
                break
            self.ITERATION = self.ITERATION + 1 
            break

    def delete_item(self):  
        self.methods.wait_for_element(self.DELETE_ITEM)[self.ITERATION].click()
        self.ITERATION = 0
