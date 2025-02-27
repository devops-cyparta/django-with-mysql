from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    address = models.TextField()
    gender=models.CharField(max_length=10)
    class Meta:
        verbose_name_plural = "Student database"
        db_table = 'Student'
    def __str__(self):
        return self.name
