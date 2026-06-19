class TestData:
    # Данные для авторизации (замените на ваши тестовые)
    VALID_PHONE = "+79261234567"
    VALID_EMAIL = "test@example.com"
    VALID_LOGIN = "testuser"
    VALID_LS = "1234567890"
    VALID_PASSWORD = "ValidPass123"
    WRONG_PASSWORD = "WrongPass"

    # Данные для регистрации (со скриншота)
    FIRST_NAME = "Грек"
    LAST_NAME = "Тестюзер"
    REGION = "Москва"
    NEW_EMAIL = "grishamakhin@gmail.com"  # замените на уникальный при прогоне
    NEW_PASSWORD = "Test_user1234"

    # Для восстановления (используем те же контакты)
    RECOVERY_PHONE = VALID_PHONE
    RECOVERY_EMAIL = VALID_EMAIL