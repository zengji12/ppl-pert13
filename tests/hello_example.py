import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class GoogleTestCase(unittest.TestCase):
    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        server = 'http://localhost:4444'

        self.browser = webdriver.Remote(command_executor=server, options=options)
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('https://www.example.com')
        element = self.browser.find_element(By.TAG_NAME, 'p')
        print(element.text) 

if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')
