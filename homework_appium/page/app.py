from appium import webdriver

from homework_appium.page.base_page import BasePage
from homework_appium.page.index_page import IndexPage


class App(BasePage):

    def start(self):
        if self.driver == None:
            caps = {
                "platformName": "Android",
                "deviceName": "127.0.0.1:7555",
                "appPackage": "com.tencent.wework",
                # Mac/Linux: adb logcat |grep -i activitymanager
                # Windows: adb logcat |findstr /i activitymanager
                "appActivity": ".launch.WwMainActivity",
                "noReset": "true"
            }
            # 与server建立连接
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
            self.driver.implicitly_wait(5)
        else:
            self.restart()

        return self

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        self.driver.quit()

    def goto_main(self):
        # 页面的入口方法
        return IndexPage(self.driver)
