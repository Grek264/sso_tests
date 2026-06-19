import pytest
from selenium.webdriver.common.by import By

class TestProductMatrix:

    @pytest.mark.parametrize("product_url, expected_tabs", [
        ("https://lk.rt.ru/", ["Телефон", "Почта", "Логин", "Лицевой счёт"]),
        ("https://my.rt.ru/", ["Телефон", "Почта", "Логин"]),
        ("https://lk.smarthome.rt.ru/", ["Телефон", "Почта", "Логин"])
    ])
    def test_available_tabs(self, driver, product_url, expected_tabs):
        driver.get(product_url)
        tabs = driver.find_elements(By.XPATH, "//div[contains(@class, 'rt-tab')]")
        tab_texts = [t.text for t in tabs]
        assert set(tab_texts) == set(expected_tabs)