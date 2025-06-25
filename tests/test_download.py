import os
from selenium.webdriver.remote.webdriver import WebDriver

import config
from pages.main_page import MainPage
from pages.downloads_page import DownloadsPage
from utils import wait_for_download_complete, get_file_size_mb


def test_file_downloading(driver: WebDriver):
    # Открываем главную и переходим на страницу загрузки файлов
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_downloads()

    downloads_page = DownloadsPage(driver)

    # Получаем ожидаемый размер файла из текста на сайте
    expected_size_mb = downloads_page.get_file_size("Веб-установщик")

    # Кликаем по кнопке скачивания
    downloads_page.click_download_file("Веб-установщик")

    # Ждём завершения скачивания файла
    download_path = wait_for_download_complete(
        os.path.abspath(config.DOWNLOADS_DIR),
        config.EXPECTED_FILENAME
    )

    # Получаем фактический размер файла
    actual_size_mb = get_file_size_mb(download_path)

    # Сравниваем с ожидаемым
    assert abs(actual_size_mb - expected_size_mb) < 0.1, (
        f"Размер не совпадает! Ожидалось: {expected_size_mb} МБ, было: {actual_size_mb:.2f} МБ"
    )