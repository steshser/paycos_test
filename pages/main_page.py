import allure
from pages.locators import MainPage as mp
import pages.basepage as bp


def main_page_visibility(driver):
    with allure.step("Check visibility of main page"):
        return bp.is_element_visible(driver, mp.APP)


def click_shop_and_save_button(driver):
    with allure.step("Click on the Shop&Save button"):
        bp.find_element(driver, mp.SHOP_AND_SAVE_BUTTON).click()
