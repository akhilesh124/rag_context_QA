# from playwright.sync_api import sync_playwright

# class BrowserAgent:
#     def __init__(self):
#         self.playwright = sync_playwright().start()

#         self.browser = self.playwright.chromium.launch_persistent_context(
#             user_data_dir=r"C:\Users\Dell\AppData\Local\Google\Chrome\User Data",
#             headless=False,
#             channel="chrome"
#         )

#         self.page = self.browser.pages[0]

#     def open_site(self, url):
#         self.page.goto(url)
#         self.page.wait_for_timeout(5000)

#     def close(self):
#         self.browser.close()
#         self.playwright.stop()
from playwright.sync_api import sync_playwright
import os

class BrowserAgent:
    def __init__(self):
        self.playwright = sync_playwright().start()

        profile_path = r"C:\playwright_profiles\naukri"
        os.makedirs(profile_path, exist_ok=True)

        self.context = self.playwright.chromium.launch_persistent_context(
            user_data_dir=profile_path,
            headless=False,
            channel="chrome"
        )

        self.page = self.context.new_page()

    def open_site(self, url: str):
        self.page.goto(url, timeout=60000)

    def close(self):
        self.context.close()
        self.playwright.stop()
