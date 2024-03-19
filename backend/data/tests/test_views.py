
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APITestCase
from data.models import Data



class TestViews(APITestCase):
    def test_upload_valid_csv(self):
        # Create a temporary CSV file with valid data
        csv_data = "name,birthdate,score,grade\nAlice,1990-01-01,90,A\nBob,1991-02-02,75,B"
        csv_file = SimpleUploadedFile("data.csv", csv_data.encode())

        # Upload the CSV file
        response = self.client.post("/api/data/upload_csv/", {"file": csv_file}, format="multipart")

        # Assert that the response is successful
        self.assertEqual(response.status_code, 200)

        # Assert that data is saved to the database
        self.assertEqual(Data.objects.count(), 2)

    def test_upload_invalid_file_format(self):
        # Upload a file with invalid format (not CSV)
        response = self.client.post("/api/data/upload_csv/", {"file": "invalid_file.txt"}, format="multipart")

        # Assert that the response indicates an error
        self.assertEqual(response.status_code, 400)

        # Assert that no data is saved to the database
        self.assertEqual(Data.objects.count(), 0)