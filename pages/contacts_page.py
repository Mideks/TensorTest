import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class ContactsPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click_tensor_banner(self):
        banner = self.driver.find_element(By.CSS_SELECTOR, "div.sbis_ru-container a.sbisru-Contacts__logo-tensor")
        banner.click()

    def get_region_text(self) -> str:
        return self.get_region_chooser().text

    def get_region_chooser(self):
        return self.driver.find_element(By.CSS_SELECTOR, "span.sbis_ru-Region-Chooser__text")

    def get_partners(self):
        partners = self.driver.find_elements(
            By.CSS_SELECTOR,
            '.sbisru-Contacts-List__col [data-qa="items-container"] [data-qa="item"]'
        )
        return partners

    def change_region(self, target_region):
        region_chooser = self.get_region_chooser()
        region_chooser.click()

        time.sleep(1)
        region = self.driver.find_element(
            By.XPATH,
            f"//ul[contains(@class, 'sbis_ru-Region-Panel__list-l')]//li[contains(., '{target_region}')]"
        )
        time.sleep(1)
        region.click()
