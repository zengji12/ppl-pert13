import unittest, sys
from selenium import webdriver
from selenium.webdriver.common.by import By

class BaseTestCase(unittest.TestCase):
    browser_name = 'firefox'

    def setUp(self):
        server = 'http://localhost:4444'
        if self.browser_name.lower() == 'firefox':
            options = webdriver.FirefoxOptions()
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--ignore-ssl-errors')
            self.browser = webdriver.Remote(command_executor=server, options=options)
        elif self.browser_name.lower() == 'chrome':
            options = webdriver.ChromeOptions()
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--ignore-ssl-errors')
            self.browser = webdriver.Remote(command_executor=server, options=options)
        elif self.browser_name.lower() == 'edge':
            options = webdriver.EdgeOptions()
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--ignore-ssl-errors')
            self.browser = webdriver.Remote(command_executor=server, options=options)
        else:
            raise Exception(f"Unsupported browser: {self.browser_name}")

        self.addCleanup(self.browser.quit)

    def test_Homepage(self):
        if len(sys.argv) > 1:
            url = sys.argv[1]
        else:
            url = "http://localhost"
        
        self.browser.get(url)
        self.browser.save_screenshot(f'screenshot_{self.browser_name}.png')
        expected_result = "Welcome back, Guest!"
        actual_result = self.browser.find_element(By.TAG_NAME, 'p')
        self.assertIn(expected_result, actual_result.text)

class FirefoxTest(BaseTestCase):
    browser_name = 'firefox'

class ChromeTest(BaseTestCase):
    browser_name = 'chrome'

class EdgeTest(BaseTestCase):
    browser_name = 'edge'

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], verbosity=2, warnings='ignore')
