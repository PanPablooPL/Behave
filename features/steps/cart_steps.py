from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

@given('I am on the homepage')
def step_given_i_am_on_the_homepage(context):
    context.browser = webdriver.Chrome()
    context.browser.get("https://bstackdemo.com/")

@when('I sign in')
def step_when_i_sign_in(context):
    context.browser.find_element(By.LINK_TEXT, "Sign In").click()

    WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#username .css-1hwfws3'))
    ).click()
    context.browser.find_element(By.CSS_SELECTOR, 'div[id^="react-select-2-option-0-0"]').click()

    context.browser.find_element(By.CSS_SELECTOR, '#password .css-1hwfws3').click()
    context.browser.find_element(By.CSS_SELECTOR, 'div[id^="react-select-3-option-0-0"]').click()

    context.browser.find_element(By.ID, 'login-btn').click()

    WebDriverWait(context.browser, 10).until(
        EC.url_changes("https://bstackdemo.com/")
    )

@when('I add the first product to the cart')
def step_when_i_add_the_first_product_to_the_cart(context):
    WebDriverWait(context.browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.shelf-item'))
    )

    try:
        add_to_cart_buttons = WebDriverWait(context.browser, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.shelf-item__buy-btn'))
        )
        if add_to_cart_buttons:
            add_to_cart_buttons[0].click()
        else:
            raise Exception("No 'Add to cart' button found.")

        time.sleep(5)

    except TimeoutException:
        print("Timed out waiting for 'Add to cart' buttons to be present.")
        raise

@then('I take a screenshot of the cart item')
def step_then_i_take_a_screenshot_of_the_cart_item(context):
    try:
        try:
            cart_button = WebDriverWait(context.browser, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '.float-cart__header'))
            )
            cart_button.click()
        except TimeoutException:
            print("Cart button not found within the timeout period")
            raise

        WebDriverWait(context.browser, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.float-cart__content'))
        )

        cart_item_element = WebDriverWait(context.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.float-cart__content .shelf-item'))
        )

        screenshot_path = "cart_item_screenshot.png"
        cart_item_element.screenshot(screenshot_path)
        print(f"Screenshot of the cart item saved as '{screenshot_path}'")

    except TimeoutException:
        print("Cart item not found within the timeout period")
        raise

@then('I log out')
def step_then_i_log_out(context):
    context.browser.find_element(By.LINK_TEXT, "Logout").click()
    WebDriverWait(context.browser, 10).until(
        EC.url_to_be("https://bstackdemo.com/")
    )
    context.browser.quit()
