from Homework_Selenium_Weixin.page import contact_page
from Homework_Selenium_Weixin.page.base_page import BasePage
from selenium.webdriver.common.by import By


class AddDepartmentPage(BasePage):
    # 部门名称元素定位
    __department_name_ele = (By.NAME, "name")
    # 所属部门下拉选项元素定位
    __department_menu_ele = (By.CSS_SELECTOR, ".js_parent_party_name")
    # 选择所属部门元素定位
    __department_select_ele = (By.CSS_SELECTOR, ".qui_dialog_body.ww_dialog_body [id='1688851307804993_anchor']")
    # 确定按钮元素定位
    __confirm_ele = (By.LINK_TEXT, "确定")

    def add_department(self, department_name):
        # 输入部门名称
        self.find(self.__department_name_ele).send_keys(department_name)
        # 点击获取所属部门列表
        self.find(self.__department_menu_ele).click()
        # 点击选择所属部门
        self.find(self.__department_select_ele).click()
        # 点击确定按钮
        self.find(self.__confirm_ele).click()

        return contact_page.ContactPage(self.driver)
