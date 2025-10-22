from django.db import models
from .form import Form

class Student(models.Model):
    class StudentPrivilege(models.TextChoices):
        NONE = 'NONE', 'None'
        ORPHAN = 'ORPHAN', 'Orphan'
        LOWINCOME = 'LOWINCOME', 'LowIncome'
        DISABLED = 'DISABLED', 'Disabled'
        LARGEFAMILY = 'LARGEFAMILY', 'LargeFamily'
        WARVETERANCHILD = 'WARVETERANCHILD', 'WarVeteranChild'
        SCHOLARSHIP = 'SCHOLARSHIP', 'Scholarship'

    name = models.CharField(db_column="Name", max_length=50)
    surname = models.CharField(db_column="Surname", max_length=50)
    patronymic = models.CharField(db_column="Patronymic", max_length=50)
    phone_number = models.CharField(db_column="PhoneNumber", max_length=10)
    email = models.CharField(db_column="Email", max_length=50)
    privilege = models.CharField(
        db_column='Privilege',
        max_length=50,
        choices=StudentPrivilege.choices,
        default=StudentPrivilege.NONE)
    date_of_birth = models.DateField(db_column="DateOfBirth")
    city = models.CharField(db_column="City", max_length=45)
    neighborhood = models.CharField(db_column="Neighborhood", max_length=45)
    street = models.CharField(db_column="Street", max_length=45)
    building = models.CharField(db_column="Building", max_length=45)
    apartment = models.CharField(db_column="Apartment", max_length=45)

    id_form = models.ForeignKey(Form, db_column='idClass', on_delete=models.SET_NULL, null=True)
    idStudent = models.AutoField(primary_key=True, db_column='idStudent')

    class Meta:
        db_table = 'Student'