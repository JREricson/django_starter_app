# import time

# from django.test import LiveServerTestCase
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys


# class Hosttest(LiveServerTestCase):
#     def testhomepage(self):
#         driver = webdriver.Chrome()
#         # try driver = webdriver.Chrome('./chromedriver') with the driver in the project folder if you cant set to path

#         driver.get(self.live_server_url)
#         # try driver.get(self.live_server_url) if driver.get('http://127.0.0.1:8000/') does not work

#         assert "App" in driver.title
