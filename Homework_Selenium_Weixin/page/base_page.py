from selenium import webdriver


class BasePage:

    def __init__(self, base_driver=None):
        """
        :param base_driver: 传入driver实例对象

        """
        # 如果 base_driver 是初始值None，那么就会实例化driver
        if base_driver is not None:
            self.driver = base_driver
            self.driver.implicitly_wait(5)
        else:
            # 使用浏览器复用模式
            chrome_arg = webdriver.ChromeOptions()
            # 加入调试地址
            chrome_arg.debugger_address = '127.0.0.1:9222'
            # 实例化driver对象
            self.driver = webdriver.Chrome(options=chrome_arg)
            self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
            self.driver.implicitly_wait(5)

    def find(self, locator):
        # 解元组的操作
        return self.driver.find_element(*locator)
