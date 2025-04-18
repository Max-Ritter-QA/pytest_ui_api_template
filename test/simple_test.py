import allure
from Page.AuthPage import AuthPage
from Page.MainPage import MainPage


def test_auth(browser):
    email = "dondontest5@gmail.com"
    password = "21057473Rv!!"
    username = "Donald"

    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, password)

    main_page = MainPage(browser)
    main_page.open_menu()
    info = main_page.get_account_info()

    current_url = main_page.get_current_url()

    with allure.step("Проверить, что URL " + current_url + "заканчивается на dondontest5/boards"):
        assert current_url.endswith("dondontest5/boards")

    with allure.step("Проверить, что указаны данные пользователя"):
        with allure.step("Имя пользователя должно быть " + username):
            assert info[0] == username
        with allure.step("Почта пользователя должна быть " + email):
            assert info[1] == email