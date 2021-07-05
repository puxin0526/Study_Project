from homework_appium.page.app import App


class TestContact:

    # def setup_class(self):
    #     self.app = App()

    def setup_class(self):
        self.app = App()

    def setup(self):
        self.main = self.app.start().goto_main()

    def teardown_class(self):
        self.app.stop()

    def test_add_member(self):
        username = '爪巴'
        phonenum = '13011000001'
        self.main.goto_contact().goto_add_member().addmember_manual(). \
            edit_addmember(username, phonenum).verify(username)

    def test_delete_member(self):
        self.main.goto_contact().goto_manage_member().goto_edit_member('爪巴') \
            .delete_member().back_contact().verify_delete_ok('爪巴')
