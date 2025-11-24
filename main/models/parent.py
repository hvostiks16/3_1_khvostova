from django.db import models

class Parent(models.Model):
    name = models.CharField(db_column="Name", max_length=50)
    surname = models.CharField(db_column="Surname", max_length=50)
    patronymic = models.CharField(db_column="Patronymic", max_length=50)
    phone_number = models.CharField(db_column="PhoneNumber", max_length=10)
    email = models.CharField(db_column="Email", max_length=50)
    idParent = models.AutoField(primary_key=True, db_column='idParent')

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic}"

    class Meta:
        db_table = 'Parent'