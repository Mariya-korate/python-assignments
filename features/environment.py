from utilities import ConfigReader
from selenium import webdriver

def before_scenario(context, scenario):
    # context.driver = webdriver.chrome()
    browser_name = ConfigReader.read_configuration("basic info", "browser")
    print(browser_name)
    if browser_name == "chrome":
        context.driver = webdriver.Chrome()
    elif browser_name == "firefox":
        context.driver = webdriver.Firefox()
    context.driver.implicitly_wait(10)
    context.driver.maximize_window()
    # context.driver.get('https://tutorialsninja.com/demo/')
    context.driver.get(ConfigReader.read_configuration("basic info", "url"))




def after_scenario(context, scenario):
    context.driver.quit()