import time

from selenium.webdriver.remote.webdriver import WebDriver

from pages.main_page import MainPage
from pages.contacts_page import ContactsPage
from pages.tensor_page import TensorPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_tensor_banner_navigation_and_image_check(driver: WebDriver):
    wait = WebDriverWait(driver, 5)

    # Открываем главную
    main = MainPage(driver)
    main.open()
    main.click_contacts()
    main.click_more_contacts()

    # На странице контактов
    contacts = ContactsPage(driver)
    time.sleep(2)  # я не знаю как иначе пофиксить StaleElementReferenceException, который иногда возникает :(
    contacts.click_tensor_banner()

    # Переход в новую вкладку
    current = driver.current_window_handle
    wait.until(lambda d: len(d.window_handles) > 1)
    new_window = [w for w in driver.window_handles if w != current][0]
    driver.switch_to.window(new_window)

    # На tensor.ru
    tensor = TensorPage(driver)
    assert tensor.has_people_block(), "Блок 'Сила в людях' не найден"

    tensor.click_more_button()

    wait.until(EC.url_to_be("https://tensor.ru/about"))
    assert driver.current_url == "https://tensor.ru/about", f"Не та страница: {driver.current_url}"

    assert tensor.all_work_images_same_size(), "Изображения в блоке 'Работаем' имеют разные размеры"
