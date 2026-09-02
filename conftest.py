import pytest


@pytest.fixture(scope="session")
def base_url():
    return "https://practicesoftwaretesting.com/"


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "headless": False,
        "slow_mo": 800,
    }


@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture(scope="function")
def navigate_to_login(page, base_url):
    page.goto(f"{base_url}auth/login")
    yield page
