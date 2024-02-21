import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AmazonLoginPage:
    def __init__(self, driver):
        self.driver = driver
        time.sleep(10)
        self.sign_in_button = (By.XPATH,"//header/div[@id='navbar']/div[@id='nav-flyout-anchor']/div[13]/div[2]/a[1]/span[1]")
        self.email_input = (By.ID, 'ap_email')
        self.continue_button = (By.ID, 'continue')
        self.password_input = (By.ID, 'ap_password')
        self.sign_in_submit_button = (By.ID, 'signInSubmit')
        self.error_message = (By.ID, 'auth-error-message-box')

    def navigate_to_login_page(self):
        self.driver.find_element(*self.sign_in_button).click()

    def enter_email(self, email):
        self.driver.find_element(*self.email_input).send_keys(email)

    def click_continue_button(self):
        self.driver.find_element(*self.continue_button).click()

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_sign_in_submit_button(self):
        self.driver.find_element(*self.sign_in_submit_button).click()

    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text if self.driver.find_elements(
            *self.error_message) else None


class AmazonHomePage:
    def __init__(self, driver):
        self.driver = driver
        self.welcome_message = (By.ID, 'nav-link-accountList')

    def get_welcome_message(self):
        return self.driver.find_element(*self.welcome_message).text if self.driver.find_elements(
            *self.welcome_message) else None


# Test Case
def test_user_login():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")  # Open the browser in incognito mode
    driver = webdriver.Chrome(options=chrome_options)  # Initialize webdriver
    driver.get("https://www.amazon.com/")  # Open the Amazon website
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    # Initialize Page Objects
    login_page = AmazonLoginPage(driver)
    home_page = AmazonHomePage(driver)

    # Navigate to login page
    login_page.navigate_to_login_page()

    # Test valid login
    login_page.enter_email("syedqc0@gmail.com")
    login_page.click_continue_button()
    login_page.enter_password("Tajusyed1!")
    login_page.click_sign_in_submit_button()
    welcome_message = wait.until(EC.visibility_of_element_located(home_page.welcome_message))
    assert "Account & Lists" in welcome_message.text

    # Test invalid login
    login_page.navigate_to_login_page()
    login_page.enter_email("syedqc09@gmail.com")
    login_page.click_continue_button()
    login_page.enter_password("invalid_password")
    login_page.click_sign_in_submit_button()
    error_message = wait.until(EC.visibility_of_element_located(login_page.error_message))
    assert "There was a problem" in error_message.text

    # Test edge case - empty fields
    login_page.navigate_to_login_page()
    login_page.click_sign_in_submit_button()
    error_message = wait.until(EC.visibility_of_element_located(login_page.error_message))
    assert "Enter your email or mobile phone number" in error_message.text

    driver.quit()  # Quit the webdriver after test completes


# Run the test
if __name__ == "__main__":
    test_user_login()
