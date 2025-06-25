import re

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class DownloadsPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click_download_file(self, file: str):
        download_link = self.get_download_file_link(file)
        download_link.click()

    def get_file_size(self, file: str) -> float:
        download_link = self.get_download_file_link(file)
        text = download_link.text
        match = re.search(r"(\d+(\.\d+)?)\s*МБ", text)
        if match:
            return float(match.group(1))

    def get_download_file_link(self, file):
        return self.driver.find_element(
            By.XPATH,
            f'//div[contains(@class, "sbis_ru-DownloadNew-block")]'
            f'//h3[contains(text(), {file})]'
            f'/../..//a[contains(@href, ".exe")]'
        )