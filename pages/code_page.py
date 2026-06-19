from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CodePage(BasePage):
    MASKED_CONTACT = (By.XPATH, "//span[contains(@class, 'masked') or contains(@class, 'contact')]")
    RESEND_BUTTON = (By.XPATH, "//button[contains(text(), 'Получить код повторно')]")
    CODE_FIELDS = [(By.ID, f"code_{i}") for i in range(6)]

    def get_masked_contact(self):
        return self.get_text(self.MASKED_CONTACT)

    def is_resend_button_visible(self):
        return self.is_element_visible(self.RESEND_BUTTON)

    def enter_code(self, code):
        for i, digit in enumerate(str(code)):
            field = self.wait_for_element(self.CODE_FIELDS[i])
            field.send_keys(digit)