import unittest
from test.amaz

class AmazonAlpayPath(unittest.TestCase, Setup):
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
        Setup.__init(self)



if __name__ == "__main__":
    unittest.main()