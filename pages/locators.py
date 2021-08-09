from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE = (By.CLASS_NAME, "price_color")
    PRODUCT_IN_BASKET_NAME = (By.CSS_SELECTOR, ".alertinner > strong")
    PRODUCT_IN_BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner > p > strong")
    ADD_TO_BASKET_LINK = (By.CSS_SELECTOR, "[class='btn btn-lg btn-primary btn-add-to-basket']")

