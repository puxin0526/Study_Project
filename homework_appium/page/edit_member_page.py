from appium.webdriver.common.mobileby import MobileBy

from homework_appium.page.base_page import BasePage


class EditMemberPage(BasePage):

    def delete_member(self):
        self.swipe_find('删除成员').click()
        self.find(MobileBy.XPATH, '//*[@text="确定"]').click()

        from homework_appium.page.manage_contact_page import ManageContactPage

        return ManageContactPage(self.driver)
