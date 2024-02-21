from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AmazonHomePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.ID, 'twotabsearchtextbox')
        self.search_button = (By.ID, 'nav-search-submit-button')
        self.search_result_links = (By.CSS_SELECTOR, 'a.a-link-normal.a-text-normal')

    def search_product(self, product_name):
        search_input = self.driver.find_element(*self.search_box)
        search_input.clear()
        search_input.send_keys(product_name)
        self.driver.find_element(*self.search_button).click()

    def click_on_product(self, index):
        search_results = self.driver.find_elements(*self.search_result_links)
        search_results[index].click()

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_button = (By.ID, 'add-to-cart-button')
        self.cart_count = (By.ID, 'nav-cart-count')
        self.cart_button = (By.ID, 'nav-cart')

    def add_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()

    def get_cart_count(self):
        return self.driver.find_element(*self.cart_count).text

    def navigate_to_cart(self):
        self.driver.find_element(*self.cart_button).click()

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_items = (By.CSS_SELECTOR, 'div.sc-list-item-content')
        self.delete_button = (By.CSS_SELECTOR, 'input[value="Delete"]')

    def get_cart_items_count(self):
        return len(self.driver.find_elements(*self.cart_items))

    def remove_item_from_cart(self):
        self.driver.find_element(*self.delete_button).click()

# Test Case
def test_add_to_cart():
    ch_options = Options()
    ch_options.add_argument('--incognito')
    driver = webdriver.Chrome(options=ch_options)  # Initialize webdriver
    driver.maximize_window()

    # Initialize Page Objects
    amazon_homepage = AmazonHomePage(driver)
    product_page = ProductPage(driver)
    cart_page = CartPage(driver)

    # Search for a product
    amazon_homepage.search_product("Laptop")
    # Click on the first search result
    amazon_homepage.click_on_product(0)

    # Add the product to the cart
    product_page.add_to_cart()

    # Verify item added to cart
    assert product_page.get_cart_count() == "1"

    # Navigate to the cart
    product_page.navigate_to_cart()

    # Verify cart contains the added item
    assert cart_page.get_cart_items_count() == 1

    # Remove item from the cart
    cart_page.remove_item_from_cart()

    # Verify cart is empty
    assert cart_page.get_cart_items_count() == 0

    driver.quit()

# Run the test
if __name__ == "__main__":
    test_add_to_cart()
