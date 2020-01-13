from selenium.webdriver import Chrome
import unittest

class WindowTest(unittest.TestCase):
    def setUp(self):
        webdriver = "path/to/driver"
        self.driver = Chrome(webdriver)

    def test_windows(self):
        driver = self.driver
        driver.get("http://www.quackit.com/html/codes/html_popup_window_code.cfm")

        window_before = driver.window_handles[0]
        parent_window_title = driver.title

        driver.switch_to.frame(driver.find_element_by_name('result1'))
        driver.find_element_by_link_text('Open a popup window').click()
        window_after = driver.window_handles[1]

        driver.switch_to.window(window_after)
        child_window_title = driver.title

        self.assertNotEqual(parent_window_title, child_window_title)
        driver.switch_to.window(window_before)
        self.assertEqual(parent_window_title, driver.title)

    def close_resources(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
