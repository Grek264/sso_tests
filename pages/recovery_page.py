from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RecoveryPage(BasePage):
    TAB_PHONE = (By.ID, "t-btn-tab-phone")
    TAB_EMAIL = (By.ID, "t-btn-tab-mail")
    TAB_LOGIN = (By.ID, "t-btn-tab-login")
    TAB_LS = (By.ID, "t-btn-tab-ls")

    INPUT_USERNAME = (By.ID, "username")
    INPUT_CAPTCHA = (By.ID, "captcha")
    BUTTON_NEXT = (By.ID, "reset")
    BUTTON_BACK = (By.ID, "reset-back")

    CAPTCHA_IMAGE = (By.CLASS_NAME, "rt-captcha__image")
    CAPTCHA_RELOAD = (By.CLASS_NAME, "rt-captcha__reload")

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

    def enter_captcha(self, captcha_text):
        self.wait_for_element(self.INPUT_CAPTCHA).send_keys(captcha_text)

    def click_next(self):
        self.wait_for_clickable(self.BUTTON_NEXT).click()

    def click_back(self):
        self.wait_for_clickable(self.BUTTON_BACK).click()

    def reload_captcha(self):
        self.wait_for_clickable(self.CAPTCHA_RELOAD).click()