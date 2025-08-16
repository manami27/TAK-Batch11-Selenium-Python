import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from Base import InitiateDriver
from Pages import LoginPage
import time

class LoginSaucedemo(unittest.TestCase):
    
    
    usernames = ["standard_user", "problem_user", "error_user"] #static array
    passwords = "secret_sauce"
    
    @classmethod
    def setUpClass(cls):
        cls.browser = InitiateDriver.startBrowser() # ini cara memanggil class dan method 
        cls.login_page = LoginPage(cls.browser)

    def test_login_test(self):
        login_data = [
            ("","", "Username is required"),
            ("standard_user","", "Password is required"),
            ("wrong_user","wrong_password","Username and password do not match any user in this service"),
            ("standard_user", "secret_sauce", None)
        ]
        
        for username, password, expected_msg in login_data:
            with self.subTest(username=username, password=password):
                self.browser.refresh()
                time.sleep(1)
                  
                self.login_page.enter_username(username) # kirim username dari Array
                self.login_page.enter_password(password)
                self.login_page.click_login()
                
                if expected_msg:
                    self.assertFalse(self.login_page.is_login_successful(), msg="Login Success")
                    self.assertTrue(self.login_page.is_login_failed(expected_msg), msg=f"Expected Error '{expected_msg}' not found")
                else:
                    self.assertTrue(self.login_page.is_login_successful(), msg="Expected Login Success")
                    self.login_page.logout()
                    time.sleep(1)  
                
    @classmethod    
    def tearDownClass(cls):
        InitiateDriver.closeBrowser()

if __name__ == '__main__':
    unittest.main(verbosity=2)