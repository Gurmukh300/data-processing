from django.db import models

class Data(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField()
    score = models.IntegerField()
    grade = models.CharField(max_length=1)  # Assuming grade is a single character (A, B, etc.)

    def __str__(self):
        return f'Data: {self.name}'