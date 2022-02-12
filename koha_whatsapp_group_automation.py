import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import json
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager
from requests.structures import CaseInsensitiveDict
from selenium.webdriver.support.ui import Select
import sys
import re

f = open('member_details.json')

def enter_login(browser):
	print("Entering username, password and captcha")

	old_url = browser.current_url

	browser.find_element_by_xpath("//*[@id='userid']").send_keys("")

	browser.find_element_by_xpath("//*[@id='password']").send_keys("")

	browser.find_element_by_xpath("//*[@id='submit-button']").click()

def enter_member_info(browser, member_info):
	member_id = member_info["member_id"]
	whatsapp_group_name = member_info["whatsapp_group_name"]

	browser.find_element_by_xpath("//*[@id='searchmember']").send_keys(member_id)

	# click submit
	try:
		browser.find_element_by_xpath("//*[@id='patron_search']/form/input[3]").click()
	except:
		browser.find_element_by_xpath("//*[@id='patron_search']/form/div[1]/input[3]").click()

	# timeout = 25

	# try:
	# 	element_present = EC.element_to_be_clickable((By.XPATH, "//*[@id='patron-extended-attributes']/div/a"))
	# 	WebDriverWait(browser, timeout).until(element_present)
	# except TimeoutException:
	# 	print("Timed out waiting for page to load")


	# Add attributes
	# browser.find_element_by_xpath("//*[@id='patron-extended-attributes']/div/a").click()

	button = browser.find_element_by_xpath("//*[@id='patron-extended-attributes']/div/a")
	browser.execute_script("arguments[0].click();", button)


	#Add whatsapp group name
	browser.find_element_by_xpath("//*[@id='patron_attr_7']").send_keys(whatsapp_group_name)

def search_patrons(browser):

	# Search patrons
	browser.find_element_by_xpath("//*[@id='ui-id-4']").click()

	member_json_list = json.load(f)

	for member_info in member_json_list:
		enter_member_info(browser, member_info)


if __name__ == '__main__':
	website_link = "http://tclpstaff.bestbookbuddies.com/"


	chrome_options = Options()
	# chrome_options.add_argument('--headless')
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument('--disable-dev-shm-usage')
	# options.headless = True

	browser = webdriver.Chrome(options=chrome_options)

	browser.get(website_link)

	enter_login(browser)
	search_patrons(browser)
