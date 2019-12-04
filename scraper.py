from selenium.webdriver import Chrome
import codecs

# webdriver = "C:/Users/User/Downloads/chromedriver_win32/chromedriver"
webdriver = "path_to_driver"
driver = Chrome(webdriver)

url = "http://www.matf.bg.ac.rs/m/180/osnovne-informatika/"
driver.get(url)

tables = driver.find_elements_by_css_selector("table")
num_tables = len(tables)

i = 0
with codecs.open("subjects.txt", "w", "utf-16") as stream:
    for i in range(num_tables-1):
        stream.write(tables[i].text)