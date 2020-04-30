# import pytest
# import time
# from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_add_to_basket_button(browser):

        browser.get(link)
        # time.sleep(30)
        button = len(browser.find_elements_by_css_selector("#add_to_basket_form>.btn-lg"))
        assert button>0, "'Add to busket button' is absent on the page"
