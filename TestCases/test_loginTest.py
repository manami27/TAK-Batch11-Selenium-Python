import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from Base import InitiateDriver
from Pages import LoginPage
from Library import read_config

class LoginSaucedemo(unittest.TestCase):
    
    #@classmethod
    def setUp(self):
        self.browser = InitiateDriver.startBrowser() # ini cara memanggil class dan method 
        self.login_page = LoginPage(self.browser)
        
        # Retrieve credential from config file
        self.usernameData = read_config("Credential", "username")
        self.passwordData = read_config("Credential", "password")
        
        print(self.usernameData)   
        print(self.passwordData)        

    # Assertion Page Login/Main Page
    def test_01_success_page_title(self):
        self.assertEqual(self.browser.title, "Swag Labs")
        #print('Assert Success')
    
    def test_02a_success_login_hardcore(self):
        browser = self.browser
        browser.find_element(By.ID, "user-name").send_keys('standard_user')
        browser.find_element(By.CSS_SELECTOR,'[data-test="password"]').send_keys('secret_sauce')
        browser.find_element(By.ID, "login-button").click()
        
        # Verifikasi login berhasil dengan URL assertion
        get_url = browser.current_url
        self.assertIn('/inventory.html', get_url)       

        #print("Website logged in successfully")
    
    #Contoh cara memanggil function daro class login page    
    def test_02b_success_login_page_element(self):
        self.login_page.enter_username(self.usernameData)
        self.login_page.enter_password(self.passwordData)
        self.login_page.click_login()
        
        self.assertTrue(self.login_page.is_login_successful())
       
    def test_03_failed_login_wrong_user_or_password(self):
        browser = self.browser
        # Fitur Login
        # Isi username dan password
        browser.find_element(By.ID, "user-name").send_keys('standard_user')
        browser.find_element(By.CSS_SELECTOR,'[data-test="password"]').send_keys('wrong_password')

        # Klik tombol login
        browser.find_element(By.ID, "login-button").click()

        # Verifikasi login failed dengan URL assertion
        error_message = browser.find_element(By.CSS_SELECTOR,'[data-test="error"]').text
        self.assertIn('Username and password do not match', error_message)

        #print("Website logged in failed - wrong username or password")

    def test_04_failed_login_locked_out_user(self):
        browser = self.browser
        # Fitur Login
        # Isi username dan password
        browser.find_element(By.ID, "user-name").send_keys('locked_out_user')
        browser.find_element(By.CSS_SELECTOR,'[data-test="password"]').send_keys('secret_sauce')

        # Klik tombol login
        browser.find_element(By.ID, "login-button").click()

        # Verifikasi login failed dengan URL assertion
        error_message = browser.find_element(By.CSS_SELECTOR,'[data-test="error"]').text
        self.assertIn('Sorry, this user has been locked out', error_message)

        #print("Website logged in failed - locked out user")
        
    #@classmethod
    def tearDown(self):
        InitiateDriver.closeBrowser()

if __name__ == '__main__':
    unittest.main(verbosity=2)