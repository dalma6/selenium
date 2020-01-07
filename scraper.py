from selenium.webdriver import Chrome

webdriver = "C:/Users/User/Downloads/chromedriver_win32/chromedriver"
driver = Chrome(webdriver)

url = "http://www.matf.bg.ac.rs/m/180/osnovne-informatika/"
driver.get(url)

tables = driver.find_elements_by_css_selector("table")[:4]
subject_data = []

for table in tables:
    table_rows = table.find_elements_by_css_selector("tr")
    for row in table_rows:
        row_text = row.text
        if any(['????????' in row_text,
                '???????' in row_text,
                '??????' in row_text
                ]):
            continue
        else:
            subject_data.append(row_text)

assert len(subject_data) == 41, "Unexpected number of subjects!"