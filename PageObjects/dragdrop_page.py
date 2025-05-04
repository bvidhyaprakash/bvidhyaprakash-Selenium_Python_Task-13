from selenium.webdriver.common.by import By
from PageObjects.base_page import BasePage
from TestLocator.locator import Locator

class Drag_DropPage(BasePage):
    DRAG_ELEMENT = (By.ID, Locator.source)
    DROP_ELEMENT = (By.ID, Locator.target)

    def drag_and_drop(self):
        self.drag_drop(self.DRAG_ELEMENT, self.DROP_ELEMENT)