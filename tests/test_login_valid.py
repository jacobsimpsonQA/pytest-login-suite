from utils import login

def test_valid_login(driver):
    login(driver, "student", "Password123")
    assert "Logged In Successfully" in driver.page_source
    print("✅ test_valid_login passed")

