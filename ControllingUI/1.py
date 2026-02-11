import os
from playwright.sync_api import sync_playwright

# Path to Firefox executable (default install location)
firefox_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"

if os.path.exists(firefox_path):
	os.startfile(firefox_path)
else:
	print("Firefox not found at the default location.")

sync_playwright().start()
with sync_playwright() as p:
	browser = p.firefox.launch(headless=False)
	page = browser.new_page()
	page.goto("https://www.example.com")
	print(page.title())
	browser.close()

sync_playwright().stop()
