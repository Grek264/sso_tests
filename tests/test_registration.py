from pages.registration_page import RegistrationPage
from pages.code_page import CodePage
from utils.test_data import TestData


class TestRegistration:

    def test_required_fields(self, driver, base_url):
        reg_page = RegistrationPage(driver, base_url)
        reg_page.open("/auth/realms/b2c/login-actions/registration?client_id=account_b2c&tab_id=test")
        reg_page.click_register()
        assert reg_page.is_element_visible(reg_page.ERROR_FIRST_NAME)
        assert reg_page.is_element_visible(reg_page.ERROR_LAST_NAME)
        assert reg_page.is_element_visible(reg_page.ERROR_ADDRESS)
        assert reg_page.is_element_visible(reg_page.ERROR_PASSWORD)
        assert reg_page.is_element_visible(reg_page.ERROR_CONFIRM)

    def test_password_policy_length(self, driver, base_url):
        reg_page = RegistrationPage(driver, base_url)
        reg_page.open("/auth/realms/b2c/login-actions/registration?client_id=account_b2c&tab_id=test")
        reg_page.fill_first_name(TestData.FIRST_NAME)
        reg_page.fill_last_name(TestData.LAST_NAME)
        reg_page.select_region(TestData.REGION)
        reg_page.fill_address(TestData.NEW_EMAIL)
        reg_page.fill_password("Abc1")
        reg_page.fill_confirm_password("Abc1")
        reg_page.click_register()
        assert "Длина пароля должна быть не менее 8 символов" in reg_page.get_error(reg_page.ERROR_PASSWORD)

    def test_password_no_uppercase(self, driver, base_url):
        reg_page = RegistrationPage(driver, base_url)
        reg_page.open("/auth/realms/b2c/login-actions/registration?client_id=account_b2c&tab_id=test")
        reg_page.fill_first_name(TestData.FIRST_NAME)
        reg_page.fill_last_name(TestData.LAST_NAME)
        reg_page.select_region(TestData.REGION)
        reg_page.fill_address(TestData.NEW_EMAIL)
        reg_page.fill_password("abcdefgh1")
        reg_page.fill_confirm_password("abcdefgh1")
        reg_page.click_register()
        assert "Пароль должен содержать хотя бы одну заглавную букву" in reg_page.get_error(reg_page.ERROR_PASSWORD)

    def test_password_non_latin(self, driver, base_url):
        reg_page = RegistrationPage(driver, base_url)
        reg_page.open("/auth/realms/b2c/login-actions/registration?client_id=account_b2c&tab_id=test")
        reg_page.fill_first_name(TestData.FIRST_NAME)
        reg_page.fill_last_name(TestData.LAST_NAME)
        reg_page.select_region(TestData.REGION)
        reg_page.fill_address(TestData.NEW_EMAIL)
        reg_page.fill_password("Абвгдеёж1")
        reg_page.fill_confirm_password("Абвгдеёж1")
        reg_page.click_register()
        assert "Пароль должен содержать только латинские буквы" in reg_page.get_error(reg_page.ERROR_PASSWORD)

    def test_password_mismatch(self, driver, base_url):
        reg_page = RegistrationPage(driver, base_url)
        reg_page.open("/auth/realms/b2c/login-actions/registration?client_id=account_b2c&tab_id=test")
        reg_page.fill_first_name(TestData.FIRST_NAME)
        reg_page.fill_last_name(TestData.LAST_NAME)
        reg_page.select_region(TestData.REGION)
        reg_page.fill_address(TestData.NEW_EMAIL)
        reg_page.fill_password("ExamplePass123")
        reg_page.fill_confirm_password("ExamplePass124")
        reg_page.click_register()
        assert "Пароли не совпадают" in reg_page.get_error(reg_page.ERROR_CONFIRM)

    def test_successful_registration(self, driver, base_url):
        reg_page = RegistrationPage(driver, base_url)
        reg_page.open("/auth/realms/b2c/login-actions/registration?client_id=account_b2c&tab_id=test")
        reg_page.fill_first_name(TestData.FIRST_NAME)
        reg_page.fill_last_name(TestData.LAST_NAME)
        reg_page.select_region(TestData.REGION)
        reg_page.fill_address(TestData.NEW_EMAIL)
        reg_page.fill_password(TestData.NEW_PASSWORD)
        reg_page.fill_confirm_password(TestData.NEW_PASSWORD)
        reg_page.click_register()

        code_page = CodePage(driver, base_url)
        masked_contact = code_page.get_masked_contact()
        assert "***@" in masked_contact
        assert code_page.is_resend_button_visible()
