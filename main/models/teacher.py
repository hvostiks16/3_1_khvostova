from django.db import models

class Teacher(models.Model):
    name = models.CharField(db_column='Name', max_length=45)
    surname = models.CharField(db_column='Surname', max_length=50)
    patronymic = models.CharField(db_column='Patronymic', max_length=50)
    phone_number = models.CharField(db_column='PhoneNumber', max_length=50)
    email = models.CharField(db_column='Email', max_length=50)

    class Meta:
        db_table = 'Teacher'
