import pytest
from pages.login_page import LoginPage
from utils.test_data import TestData

class TestAuthorization:

    def test_valid_login_by_phone(self, driver, base_url):
        login_page = LoginPage(driver, base_url)
        login_page.open()
        login_page.select_tab("телефон")
        login_page.enter_username(TestData.VALID_PHONE)
        login_page.enter_password(TestData.VALID_PASSWORD)
        login_page.submit()
        # После успешного входа должно произойти перенаправление
        assert "account_b2c" in driver.current_url or "redirect" in driver.current_url

    def test_invalid_password(self, driver, base_url):
        login_page = LoginPage(driver, base_url)
        login_page.open()
        login_page.select_tab("телефон")
        login_page.enter_username(TestData.VALID_PHONE)
        login_page.enter_password(TestData.WRONG_PASSWORD)
        login_page.submit()
        assert "Неверный логин или пароль" in login_page.get_error_text()
        assert login_page.is_forgot_password_orange()

    def test_auto_tab_switching(self, driver, base_url):
        login_page = LoginPage(driver, base_url)
        login_page.open()
        login_page.enter_username("+79261234567")
        assert "Телефон" == login_page.get_active_tab_text()
        login_page.clear_username()
        login_page.enter_username("test@mail.ru")
        assert "Почта" == login_page.get_active_tab_text()
        login_page.clear_username()
        login_page.enter_username("user123")
        assert "Логин" == login_page.get_active_tab_text()
        login_page.clear_username()
        login_page.enter_username("1234567890")
        assert "Лицевой счёт" == login_page.get_active_tab_text()

    def test_valid_login_by_email(self, driver, base_url):
        login_page = LoginPage(driver, base_url)
        login_page.open()
        login_page.select_tab("почта")
        login_page.enter_username(TestData.VALID_EMAIL)
        login_page.enter_password(TestData.VALID_PASSWORD)
        login_page.submit()
        assert "account_b2c" in driver.current_url

    def test_valid_login_by_login(self, driver, base_url):
        login_page = LoginPage(driver, base_url)
        login_page.open()
        login_page.select_tab("логин")
        login_page.enter_username(TestData.VALID_LOGIN)
        login_page.enter_password(TestData.VALID_PASSWORD)
        login_page.submit()
        assert "account_b2c" in driver.current_url

    def test_valid_login_by_ls(self, driver, base_url):
        # Требуется аккаунт с ЛС, заглушка
        pass