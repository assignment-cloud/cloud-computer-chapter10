from django.test import TestCase

class IndexViewTest(TestCase):
    def test_index_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        
    def test_index_page_content(self):
        response = self.client.get("/")
        self.assertContains(response, "Cloud Application")
        self.assertContains(response, "Group 10")
        self.assertContains(response, "Cloud Computing")