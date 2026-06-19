import pytest
from pages.recovery_page import RecoveryPage
from utils.test_data import TestData
from selenium.webdriver.common.by import By

class TestRecovery:

    def test_phone_tab_default(self, driver, base_url):
        rec_page = RecoveryPage(driver, base_url)
        rec_page.open("/auth/realms/b2c/login-actions/reset-credentials?client_id=account_b2c&tab_id=test")
        active = rec_page.driver.find_element(By.XPATH, "//div[contains(@class, 'rt-tab--active')]")
        assert "Телефон" in active.text

    def test_switch_tabs(self, driver, base_url):
        rec_page = RecoveryPage(driver, base_url)
        rec_page.open("/auth/realms/b2c/login-actions/reset-credentials?client_id=account_b2c&tab_id=test")
        rec_page.select_tab("почта")
        placeholder = rec_page.driver.find_element(By.ID, "username").get_attribute("placeholder")
        assert "Электронная почта" in placeholder or "Почта" in placeholder

    def test_captcha_required(self, driver, base_url):
        rec_page = RecoveryPage(driver, base_url)
        rec_page.open("/auth/realms/b2c/login-actions/reset-credentials?client_id=account_b2c&tab_id=test")
        rec_page.enter_username(TestData.RECOVERY_PHONE)
        rec_page.click_next()
        error = rec_page.driver.find_element(By.XPATH, "//input[@id='captcha']/following-sibling::span[contains(@class, 'error')]")
        assert "Обязательное поле" in error.text or "Введите символы" in error.text

    def test_invalid_phone_format(self, driver, base_url):
        rec_page = RecoveryPage(driver, base_url)
        rec_page.open("/auth/realms/b2c/login-actions/reset-credentials?client_id=account_b2c&tab_id=test")
        rec_page.enter_username("123")
        rec_page.click_next()
        error = rec_page.driver.find_element(By.XPATH, "//input[@id='username']/following-sibling::div[contains(@class, 'error')]")
        assert "Неверный формат" in error.text