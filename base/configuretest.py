import random
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BaseClass(object):
    """Base class to initialize the base page that will be called from all pages"""

    ALLOW_OPTIN = (By.CSS_SELECTOR, '#optInText')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 35)

    def wait_for_element(self, selector):
        """
        Wait for element to present
        :param selector: locator of the element to find.
        """
        return self.wait.until(ec.element_to_be_clickable(selector))

    def presence_for_element(self, selector):
        """
        Presence for element to present
        :param selector: locator of the element to find
        """
        return self.wait.until(ec.presence_of_element_located(selector))

    def wait_till_element_dissappears(self, selector):
        """
        Wait for element to disappears
        :param selector: locator of the element to find
        """
        return self.wait.until(ec.invisibility_of_element_located(selector))

































import pytest
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
# use conftest when the feature you are oging to use will be used by multiple test cases.
# by using below code we will be able to change the browser that we use by command line
# in the command screen by passing --browser_name firefox or chrome you will open the specific browser thanks to below code.
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action = "store", default = "chrome"
        
    )

# request is an instance for your fixture " when you declare an fixture, request will be its instance"
# before starting the test this part of code will be executed and the config will be handle at the beginning.

@pytest.fixture(scope="class")  # scope means we used the fixture at class level.
def setup(request):
    browser_name = request.config.getOption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:/seleniumdriver/chromedriver")
    elif browser_name == "firefox":
        # firefox invocation Gecko Driver
        driver = webdriver.Chrome(executable_path="C:/seleniumdriver/chromedriver")
    elif browser_name == "IE":
        # IE driver
        driver = webdriver.Chrome(executable_path="C:/seleniumdriver/chromedriver")

    driver.get("https://amazon.com")
    driver.maximize_window()


    request.cls.driver = driver # this is how you can pass the driver from your fixture to the test case (self. will be put in test case python file too)
    yield  # thanks to yield after the above code will be executed and then the main code will be executed in another python file and then below close
    driver.close()
