"""
This base_page contains common methods like find_element, find_elements, etc.,
"""

# import all necessary dependencies
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# import the exceptions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException

class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 15
        self.action = ActionChains(self.driver)

    def find_element(self, locator):
        try:
            web_element = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))
            return web_element
        except(NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR", error)

    def drag_drop(self, source, target):
        try:
            source_element = self.find_element(source)
            target_element = self.find_element(target)

            # perform drag and drop
            self.action.drag_and_drop(source_element, target_element).perform()
            print("Successful Drag and Drop")
        except(NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR", error)

    def fetch_title(self):
        try:
            return self.driver.title
        except (NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR", error)