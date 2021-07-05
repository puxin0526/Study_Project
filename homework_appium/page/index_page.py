from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from homework_appium.page.base_page import BasePage
from homework_appium.page.contacts_page import ContactPage


class IndexPage(BasePage):

    def goto_contact(self):
        self.find(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        return ContactPage(self.driver)
