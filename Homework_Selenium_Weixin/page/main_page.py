from selenium.webdriver.common.by import By
from Homework_Selenium_Weixin.page.base_page import BasePage
from Homework_Selenium_Weixin.page.contact_page import ContactPage


class MainPage(BasePage):
    # 查找跳转到通讯录元素
    __goto_contact_ele = (By.XPATH, '//*[@id="menu_contacts"]/span')

    def goto_import_contact(self):
        pass

    def goto_add_member(self):
        pass

    def goto_contact(self):
        # 点击跳转到通讯录
        self.find(self.__goto_contact_ele).click()

        return ContactPage(self.driver)
