from django.test import TestCase
from datetime import date
from data.models import Data
from data.api.serializers import DataSerializer
from django.db import IntegrityError

class TestDataSerializer(TestCase):
    def test_serializer_valid_data(self):
        # Create a Data object
        data = Data.objects.create(
            name='John Doe',
            birthdate=date(1990, 1, 1),
            score=80,
            grade='A'
        )

        # Serialize the Data object
        serializer = DataSerializer(data)

        # Check if the serializer data matches the expected data
        self.assertEqual(serializer.data, {
            'id': data.id,
            'name': 'John Doe',
            'birthdate': '1990-01-01',  # Convert date to string
            'score': 80,
            'grade': 'A'
        })
        
    def test_serializer_invalid_data(self):
        # Attempt to create a Data object with missing required fields
        with self.assertRaises(IntegrityError):
            Data.objects.create(name='John Doe')
