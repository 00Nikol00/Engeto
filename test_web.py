from playwright.sync_api import sync_playwright

#URL adresa testovaného webu
URL_web_page = "https://www.mg-sskvitkovice.cz/"


def test_homepage_nav():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(URL_web_page)
        
        page.wait_for_load_state('domcontentloaded')

        navigation_element = page.locator('nav#main-navigation')
        
        assert navigation_element.is_visible(), "Navigace není načtena."

        browser.close()

def test_nav_click_contacts():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        page.goto(URL_web_page)
        
        page.wait_for_load_state('domcontentloaded')
        
        test_element = page.locator('//*[@id="menu-item-1685"]/a')

        assert test_element.is_visible(), "je mě vidět, není mě vidět"

        test_element.click()

        
        page.wait_for_load_state('domcontentloaded')
        
        test_element = page.locator('//*[@id="content"]/div/div[1]/div/article/div/h1')

        assert test_element.inner_text() == 'Kontakt', "je mě vidět, není mě vidět"     
        browser.close()

def test_user_login():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('https://www.mg-sskvitkovice.cz/wp-login.php')
        page.fill('//*[@id="user_login"]', 'fakeuser')
        page.fill('//*[@id="user_pass"]', 'fakepassword')
        page.click('//*[@id="wp-submit"]')
        page.wait_for_selector("load")
        error_message_element = page.locator('//*[@id="login_error"]')
        assert error_message_element.is_visible(), "Je to v lese..."

        browser.close()




test_homepage_nav()
test_nav_click_contacts()
test_user_login()