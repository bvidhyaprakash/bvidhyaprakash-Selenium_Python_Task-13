from PageObjects.dragdrop_page import Drag_DropPage
from PageObjects.base_page import BasePage
from TestData.data import Data
from Configuration.conftest import driver_setup

def test_title(driver_setup):
    driver_setup.get(Data.url)
    driver_setup.switch_to.frame(0) # Switch to the iframe containing drag-drop elements
    base_page = BasePage(driver_setup)
    assert base_page.fetch_title() == "Droppable | jQuery UI"
    print("\nSUCCESS: Title is valid\n")

    dragdrop = Drag_DropPage(driver_setup)
    dragdrop.drag_and_drop()
