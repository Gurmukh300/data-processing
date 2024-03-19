# from django.db import IntegrityError
# from django.test import TestCase

# # Create your tests here.
# import tempfile
# from django.core.files.uploadedfile import SimpleUploadedFile
# from rest_framework.test import APITestCase
# from data.models import Data

# from datetime import date

# from data.api.serializers import DataSerializer

# from django.urls import reverse, resolve
# from data.api.urls import urlpatterns
# from data.api.views import DataViewSet


# class UploadCSVTestCase(APITestCase):
#     def test_upload_valid_csv(self):
#         # Create a temporary CSV file with valid data
#         csv_data = "name,birthdate,score,grade\nAlice,1990-01-01,90,A\nBob,1991-02-02,75,B"
#         csv_file = SimpleUploadedFile("data.csv", csv_data.encode())

#         # Upload the CSV file
#         response = self.client.post("/api/data/upload_csv/", {"file": csv_file}, format="multipart")

#         # Assert that the response is successful
#         self.assertEqual(response.status_code, 200)

#         # Assert that data is saved to the database
#         self.assertEqual(Data.objects.count(), 2)

#     def test_upload_invalid_file_format(self):
#         # Upload a file with invalid format (not CSV)
#         response = self.client.post("/api/data/upload_csv/", {"file": "invalid_file.txt"}, format="multipart")

#         # Assert that the response indicates an error
#         self.assertEqual(response.status_code, 400)

#         # Assert that no data is saved to the database
#         self.assertEqual(Data.objects.count(), 0)

#     # Add more test cases here for different scenarios (missing columns, incorrect date format, etc.)
# class DataModelTestCase(TestCase):
#     def setUp(self):
#         # Create a sample Data object
#         self.data = Data.objects.create(
#             name="John Doe",
#             birthdate=date(1990, 1, 1),
#             score=85,
#             grade="A"
#         )

#     def test_data_model(self):
#         # Retrieve the created Data object from the database
#         data_from_db = Data.objects.get(id=self.data.id)

#         # Check if the retrieved object matches the created object
#         self.assertEqual(data_from_db.name, "John Doe")
#         self.assertEqual(data_from_db.birthdate, date(1990, 1, 1))
#         self.assertEqual(data_from_db.score, 85)
#         self.assertEqual(data_from_db.grade, "A")


# class TestDataSerializer(TestCase):
#     def test_serializer_valid_data(self):
#         # Create a Data object
#         data = Data.objects.create(
#             name='John Doe',
#             birthdate=date(1990, 1, 1),
#             score=80,
#             grade='A'
#         )

#         # Serialize the Data object
#         serializer = DataSerializer(data)

#         # Check if the serializer data matches the expected data
#         self.assertEqual(serializer.data, {
#             'id': data.id,
#             'name': 'John Doe',
#             'birthdate': '1990-01-01',  # Convert date to string
#             'score': 80,
#             'grade': 'A'
#         })
        
#     def test_serializer_invalid_data(self):
#         # Attempt to create a Data object with missing required fields
#         with self.assertRaises(IntegrityError):
#             Data.objects.create(name='John Doe')


# class TestUrls(TestCase):
#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()
#         # Print urlpatterns for inspection
#         print("URL patterns:", urlpatterns)

#     def test_url_patterns_include_data_router(self):
#         # Define the expected URL pattern for the DataViewSet
#         expected_url = ''

#         # Check if the expected URL is included in urlpatterns
#         self.assertIn(expected_url, [pattern.pattern._route for pattern in urlpatterns])