import math
import time
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_btn = browser.find_element_by_css_selector(".container button").click()
    alert = browser.switch_to.alert
    alert.accept()
    
    x_element = browser.find_element_by_id("input_value").text
    y = calc(x_element)
    shield = browser.find_element_by_tag_name("input").send_keys(y)
    browser.find_element_by_tag_name('button').click()

finally:
    time.sleep(10)
    browser.quit()
    
