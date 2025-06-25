import os
import shutil

import pytest
from selenium import webdriver

import config


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_experimental_option("prefs", {
        "download.default_directory": os.path.abspath(config.DOWNLOADS_DIR),  # Делаем папку для загрузок рядом с тестами
        "download.prompt_for_download": False,
        "directory_upgrade": True,
        "safebrowsing.enabled": True  # Отключаем проверку перед скачиванием
    })
    shutil.rmtree(config.DOWNLOADS_DIR, True)  # Очистка загрузок
    os.mkdir(config.DOWNLOADS_DIR)

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(3)
    try:
        yield driver
    finally:
        driver.quit()
