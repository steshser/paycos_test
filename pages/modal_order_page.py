import allure
from pages.locators import ModalOffer as mo
import pages.basepage as bp


def modal_offer_visibility(driver):
    with allure.step("Check visibility of modal offer"):
        return bp.is_element_visible(driver, mo.MODAL_OFFER)


def click_close_button(driver):
    with allure.step("Click on the modal order close button"):
        bp.find_element(driver, mo.CLOSE_BUTTON).click()