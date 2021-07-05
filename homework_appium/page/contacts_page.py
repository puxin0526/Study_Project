from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from homework_appium.page.add_member_page import AddMemberPage
from homework_appium.page.base_page import BasePage
from homework_appium.page.manage_contact_page import ManageContactPage


class ContactPage(BasePage):

    def goto_add_member(self):
        self.swipe_find('添加成员').click()
        return AddMemberPage(self.driver)

    def goto_manage_member(self):
        self.find(MobileBy.ID, 'com.tencent.wework:id/h8l').click()

        return ManageContactPage(self.driver)

    def verify_delete_ok(self, username):
        expect_name = username
        ele_list = WebDriverWait(self.driver, 10).until \
            (lambda x: x.find_elements(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/he1"]/*'))

        actual_name = [i.text for i in ele_list]
        print(actual_name)

        assert expect_name not in actual_name
