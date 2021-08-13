from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_LINK), "Login link is not presented"
        assert "/login" in self.url,  "Login is not presented in URL"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        assert True

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_FORM)
        email_field.send_keys(email)
        password1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1_FORM)
        password1.send_keys(password)
        password2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2_FORM)
        password2.send_keys(password)
        submit_registration_button = self.browser.find_element(*LoginPageLocators.SUBMIT_REGISTRATION_BUTTON)
        submit_registration_button.click()
