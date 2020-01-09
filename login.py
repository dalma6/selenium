from selenium.webdriver import Chrome

webdriver = "C:/Users/User/Downloads/chromedriver_win32/chromedriver"
driver = Chrome(webdriver)

url = "http://facebook.com/login"
driver.get(url)

email = driver.find_element_by_id("email")
email.send_keys("test.selenium.matf@gmail.com")

password = driver.find_element_by_id("pass")
password.send_keys("testpwd")

login_btn = driver.find_element_by_id("loginbutton")
login_btn.click()