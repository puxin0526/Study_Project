# from homework_appium.page.add_member_edit_page import AddMemberEditPage
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from homework_appium.page.base_page import BasePage


class AddMemberPage(BasePage):

    def addmember_manual(self):
        from homework_appium.page.add_member_edit_page import AddMemberEditPage
        self.find(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        return AddMemberEditPage(self.driver)

    def verify(self, username):
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, '//*[@text="添加成功"]'))
        real_res = self.find(MobileBy.XPATH, '//*[@text="添加成功"]').text
        expect_res = '添加成功'
        expect_name = username
        self.find(MobileBy.ID, 'com.tencent.wework:id/h86').click()
        ele_list = self.driver.find_elements(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/he1"]/*')

        actual_name = [i.text for i in ele_list]
        print(actual_name)

        assert expect_name in actual_name
        assert real_res == expect_res
