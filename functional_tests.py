from selenium import webdriver
import unittest

class MyTests(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_before_login_main_page(self):
		self.browser.get('http://localhost:8000')

		self.assertIn('Logowanie', self.browser.title)

if __name__ == '__main__':
	unittest.main(warnings='ignore')
