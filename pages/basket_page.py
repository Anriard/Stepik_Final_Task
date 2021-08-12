from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_not_items_added(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "There is items added to basket presented"

    def should_be_empty_items_list_added_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "Empty basket message is not presented"
