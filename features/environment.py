import os
from appium import webdriver


def before_feature(context, feature):
    app = os.path.join(os.path.dirname(__file__),
                       '../app/Calculator.apk')
    app = os.path.abspath(app)
    context.driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723/wd/hub',
        desired_capabilities={
            'app': app,
            'platformName': 'Android',
            'platformVersion': '4.4',
            'deviceName': 'AndroidEmu'
        }
    )


def after_feature(context, feature):
    context.driver.quit()
