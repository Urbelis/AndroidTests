from behave import *
from appium import webdriver
from ..main_view import MainView


@step('upper text bar is: {"text"}')
def upper_bar_found(context, text):
    upper_bar_value = context.driver.upper_text()
    assert text in upper_bar_value


@step('bottom text bar is: {"text"}')
def bottom_text_bar_found(context, text):
    bottom_bar_value = context.driver.lower_text()
    assert text in bottom_bar_value


@step('ADD button should be present')
def add_button_present(context):
    add_button = context.driver.find_element_by_id('com.test.calc:id/add_b')
    assert add_button.is_displayed() is True


@step('SUB button should be present')
def sub_button_present(context):
    sub_button = context.driver.find_element_by_id('com.test.calc:id/sub_b')
    assert sub_button.is_displayed() is True


@step('user clicks ADD button')
def add_button_click(context):
    context.driver.click_add_button()


@step('user clicks SUB button')
def sub_button_click(context):
    context.driver.click_sub_button()


@step('user clicks ADD button twice')
def add_btn_click_twice(context):
    context.driver.click_add_button()
    context.driver.click_add_button()


@step('user clicks SUB button twice')
def add_btn_click_twice(context):
    context.driver.click_sub_button()
    context.driver.click_sub_button()
