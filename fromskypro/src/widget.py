def mask_account_number(user_account_number: str) -> str:
    """
    Функция принимает номер счета и возвращает маску счета.
    """
    masked_number = "**** " + user_account_number[-4:]
    return masked_number
