from selenium import webdriver
from bs4 import BeautifulSoup
from handlers.data import write_output, parse_facts, write_output2, parse_facts2
from handlers.driver import accept_cookies


source = 'https://www.dummysports.com/interesting-f1-facts/'
source_2 = 'https://www.mdd-europe.com/50-f1-facts/'

if __name__ == '__main__':
    # Start a new selenium driver with Chrome
    driver = webdriver.Chrome()
    # Get the content
    driver.get(source)
    # Accept the cookies
    accept_cookies(driver)
    # Set page source to BeautifulSoup so we can parse the HTML data
    soup = BeautifulSoup(driver.page_source, features='html.parser')
    facts = parse_facts(soup)
    # Write output to file
    write_output(facts)
    # Close the driver
    driver.close()

    ###### Second source ######
    # Start a new selenium driver with Chrome
    driver = webdriver.Chrome()
    # Get the content
    driver.get(source_2)
    # Accept the cookies
    accept_cookies(driver)
    # Set page source to BeautifulSoup so we can parse the HTML data
    soup = BeautifulSoup(driver.page_source, features='html.parser')
    facts = parse_facts2(soup)
    # Write output to file
    write_output2(facts)
    # Close the driver
    driver.close()