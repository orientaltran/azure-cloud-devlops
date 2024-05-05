from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions

import unittest

class SwayLabs(unittest.TestCase):
    @classmethod
    def setUp(inst):
        print ('Starting the browser...')
        # --uncomment when running in Azure DevOps.
        options = ChromeOptions()
        options.add_argument("--headless")
        options.add_argument('--remote-debugging-port=9222')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        



        # inst.driver = webdriver.Chrome()
        inst.driver = webdriver.Chrome(options=options)


        # inst.driver = webdriver.Chrome(executable_path=binary_path)
        print ('Browser started successfully. Navigating to the demo page to login.')
        inst.driver.get('https://www.saucedemo.com/')
        inst.wait = WebDriverWait(inst.driver, 5)

    def login(self, user, password):
        usernameTxt = self.wait.until(presence_of_element_located((By.ID, 'user-name')))
        passwordTxt = self.wait.until(presence_of_element_located((By.ID, 'password')))
        loginBtn = self.wait.until(presence_of_element_located((By.ID, 'login-button')))
        
        # user name
        print ('Login with username: {0}'.format(user))
        usernameTxt.send_keys(user)
        
        # password
        print ('Login with password: {0}'.format(password))
        passwordTxt.send_keys(password)
        
        # click login
        print('Click Login button')
        loginBtn.click()
        print('User {0} login successfully'.format(user))

    def add_or_remove_all_products(self,action):
            productsContainer = self.driver.find_element(By.ID,'inventory_container')
            products = productsContainer.find_elements(By.CLASS_NAME, 'inventory_item')
            for idx, product in enumerate(products):
                productName = product.find_element(By.CLASS_NAME, 'inventory_item_label').find_element(By.TAG_NAME, 'a').text
                cartBtn = product.find_element(By.CLASS_NAME, 'btn_inventory')
                cartBtn.click()
                print('{0} {1} products, product is: {2}'.format(action,idx+1,productName))  

    # Testing with users
    def test_log_in(self): 
		# Login is here with standard_user
        self.login('standard_user', 'secret_sauce')

    def test_add_and_remove_all_products(self): 
        self.login('standard_user', 'secret_sauce')
        
        # Action add
        action = "Add"
        self.add_or_remove_all_products(action)
        cartBadge = self.driver.find_element(By.CSS_SELECTOR, '.shopping_cart_container span').text
        assert cartBadge == '6' , 'The Cart Badge displays 6 products.'
        print('All items are placed in the shopping cart.')

        # Action Remove
        action ="Remove"
        self.add_or_remove_all_products(action)
        cartBadge = self.driver.find_element(By.CLASS_NAME, 'shopping_cart_container').text
        assert cartBadge == '' , 'The Cart Badge displays 0 product.'
        print('All items are taken out of the shopping cart.')

    @classmethod
    def tearDown(self):
         self.driver.quit()

if __name__ == "__main__":
    unittest.main()