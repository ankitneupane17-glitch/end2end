import unittest
import sys
from xmlrunner import XMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class WebAppTests(unittest.TestCase):

    def setUp(self):
        # Setup runs before every test
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        # Ensure we connect to the correct port (Jenkins will swap 8080 with 9091)
        self.target_url = "http://localhost:8080"
        self.driver = webdriver.Chrome(options=chrome_options)

    def tearDown(self):
        # Teardown runs after every test
        self.driver.quit()

    def test_homepage_title(self):
        """Test that the homepage has the correct welcome text"""
        self.driver.get(self.target_url)
        
        # Find element
        heading = self.driver.find_element(By.ID, "welcome-message").text
        print(f"DEBUG: Found heading: {heading}")
        
        # Assertions - this is what generates "Pass/Fail" in the report
        self.assertIn("Welcome to the JDK 21 App", heading, "Heading text did not match!")

if __name__ == '__main__':
    # This generates the 'test-reports' folder with XML files inside
    unittest.main(
        testRunner=XMLTestRunner(output='test-reports'),
        failfast=False,
        buffer=False,
        catchbreak=False
    )