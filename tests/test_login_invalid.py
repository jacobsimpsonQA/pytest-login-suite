from utils import login

def test_invalid_login(driver):
    login(driver, "student", "wrongpassword")
    assert "Your password is invalid!" in driver.page_source
    print("❌ test_invalid_login passed – error shown")
