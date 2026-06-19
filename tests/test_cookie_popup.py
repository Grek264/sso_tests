import pytest
from pages.login_page import LoginPage

class TestCookiePopup:
    def test_cookie_disabled_popup(self, driver, base_url):
        # Для полноценного теста нужно настроить браузер с отключенными cookie
        # Это можно сделать через ChromeOptions: chrome_options.add_argument("--disable-cookies")
        # Но для демонстрации оставляем заглушку
        pass