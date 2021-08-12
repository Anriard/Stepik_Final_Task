from selenium.webdriver.common.by import By


# class MainPageLocators():
#     LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


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
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "[class = 'btn-group'] > [class = 'btn btn-default']")


class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, "[class = 'basket_summary']")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "[id = 'content_inner'] > P")


