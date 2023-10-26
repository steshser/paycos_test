import allure
from pages.locators import CartPage as cp
import pages.basepage as bp


def order_summary_header_visibility(driver):
    with allure.step("Check visibility of order summary header"):
        return bp.is_element_visible(driver, cp.ORDER_SUMMARY_HEADER)


def get_total_price(driver):
    with allure.step("Get total price value"):
        return bp.find_element(driver, cp.TOTAL_PRICE).text
