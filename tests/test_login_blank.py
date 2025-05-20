from utils import login

def test_blank_login(driver):
    login(driver, "", "")
    error_message = driver.find_element("id", "error").text
    assert "Your username is invalid!" in error_message or "Your password is invalid!" in error_message
    print("⚠️ test_blank_login passed – blank credentials properly rejected")
