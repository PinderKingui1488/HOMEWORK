def mask_card_number(card_number: str) -> str:
    """
    Функция маскирует номер кредитной карты, заменяя все, кроме первых 4 и последних 4 цифр, символами 'X'.
    """
    if len(card_number) != 16:
        return "Неверный формат номера карты"
    masked_number = card_number[:4] + " " + "**" + " " + "****" + " " + card_number[12:]
    return masked_number


def mask_account_number(account_number: str) -> str:
    """
    Функция маскирует номер счета, заменяя все, кроме последних 6 цифр, символами 'X'.
    """
    if len(account_number) < 6:
        return "Номер счета слишком короткий"
    masked_number = "**" + account_number[-6:]
    return masked_number