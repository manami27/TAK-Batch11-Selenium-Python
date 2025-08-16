from selenium.webdriver.common.by import By
from Library import get_locator, read_config
import time

class LoginPage:
    def __init__(self, browser):
        self.browser = browser
        
        # Ambil locator dari element.cfg
        self.username_locator = get_locator("Login","username")
        self.password_locator = get_locator("Login","password")
        self.login_btn_locator = get_locator("Login","login_btn")
        self.inventory_url = get_locator("Inventory","inventory_url")
        self.burger_menu_locator = get_locator("Inventory","burger_menu")
        self.logout_btn_locator = get_locator("Inventory","logout_btn")
        self.error_msg_locator = get_locator("Login","error_msg")
    
    # Contoh mengisi step by step 
    def enter_username(self, username):
        username_field = self.browser.find_element(By.ID, self.username_locator)
        username_field.clear()
        username_field.send_keys(username)
        
    def enter_password(self, password):
        pass_field = self.browser.find_element(By.ID, self.password_locator)
        pass_field.clear()
        pass_field.send_keys(password)
    
    def click_login(self):
        self.browser.find_element(By.ID, self.login_btn_locator).click()
    
    # Alternatif lain, boleh buat function satu flow dengan memanggil function sebelumnya
    def login_success(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        
    def is_login_successful(self):
        get_url = self.browser.current_url
        get_inventory_url = self.inventory_url
        
        if get_inventory_url in get_url:
            print("Website logged in successfully")
            return True
        else:
            print("Failed Login")
            return False
        
    def is_login_failed(self, expected_text=None):
        try:
            err = self.browser.find_element(By.CSS_SELECTOR, self.error_msg_locator)
            err_text = err.text.strip() #get text dari locator
            print("Login error text: ", err_text)
            
            if expected_text:
                return expected_text in err_text
            return True
        except Exception as e:
            # element not found
            print("No Login Error element found: ", e)
            return False            
        
    def logout(self):
        self.browser.find_element(By.ID, self.burger_menu_locator).click()
        time.sleep(1)
        self.browser.find_element(By.ID, self.logout_btn_locator).click()
        time.sleep(2) # tunggu proses logout complete
        