from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=120)
    age = models.PositiveIntegerField()
    grade = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.name} ({self.grade})"
