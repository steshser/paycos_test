import allure
import pytest
from allure_commons.types import AttachmentType
import constants as c
from pages import modal_order_page, main_page, mattress_page, cart_page


@allure.feature("Add cart")
@pytest.mark.ui
def test_add_cart(driver):
    try:
        with allure.step("Open website https://qa.awarasleep.com/"):
            driver.get(c.URL_UI)
        assert main_page.main_page_visibility(driver)
        # Шаг добавлен для стабильности теста
        if modal_order_page.modal_offer_visibility(driver):
            modal_order_page.click_close_button(driver)
        main_page.click_shop_and_save_button(driver)
        assert "/mattress" in driver.current_url
        mattress_page.click_add_to_cart_button(driver)
        assert cart_page.order_summary_header_visibility(driver)
        assert cart_page.get_total_price(driver)[1:] != "0"
    except Exception as exc:
        allure.attach(driver.get_screenshot_as_png(), name=f"Error screenshot: {exc.args[0]}",
                      attachment_type=AttachmentType.JPG)
        raise


