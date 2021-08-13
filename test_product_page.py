from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
import pytest
import time
from .pages.basket_page import BasketPage


@pytest.mark.parametrize('link', [r"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  r"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  r"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  r"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  r"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  r"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  r"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      r"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
                                      "?promo=offer7",
                                      marks=pytest.mark.xfail(reason="known bug")),
                                  r"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  r"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket_and_compare_name_and_price()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.message_should_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_be_not_items_added()
    page.should_be_empty_items_list_added_message()


@pytest.mark.login
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = "Tester01Tester01"
        page.register_new_user(email=email, password=password)

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket_and_compare_name_and_price()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
