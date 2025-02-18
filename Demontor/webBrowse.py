import selenium

from selenium.webdriver import Firefox, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options


tickerChoice = input("Enter ticker: ")

if tickerChoice is not None:
    opts = Options()
    opts.headless = True
    assert opts.headless
    browser = Firefox(options=opts)
    browser.get('https://app.webull.com/stocks')

    popup_form = browser.find_element(By.CLASS_NAME, "jss455.webull-cancel_.jss456.jss2")
    popup_form.click()

    popup_form2 = browser.find_element(By.CLASS_NAME, "jss455.webull-cancel_.jss456.jss373")
    popup_form2.click()

    search_form = browser.find_element(By.CLASS_NAME, "jss147.jss155.jss149")
    search_form.send_keys(tickerChoice)
    search_form.send_keys(Keys.RETURN)


