from django.test import TestCase
from data.api.urls import urlpatterns

class TestUrls(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Print urlpatterns for inspection
        print("URL patterns:", urlpatterns)

    def test_url_patterns_include_data_router(self):
        # Define the expected URL pattern for the DataViewSet
        expected_url = ''

        # Check if the expected URL is included in urlpatterns
        self.assertIn(expected_url, [pattern.pattern._route for pattern in urlpatterns])