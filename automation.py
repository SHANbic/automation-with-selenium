from selenium import webdriver
import time

chrome_browser = webdriver.Chrome('./chromedriver')
chrome_browser.get('http://shanbic.pythonanywhere.com/contact.html')
time.sleep(1)

email = chrome_browser.find_element_by_id('email')
subject = chrome_browser.find_element_by_id('subject')
textarea = chrome_browser.find_element_by_tag_name('textarea')
submit = chrome_browser.find_elements_by_class_name('btn')[0]
print(submit)


email.clear()
email.send_keys('selenium@test.com')

subject.clear()
subject.send_keys('sent from selenium')

textarea.clear()
textarea.send_keys('hello, i was went from a selenium script ;)')

time.sleep(1)

submit.click()