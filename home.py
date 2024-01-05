#Home: добавление комментария
from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://practice.automationtesting.in/')
driver.execute_script("window.scrollBy(0, 600);")
Selenium_Ruby = driver.find_element_by_css_selector('#text-22-sub_row_1-0-2-0-0 .products').click()
Reviews = driver.find_element_by_class_name('reviews_tab').click()
Star = driver.find_element_by_class_name('star-5').click()
Review_text = driver.find_element_by_id('comment')
Review_text.send_keys('Nice book!')
Name = driver.find_element_by_id('author')
Name.send_keys('Daniil')
Email = driver.find_element_by_id('email')
Email.send_keys('Daniil.barkovskii@yandex.ru')
Submit = driver.find_element_by_css_selector('#submit.submit').click()
driver.quit()

