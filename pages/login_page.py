from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    # Табы
    TAB_PHONE = (By.ID, "t-btn-tab-phone")
    TAB_EMAIL = (By.ID, "t-btn-tab-mail")
    TAB_LOGIN = (By.ID, "t-btn-tab-login")
    TAB_LS = (By.ID, "t-btn-tab-ls")

    # Поля
    INPUT_USERNAME = (By.ID, "username")
    INPUT_PASSWORD = (By.ID, "password")
    CHECKBOX_REMEMBER = (By.NAME, "rememberMe")
    BUTTON_SUBMIT = (By.NAME, "login")
    FORGOT_PASSWORD_LINK = (By.ID, "forgot_password")
    REGISTER_LINK = (By.ID, "kc-register")

    # Ошибка (общий локатор)
    ERROR_MESSAGE = (By.XPATH, "//div[contains(@class, 'error') or contains(@class, 'alert')]")

    def select_tab(self, tab_name):
        tab_map = {
            "телефон": self.TAB_PHONE,
            "почта": self.TAB_EMAIL,
            "логин": self.TAB_LOGIN,
            "лицевой счет": self.TAB_LS
        }
        self.wait_for_clickable(tab_map[tab_name.lower()]).click()

    def enter_username(self, username):
        self.wait_for_element(self.INPUT_USERNAME).send_keys(username)

    def enter_password(self, password):
        self.wait_for_element(self.INPUT_PASSWORD).send_keys(password)

    def submit(self):
        self.wait_for_clickable(self.BUTTON_SUBMIT).click()

    def get_error_text(self):
        return self.get_text(self.ERROR_MESSAGE)

    def is_forgot_password_orange(self):
        elem = self.wait_for_element(self.FORGOT_PASSWORD_LINK)
        color = elem.value_of_css_property("color")
        # Оранжевый цвет в системе (может быть rgb(255, 79, 18))
        return "255, 79, 18" in color or "orange" in color.lower()

    def go_to_registration(self):
        self.wait_for_clickable(self.REGISTER_LINK).click()

    def go_to_recovery(self):
        self.wait_for_clickable(self.FORGOT_PASSWORD_LINK).click()

    def get_active_tab_text(self):
        active_tab = self.driver.find_element(By.XPATH, "//div[contains(@class, 'rt-tab--active')]")
        return active_tab.text.strip()

    def clear_username(self):
        self.wait_for_element(self.INPUT_USERNAME).clear()