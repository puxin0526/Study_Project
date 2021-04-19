from selenium.webdriver.common.by import By

from Homework_Selenium_Weixin.page.add_department_page import AddDepartmentPage
from Homework_Selenium_Weixin.page.base_page import BasePage


class ContactPage(BasePage):
    __add_icon_ele = (By.CSS_SELECTOR, ".member_colLeft_top_addBtnWrap.js_create_dropdown")
    __goto_add_department_ele = (By.LINK_TEXT, "添加部门")
    # 添加的部门名称

    def goto_add_department(self):
        # 点击+号图标
        self.find(self.__add_icon_ele).click()
        # 点击添加部门
        self.find(self.__goto_add_department_ele).click()

        return AddDepartmentPage(self.driver)

    def goto_add_member(self):
        pass

    def department_list(self, department_name):
        # 方法一：通过列表中的部门名称存在进行断言
        # self.driver.find_elements((By.CSS_SELECTOR, ".jstree-icon.jstree-ocl")).click()
        # ele_list = self.driver.find_elements(By.CSS_SELECTOR, '.jstree-children .jstree-node '
        #                                                       '.jstree-anchor')
        # name_list = [i.text for i in ele_list]
        # print(name_list)
        # return name_list

        # 方法二： 搜索框搜索部门名称进行断言
        # 搜索添加的部门名称
        self.driver.find_element(By.ID, 'memberSearchInput').send_keys(department_name)
        # 搜索结果展示
        res = self.driver.find_element(By.XPATH, '//*[@id="search_party_list"]/li/a').text
        return res
