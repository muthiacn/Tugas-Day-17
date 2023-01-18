import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_login_positif(self): 
        # steps
        browser = self.browser 
        browser.get("http://barru.pythonanywhere.com/daftar") 
        time.sleep(3)
        browser.find_element(By.ID,"email").send_keys("qonitamuthia@gmail.com") 
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("muthia16") 
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Welcome', response_data)
        self.assertEqual(response_message, 'Anda Berhasil Login')

    def test_login_empty(self): 
        browser = self.browser 
        browser.get("http://barru.pythonanywhere.com/daftar") 
        time.sleep(3)
        browser.find_element(By.ID,"email").send_keys("") 
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("")
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click() 
        time.sleep(1)

        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn("User's not found", response_data)
        self.assertEqual(response_message, 'Email atau Password Anda Salah')

    def test_login_negatif(self): 
        browser = self.browser 
        browser.get("http://barru.pythonanywhere.com/daftar") 
        time.sleep(3)
        browser.find_element(By.ID,"email").send_keys("conitamuthia@gmail.com") 
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("muthia17")
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click() 
        time.sleep(1)
        
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn("User's not found", response_data)
        self.assertEqual(response_message, 'Email atau Password Anda Salah')


    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()