from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from homework_appium.page.base_page import BasePage
from homework_appium.page.edit_member_page import EditMemberPage


class ManageContactPage(BasePage):

    def goto_edit_member(self, username):
        WebDriverWait(self.driver, 10).until \
            (lambda x: x.find_element(MobileBy.XPATH, f'//*[@text="{username}"]'))

        self.find(MobileBy.XPATH, f'//*[@text="{username}"]').click()

        return EditMemberPage(self.driver)

    def back_contact(self):
        self.find(MobileBy.ID, 'com.tencent.wework:id/h8g').click()
        from homework_appium.page.contacts_page import ContactPage
        return ContactPage(self.driver)
