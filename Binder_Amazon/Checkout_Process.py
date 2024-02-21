from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_input = (By.ID, 'ap_email')
        self.password_input = (By.ID, 'ap_password')
        self.sign_in_button = (By.ID, 'signInSubmit')

    def login(self, email, password):
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.sign_in_button).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'ap_password')))
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.sign_in_button).click()

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.proceed_to_checkout_button = (By.CSS_SELECTOR, '#sc-buy-box-ptc-button span.a-button-inner')
        self.subtotal = (By.CSS_SELECTOR, '.sc-subtotal-buy-box .a-span-last')

    def proceed_to_checkout(self):
        self.driver.find_element(*self.proceed_to_checkout_button).click()

class AddressPage:
    def __init__(self, driver):
        self.driver = driver
        self.shipping_address_radio = (By.ID, 'address-book-entry-0')
        self.continue_button = (By.CSS_SELECTOR, 'input.a-button-input')

    def select_shipping_address(self):
        self.driver.find_element(*self.shipping_address_radio).click()
        self.driver.find_element(*self.continue_button).click()

class PaymentPage:
    def __init__(self, driver):
        self.driver = driver
        self.payment_method_radio = (By.ID, 'pm_1')
        self.continue_button = (By.CSS_SELECTOR, 'input.a-button-input')

    def select_payment_method(self):
        self.driver.find_element(*self.payment_method_radio).click()
        self.driver.find_element(*self.continue_button).click()

class OrderSummaryPage:
    def __init__(self, driver):
        self.driver = driver
        self.place_order_button = (By.CSS_SELECTOR, '#submitOrderButtonId span.a-button-inner')

    def place_order(self):
        self.driver.find_element(*self.place_order_button).click()

# Test Case
def test_checkout_process():
    ch_options = Options()
    ch_options.add_argument('--incognito')
    driver = webdriver.Chrome(options=ch_options)  # Initialize webdriver
    driver.maximize_window()

    # Initialize Page Objects
    login_page = LoginPage(driver)
    cart_page = CartPage(driver)
    address_page = AddressPage(driver)
    payment_page = PaymentPage(driver)
    order_summary_page = OrderSummaryPage(driver)

    # Login
    login_page.login("syedqc0@gmail.com", "Tajusyed1!")

    # Add items to cart and proceed to checkout
    # (Add your steps to add items to the cart)

    # Proceed to checkout from the cart
    cart_page.proceed_to_checkout()

    # Select shipping address
    address_page.select_shipping_address()

    # Select payment method
    payment_page.select_payment_method()

    # Place the order
    order_summary_page.place_order()

    # Assert order confirmation
    assert "Thank you for your purchase" in driver.page_source

    driver.quit()  # Quit the webdriver after test completes

# Run the test
if __name__ == "__main__":
    test_checkout_process()
