"""
:authors: @litemat
:license: The MIT License (MIT), see LICENSE file
:copyright: (c) 2025 @litemat
"""

from altel_api import AltelB2B

client = AltelB2B(username="747XXXXXXX", password="********")

test_number: str = ""
test_uin: str = ""

if client.login():
    subs = client.all_subscribers(limit=40)  # Вывод списка первых до 40.
    print(subs)

    subs = client.all_subscribers(limit=50)  # Вывод списка первых до 50.
    print(subs)

    subs = client.search_subscriber(test_number)  # Поиск абонента по номеру.
    print(subs)

    result = client.block(test_number)  # Блокировка абонента по номеру.
    print(result)

    result = client.unblock(test_number)  # Разблокировка абонента по номеру.
    print(result)

    result = client.get_details(test_number)  # Получение обширных деталей абонента по номеру.
    print(result)

    result = client.register_imei(test_number, test_uin)  # Регистрация IMEI абонента по IMEI и ИИН/БИН.
    print(result)

    result = client.change_status(test_number, status_code=1)  # 1 - активен, 2 - заблокирован.
    print(result)

    result = client.company_info()  # Получение информации по вашей компании.
    print(result)

    result = client.admins()  # Получение информации об админах (пользователей вашей компании).
    print(result)

    result = client.profiles()  # Получение информации о зарегистрированных лицевых счетов вашей компании.
    print(result)
else:
    raise Exception("Not authenticate")
