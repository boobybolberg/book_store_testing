#Shop: отображение страницы товара
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
Shop = driver.find_element_by_id('menu-item-40').click()
HTML5Forms = driver.find_element_by_css_selector('.products > li:nth-child(3)').click()
HTML5_title = driver.find_element_by_css_selector('h1.product_title')
HTML5_title_text = HTML5_title.text
assert HTML5_title_text == "HTML5 Forms"
driver.quit()

#Shop: количество товаров в категории
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
Shop = driver.find_element_by_id('menu-item-40').click()
HTML = driver.find_element_by_css_selector('.product-categories > li:nth-child(2)').click()
items = driver.find_elements_by_css_selector('#content .products')
if len(items) == 3:
    print("На странице отображается 3 товара")
else:
    print("Ошибка. Количество товаров на странице: " + str(len(items)))
driver.quit()

#Shop: сортировка товаров
from selenium.webdriver.support.select import Select
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
Shop = driver.find_element_by_id('menu-item-40').click()
selector_default = driver.find_element_by_css_selector('[name="orderby"] > option:nth-child(1)')
default_selected = selector_default.get_attribute("selected")
print("value of default selector: ", default_selected)
if default_selected is not None:
    print("Стоит сортировка по умолчанию")
else:
    print("Ошибка:филтьр не отмечен")
Sort_price = driver.find_element_by_css_selector('select.orderby')
select = Select(Sort_price)
select.select_by_value("price-desc")
price_desc = driver.find_element_by_css_selector('[name="orderby"] > option:nth-child(6)')
price_desc_selected = price_desc.get_attribute("selected")
print("value of default selector: ", price_desc_selected)
if price_desc_selected is not None:
    print("Стоит сортировка по убыванию цены")
else:
    print("Ошибка:филтьр не отмечен")
driver.quit()

#Shop: отображение, скидка товара
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
Shop = driver.find_element_by_id('menu-item-40').click()
AndroidBook = driver.find_element_by_css_selector('.products > li:nth-child(1)').click()
OldPrice = driver.find_element_by_css_selector('.price > del > span')
OldPrice_text = OldPrice.text
assert OldPrice_text == "₹600.00"
NewPrice = driver.find_element_by_css_selector('.price > ins > span')
NewPrice_text = NewPrice.text
assert NewPrice_text == "₹450.00"
PicOpen = driver.find_element_by_class_name('images').click()
PicOpen_wait = WebDriverWait(driver, 10).until(
    ec.presence_of_element_located((By.ID, 'fullResImage')))
Quit = driver.find_element_by_class_name('pp_close').click()
Quit_wait = WebDriverWait(driver,10).until(
    ec.invisibility_of_element((By.ID, 'fullResImage')))
driver.quit()

#Shop: проверка цены в корзине
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://practice.automationtesting.in/')
Shop = driver.find_element_by_id('menu-item-40').click()
Add_to_bucket = driver.find_element_by_css_selector('.products > li:nth-child(4) > .button').click()
CartAmount = driver.find_element_by_class_name('cartcontents')
CartAmount_text = CartAmount.text
assert CartAmount_text == "1 Item"
CartPrice = driver.find_element_by_css_selector('#wpmenucartli .amount')
CartPrice_text = CartPrice.text
assert CartPrice_text == "₹180.00"
Cart = driver.find_element_by_id('wpmenucartli').click()
Subtotal = WebDriverWait(driver,10).until(
    ec.text_to_be_present_in_element((By.CSS_SELECTOR, '.cart-subtotal .amount'),'180.00'))
Total = WebDriverWait(driver,10).until(
    ec.text_to_be_present_in_element((By.CSS_SELECTOR, '.order-total .amount'),'183.60'))
driver.quit()

#Shop: работа в корзине
import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)

driver.get('https://practice.automationtesting.in/')
Shop = driver.find_element_by_id('menu-item-40').click()
driver.execute_script("window.scrollBy(0, 300);")
Add_to_bucket1 = driver.find_element_by_css_selector('.products > li:nth-child(4) > .button').click()
time.sleep(3)
Add_to_bucket2 = driver.find_element_by_css_selector('.products > li:nth-child(5) > .button').click()
time.sleep(3)
Cart = driver.find_element_by_class_name('cartcontents').click()
time.sleep(3)
DeleteBook1 = driver.find_element_by_css_selector(
    'div > div.woocommerce > form > table > tbody > tr:nth-child(1) > td.product-remove > a').click()
time.sleep(3)
Undo = driver.find_element_by_xpath('//*[@id="page-34"]/div/div[1]/div[1]/a').click()
time.sleep(3)
Quantity = driver.find_element_by_css_selector('tbody > tr:nth-child(2) > td.product-quantity > div > input')
Quantity.clear()
Quantity.send_keys('3')
time.sleep(3)
Update = driver.find_element_by_css_selector('[name="update_cart"]').click()
time.sleep(3)
Quantity_value = Quantity.get_attribute('value')
assert Quantity_value == '3'
time.sleep(3)
apply_coupon_button = driver.find_element_by_name("apply_coupon")
apply_coupon_button.click()
ApplyError = driver.find_element_by_css_selector('.woocommerce-error > li')
ApplyError_text = ApplyError.text
assert ApplyError_text == 'Please enter a coupon code.'
driver.quit()

#Shop: покупка товара
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://practice.automationtesting.in/")
shop_tab = driver.find_element(By.LINK_TEXT, "Shop")
shop_tab.click()
driver.execute_script("window.scrollBy(0, 300)")
book = driver.find_element_by_css_selector('.products > li:nth-child(4) > .button').click()
time.sleep(3)
cart = driver.find_element_by_class_name('wpmenucart-contents').click()
wait = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'checkout-button')))
wait.click()
url = WebDriverWait(driver,10).until(
    EC.url_to_be, "https://practice.automationtesting.in/checkout/")
first_name_input = driver.find_element_by_name("billing_first_name")
first_name_input.send_keys("John")
last_name_input = driver.find_element_by_id('billing_last_name')
last_name_input.send_keys("Malcovic")
email_input = driver.find_element_by_id("billing_email")
email_input.send_keys("John123@gmail.com")
phone_input = driver.find_element_by_id("billing_phone")
phone_input.send_keys("89512997546")
time.sleep(5)
country_select = driver.find_element_by_id('s2id_billing_country').click()
time.sleep(3)
country_search = driver.find_element_by_id('s2id_autogen1_search')
country_search.send_keys("Russia")
country_confirm = driver.find_element_by_id("select2-results-1").click()
billing_address = driver.find_element_by_id('billing_address_1')
billing_address.send_keys("Krasnaya Ploshad")
City = driver.find_element_by_css_selector("#billing_city.input-text ")
City.send_keys("Spb")
State = driver.find_element_by_css_selector("#billing_state.input-text")
State.send_keys("Russia")
PostalCode = driver.find_element_by_css_selector("#billing_postcode.input-text")
PostalCode.send_keys("195277")
driver.execute_script("window.scrollBy(0, 600)")
time.sleep(3)
check_payments = driver.find_element_by_id('payment_method_cheque').click()
place_order = driver.find_element_by_id('place_order').click()
ThankYou_message = WebDriverWait(driver,10).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "woocommerce-thankyou-order-received"), 'Thank you. Your order has been received.'))
CheckPayments_message = WebDriverWait(driver,10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tr:nth-child(3) > td"),"Check Payments"))
driver.quit()