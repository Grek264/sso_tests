import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="function")
def driver(request):
    """Инициализация драйвера Chrome."""
    chrome_options = Options()
    if request.config.getoption("--headless"):
        chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", help="Run in headless mode")
    parser.addoption("--base-url", action="store", default="https://b2c.passport.rt.ru/", help="Base URL")