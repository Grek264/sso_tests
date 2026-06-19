from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RegistrationPage(BasePage):
    INPUT_FIRST_NAME = (By.NAME, "firstName")
    INPUT_LAST_NAME = (By.NAME, "lastName")
    REGION_DROPDOWN = (By.CLASS_NAME, "rt-select")
    REGION_OPTIONS = (By.XPATH, "//div[contains(@class, 'rt-select-option')]")
    INPUT_ADDRESS = (By.ID, "address")
    INPUT_PASSWORD = (By.ID, "password")
    INPUT_CONFIRM_PASSWORD = (By.ID, "password-confirm")
    BUTTON_REGISTER = (By.NAME, "register")
    BUTTON_BACK = (By.NAME, "gotoLogin")

    # Ошибки валидации (под полями)
    ERROR_FIRST_NAME = (By.XPATH, "//input[@name='firstName']/following-sibling::div[contains(@class, 'error')]")
    ERROR_LAST_NAME = (By.XPATH, "//input[@name='lastName']/following-sibling::div[contains(@class, 'error')]")
    ERROR_ADDRESS = (By.XPATH, "//input[@id='address']/following-sibling::div[contains(@class, 'error')]")
    ERROR_PASSWORD = (By.XPATH, "//input[@id='password']/following-sibling::div[contains(@class, 'error')]")
    ERROR_CONFIRM = (By.XPATH, "//input[@id='password-confirm']/following-sibling::div[contains(@class, 'error')]")

    def fill_first_name(self, name):
        self.wait_for_element(self.INPUT_FIRST_NAME).send_keys(name)

    def fill_last_name(self, surname):
        self.wait_for_element(self.INPUT_LAST_NAME).send_keys(surname)

    def select_region(self, region_text):
        self.wait_for_clickable(self.REGION_DROPDOWN).click()
        options = self.driver.find_elements(*self.REGION_OPTIONS)
        for opt in options:
            if opt.text.strip() == region_text:
                opt.click()
                break

    def fill_address(self, address):
        self.wait_for_element(self.INPUT_ADDRESS).send_keys(address)

    def fill_password(self, password):
        self.wait_for_element(self.INPUT_PASSWORD).send_keys(password)

    def fill_confirm_password(self, password):
        self.wait_for_element(self.INPUT_CONFIRM_PASSWORD).send_keys(password)

    def click_register(self):
        self.wait_for_clickable(self.BUTTON_REGISTER).click()

    def click_back(self):
        self.wait_for_clickable(self.BUTTON_BACK).click()

    def get_error(self, locator):
        return self.get_text(locator)