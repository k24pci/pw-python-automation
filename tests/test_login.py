def test_login(page):
    page.goto("https://google.com")
    print(page.title())