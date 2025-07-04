import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")
    yield driver
    driver.quit()

def test_login_valid(browser):
    browser.get("https://example.com/login")
    browser.find_element(By.NAME, "username").send_keys("admin")
    browser.find_element(By.NAME, "password").send_keys("password123")
    browser.find_element(By.ID, "loginBtn").click()
    time.sleep(2)
    assert "dashboard" in browser.current_url

