from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from homework_appium.page.base_page import BasePage


class AddMemberEditPage(BasePage):

    def edit_addmember(self, username, phonenum):
        from homework_appium.page.add_member_page import AddMemberPage
        self.find(MobileBy.XPATH, '//*[@text="姓名　"]/../*[@text="必填"]').send_keys(username)
        self.find(MobileBy.XPATH, '//*[@text="手机　"]/..//*[@text="必填"]').send_keys(phonenum)
        self.find(MobileBy.XPATH, '//*[@text="保存"]').click()

        return AddMemberPage(self.driver)
