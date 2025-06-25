import time

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.main_page import MainPage
from pages.contacts_page import ContactsPage
from pages.tensor_page import TensorPage


def test_location_changing(driver: WebDriver):
    # Открываем главную и переходим в Контакты
    main = MainPage(driver)
    main.open()
    main.click_contacts()
    main.click_more_contacts()

    time.sleep(2)  # иначе StaleElementReferenceException

    contacts = ContactsPage(driver)
    initial_region = contacts.get_region_text()
    expected_region = "г. Москва"
    assert initial_region == expected_region, f"Ожидался регион '{expected_region}', а получен '{initial_region}'"

    initial_partners = contacts.get_partners()
    assert len(initial_partners) > 0, "Список партнёров в изначальном регионе пуст"

    # Меняем регион
    target_region = "Камчатский край"
    target_region_url = "41-kamchatskij-kraj"
    contacts.change_region(target_region)

    time.sleep(1)  # Задержка чтоб успело обновиться...

    # Проверяем обновление заголовка страницы
    assert target_region in driver.title, f"В заголовке страницы нет '{target_region}'"

    # Проверяем обновление URL
    assert target_region_url in driver.current_url, f"В URL не найдено '{target_region_url}'"

    # Проверяем смену региона в селекторе
    current_region = contacts.get_region_text()
    assert current_region == target_region, f"В селекторе региона отображается '{current_region}', ожидалось '{target_region}'"

    # Проверяем, что список партнёров изменился
    new_partners = contacts.get_partners()
    assert len(new_partners) != len(initial_partners), "Количество партнёров не изменилось после смены региона"
