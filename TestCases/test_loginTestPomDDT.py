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


    #Contoh cara memanggil function dari class login page dan data loginnya diambil dari static array usernames
    def test_success_login_page_element_ddt(self):
        for username in self.usernames:
            with self.subTest(username=username):
                self.login_page.enter_username(username) # kirim username dari Array
                self.login_page.enter_password(self.passwords)
                self.login_page.click_login()
                self.assertTrue(self.login_page.is_login_successful())
                self.login_page.logout()            
  
                    
    @classmethod    
    def tearDownClass(cls):
        InitiateDriver.closeBrowser()

if __name__ == '__main__':
    unittest.main(verbosity=2)