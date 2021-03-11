import time
import math
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    btn = browser.find_element_by_css_selector("button").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    x_element = browser.find_element_by_id("input_value").text
    y = calc(x_element)
    shield = browser.find_element_by_tag_name("input").send_keys(y)
    btn = browser.find_element_by_tag_name('button').click()

finally:
    time.sleep(10)
    browser.quit()
