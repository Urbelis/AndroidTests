from appium import webdriver

class MainView(object):

    def __init__(self, context):
        self.context = context
        self.driver = self.context.driver

    def upper_text(self):
        upper_text_view = self.context.find_element_by_id(
            'com.test.calc:id/tv1')
        return upper_text_view.text()

    def bottom_text(self):
        upper_text_view = self.context.find_element_by_id(
            'com.test.calc:id/tv2')
        return upper_text_view.text()

    def click_add_button(self):
        self.context.find_element_by_id('com.test.calc:id/add_b').click()

    def click_sub_button(self):
        return self.context.find_element_by_id('com.test.calc:id/sub_b').click()
