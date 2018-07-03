import unittest
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

class automation(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_page_load_timeout(30)

    def test_see_news_comment_login_with_google(self):
        driver = self.driver
        #1 Visit https://kumparan.com/
        driver.get('https://kumparan.com/')
        self.assertIn('kumparan', self.driver.title)

        #2 Select some news
        driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div/div/div[2]/div[1]/div[2]/div[1]/div[2]').click()
        time.sleep(5)

        #3 Insert comment
        comment = driver.find_element_by_xpath('//*[@id="newCommentTextArea"]')
        comment.send_keys('test')
        wait(driver, 50)
        driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div/div[2]/div/div/div[1]/div/div[2]/div[3]/div/div[1]/div/div/div/div/div/div/div[2]/div[3]/button').click()

        #4 Login with Google Plus
        wait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/div/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/button'))).click()
        main_window_handle = None
        while not main_window_handle:
            main_window_handle = driver.current_window_handle
        signin_window_handle = None
        while not signin_window_handle:
            for handle in driver.window_handles:
                if handle!= main_window_handle:
                    signin_window_handle = handle
                    break
        driver.switch_to.window(signin_window_handle)
        wait(driver, 50)
        email = driver.find_element_by_id('identifierId')
        email.send_keys('mich.kotamori69@gmail.com')
        wait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'identifierNext'))).click()
        time.sleep(2)
        password = driver.find_element_by_name('password')
        password.send_keys('michkotamori')
        wait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'passwordNext'))).click()
        driver.switch_to.window(main_window_handle)
        time.sleep(2)

        #5 Insert comment again
        comment = driver.find_element_by_xpath('//*[@id="newCommentTextArea"]')
        comment.send_keys('test')
        wait(driver, 50)
        driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div/div[2]/div/div/div[1]/div/div[2]/div[3]/div/div[1]/div/div/div/div/div/div/div[2]/div[3]/button').click()

    def test_see_news_comment_login_with_facebook(self):
        driver = self.driver
        #1 Visit https://kumparan.com/
        driver.get('https://kumparan.com/')
        self.assertIn('kumparan', self.driver.title)

        #2 Select some news
        driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div/div/div[2]/div[1]/div[2]/div[1]/div[2]').click()
        time.sleep(5)

        #3 Insert comment
        comment = driver.find_element_by_xpath('//*[@id="newCommentTextArea"]')
        comment.send_keys('test')
        wait(driver, 50)
        driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div/div[2]/div/div/div[1]/div/div[2]/div[3]/div/div[1]/div/div/div/div/div/div/div[2]/div[3]/button').click()

        #4 Login with Facebook
        wait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/div/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/span/button'))).click()
        main_window_handle = None
        while not main_window_handle:
            main_window_handle = driver.current_window_handle
        signin_window_handle = None
        while not signin_window_handle:
            for handle in driver.window_handles:
                if handle!= main_window_handle:
                    signin_window_handle = handle
                    break
        driver.switch_to.window(signin_window_handle)
        wait(driver, 50)
        email = driver.find_element_by_xpath('//*[@id="email"]')
        email.send_keys('filza.94@gmail.com')
        password = driver.find_element_by_xpath('//*[@id="pass"]')
        password.send_keys('test123456')
        wait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="u_0_0"]'))).click()
        driver.switch_to.window(main_window_handle)
        time.sleep(2)

        #5 Insert comment again
        comment = driver.find_element_by_xpath('//*[@id="newCommentTextArea"]')
        comment.send_keys('test')
        wait(driver, 50)
        driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div/div[2]/div/div/div[1]/div/div[2]/div[3]/div/div[1]/div/div/div/div/div/div/div[2]/div[3]/button').click()

    #def test_negative_test(self):
    #    driver = self.driver
    #    #1 Visit https://kumparan.com/
    #    driver.get('https://kumparan.com/')
    #    self.assertIn('kumparan', self.driver.title)

    def tearDown(self):
        time.sleep(5)
        self.driver.close()


if __name__ == '__main__':
    unittest.main()