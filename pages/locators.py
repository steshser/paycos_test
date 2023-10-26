from selenium.webdriver.common.by import By


class ModalOffer:
    MODAL_OFFER = By.CLASS_NAME, "entryoverlay"
    CLOSE_BUTTON = By.CLASS_NAME, "dy-lb-close"


class MainPage:
    APP = By.ID, "app"
    SHOP_AND_SAVE_BUTTON = By.ID, "hero_shop_mattress"


class MattressPage:
    ADD_TO_CART_BUTTON = By.ID, "addtocart_btn"


class CartPage:
    ORDER_SUMMARY_HEADER = By.XPATH, "//h2[@data-testid='summary_title_collapse']"
    TOTAL_PRICE = By.ID, "total_price"
