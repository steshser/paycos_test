import allure
from pages.locators import MattressPage as mp
import pages.basepage as bp


def modal_offer_visibility(driver):
    with allure.step("Check visibility of add to cart button"):
        return bp.is_element_visible(driver, mp.ADD_TO_CART_BUTTON)


def click_add_to_cart_button(driver):
    with allure.step("Click on the Add to cart button"):
        bp.find_element(driver, mp.ADD_TO_CART_BUTTON).click()
