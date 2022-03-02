import time

from selenium.webdriver.common.by import By

link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_buton_basket_on_page(browser):
    browser.get(link)
    #time.sleep(30)
    button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    assert button, "basket button not find!"


