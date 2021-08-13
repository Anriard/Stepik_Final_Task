from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket_and_compare_name_and_price(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

        add_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_LINK)
        add_link.click()
        print("Product added to basket")

        self.solve_quiz_and_get_code()

        product_in_basket_name = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET_NAME).text
        product_in_basket_price = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET_PRICE).text

        assert product_name == product_in_basket_name, "Product name in product page" \
                                                       " and product name in basket didn`t match"
        assert product_price == product_in_basket_price, "Product price in product page" \
                                                         " and product price in basket didn`t match"

    def add_product_to_basket(self):
        add_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_LINK)
        add_link.click()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"






