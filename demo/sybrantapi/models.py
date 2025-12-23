from django.db import models

class PersonalProfile(models.Model):
    id = models.CharField(primary_key=True, max_length=20) 
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    class Meta:
        db_table = 'person_profiles'
        managed = False  