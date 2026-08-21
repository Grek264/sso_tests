import os


class TestData:
    """Test data loaded from environment variables."""

    VALID_PHONE = os.getenv("RT_VALID_PHONE", "")
    VALID_EMAIL = os.getenv("RT_VALID_EMAIL", "")
    VALID_LOGIN = os.getenv("RT_VALID_LOGIN", "")
    VALID_LS = os.getenv("RT_VALID_LS", "")
    VALID_PASSWORD = os.getenv("RT_VALID_PASSWORD", "")
    WRONG_PASSWORD = os.getenv("RT_WRONG_PASSWORD", "incorrect-password")

    FIRST_NAME = os.getenv("RT_FIRST_NAME", "Тест")
    LAST_NAME = os.getenv("RT_LAST_NAME", "Пользователь")
    REGION = os.getenv("RT_REGION", "Москва")
    NEW_EMAIL = os.getenv("RT_NEW_EMAIL", "")
    NEW_PASSWORD = os.getenv("RT_NEW_PASSWORD", "")

    RECOVERY_PHONE = VALID_PHONE
    RECOVERY_EMAIL = VALID_EMAIL
