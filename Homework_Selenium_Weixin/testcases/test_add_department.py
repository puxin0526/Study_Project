import pytest

from Homework_Selenium_Weixin.page.main_page import MainPage


class TestAddDepartment:
    @pytest.mark.parametrize('department_name', [
        ['a行政部1.'],
        ['行为部门']

    ])
    def test_add_department(self, department_name):
        self.main = MainPage()
        res = self.main.goto_contact().goto_add_department().add_department(department_name)\
            .department_list(department_name)

        assert res in department_name
