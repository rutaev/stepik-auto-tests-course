from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)

    shield = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", shield)
    shield.send_keys(y)

    checkbox = browser.find_element_by_id("robotCheckbox").click()
    radio = browser.find_element_by_id("robotsRule").click()
    btn = browser.find_element_by_css_selector("button").click()

finally:
    time.sleep(15)
    browser.quit()
    

    
    
  
