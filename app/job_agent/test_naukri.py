from browser_agent import BrowserAgent
import time

browser = BrowserAgent()
browser.open_site("https://www.naukri.com/jobs?q=Node.js+Developer&l=")

print("Browser is open. Press Ctrl+C to exit.")
while True:
    time.sleep(1)