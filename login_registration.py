#Registration_login: регистрация аккаунта
from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://practice.automationtesting.in/')
MyAccount = driver.find_element_by_id('menu-item-50').click()
Register_Email = driver.find_element_by_id('reg_email')
Register_Email.send_keys('Daniil.barkovskii@yandex.ru')
Register_Password = driver.find_element_by_id('reg_password')
Register_Password.send_keys('1337228Putin!')
Register_btn = driver.find_element_by_css_selector("[name='register']").click()
driver.quit()

#Registration_login: логин в систему
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://practice.automationtesting.in/')
MyAccount = driver.find_element_by_id('menu-item-50').click()
Login_Email = driver.find_element_by_id('username')
Login_Email.send_keys('Daniil.barkovskii@yandex.ru')
Login_Password = driver.find_element_by_id('password')
Login_Password.send_keys('1337228Putin!')
Login_btn = driver.find_element_by_css_selector("[name='login']").click()
Logout = WebDriverWait(driver, 10).until(
    ec.presence_of_element_located((By.CSS_SELECTOR, '#content nav li:nth-child(6)')))
driver.quit()

