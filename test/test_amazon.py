import unittest
from test import amazon_setup
from page.AmazonHomePage import AmazonHomePage
from page.AmazonLoginPage import AmazonLoginPage
from page.AmazonSearchPage import AmazonSearchPage
from page.AmazonCategoryPage import AmazonCategoryPage
from page.AmazonProductPage import AmazonProductPage
from page.AmazonWishList import AmazonWishList



class Test_Amazon(unittest.TestCase, Setup):
    """Test case is:
    1. Go to given URL, Check the page we land is, Homepage or not by Assertion
    2. Open Login screen log into an account.
    3. Type 'Samsung' to Search section and click to Search button.
    4. Validate there are results belong to 'samsung' search by Assertion. (However you wish.)
    5. From the results of search page you will click to 2nd page of it. And You will validate that you are on 2nd Page of search page.
    6. Click to the 'Add to List' button of 3rd Item from upper side.
    7. Then It will click, to the 'List' Link from above part. And Choose the 'Wish List'
    8. And on WishList, you will validate that, you added correct item from product page to WishList VALIDATION
    9. Then you will delete this item by using delete button next to it.
    10. And you will Validate that, deleted item is no longer in the WishList and TearDown

    """

    def setUp(self):
        Setup.__init__(self) # TRACK WHERE THE SETUP GOES TO!!!! amazon_setup içinde site açılacak-

        # Nasıl start vereceksin teste, driver get nereden başlayacak onu belirlemen gerek.

    def test_amazon(self):        
        self.assertIn(AmazonHomePage.HOME_PAGE_TITLE, self.homePage.driver.title)
        # AmazonHomePage içerisindeki title değişkenine nasıl ulaşabilirsin onu düşün.
        # homePage burada instance bir object bunun üzerinden driver.title çekimi var.
        self.AmazonHomePage.amazon_login()
        self.AmazonSearch.
        self.assertIn(AmazonHomePage.HOME_PAGE_TITLE, self.homePage.driver.title)
        self.A

        self.assertNotIn(TestData.NO_RESULTS_TEXT,self.searchResultsPage.driver.page_source) # no result and the other text should be fetch from the .py


if __name__ == "__main__":
    unittest.main()