from Page.AuthPage import AuthPage

def test_auth(browser):
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as("dondontest5@gmail.com", "21057473Rv!!")

    assert auth_page.get_current_url().endswith("dondontest5/boards")