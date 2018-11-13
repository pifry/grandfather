from django.test import TestCase

# Create your tests here.

class MainPageTests(TestCase):

	def test_main_page_status_code(self):
		response = self.client.get('/')
		self.assertEquals(response.status_code, 200)

	def test_main_page_without_login_is_login_page(self):
		response = self.client.get('/')
		self.assertContains(response, "Logowanie")