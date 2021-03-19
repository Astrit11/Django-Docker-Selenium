from pyvirtualdisplay import Display
from selenium import webdriver


def test():
    display = Display(visible=0, size=(800, 600))
    display.start()
    baseURl = 'https:google.com'
    browser = webdriver.Firefox()
    browser.get(baseURl)
    print(browser.title)   

    
