from django.test import TestCase
from datetime import date
from data.models import Data

class TestModel(TestCase):
    def setUp(self):
        # Create a sample Data object
        self.data = Data.objects.create(
            name="John Doe",
            birthdate=date(1990, 1, 1),
            score=85,
            grade="A"
        )

    def test_data_model(self):
        # Retrieve the created Data object from the database
        data_from_db = Data.objects.get(id=self.data.id)

        # Check if the retrieved object matches the created object
        self.assertEqual(data_from_db.name, "John Doe")
        self.assertEqual(data_from_db.birthdate, date(1990, 1, 1))
        self.assertEqual(data_from_db.score, 85)
        self.assertEqual(data_from_db.grade, "A")
