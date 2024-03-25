from django.db import models
from django.utils import timezone
# Create your models here.
class SA_Serial_Numbers(models.Model):
    # This will put a timestamp of whenever a record was added
    created_at = models.DateTimeField(auto_now_add=True)
    serial_number= models.CharField(max_length=100)
    last_checked = models.CharField(max_length=100, default=timezone.now)


class Alienware(models.Model):
    # This will put a timestamp of whenever a record was added
    created_at = models.DateTimeField(auto_now_add=True)
    serial_number= models.CharField(max_length=100)
    sa_serial_number = models.CharField(max_length=100)
    location = models.CharField(max_length=100)


# IGNORE THIS ONE BELOW
class alienware_table(models.Model):
    serial_number = models.CharField(max_length=100)
    last_checked = models.CharField(max_length=100)
    sa_serial_number = models.CharField(max_length=100, primary_key=True)
    location = models.CharField(max_length=100)

    class Meta:
        managed = False  # Set managed to False to tell Django not to manage this model's database table
        db_table = 'alienware_table'  # Name of the view in the database


class new_alienware_table(models.Model):
    serial_number = models.CharField(max_length=100)
    last_checked = models.CharField(max_length=100)
    sa_serial_number = models.CharField(max_length=100, primary_key=True)
    location = models.CharField(max_length=100)

    class Meta:
        managed = False  # Set managed to False to tell Django not to manage this model's database table
        db_table = 'new_alienware_table'  # Name of the view in the database


class SparkFunKit(models.Model):
    # This will put a timestamp of whenever a record was added
    created_at = models.DateTimeField(auto_now_add=True)

    serial_number= models.CharField(max_length=100)
    batch_number = models.CharField(max_length=100)
    sa_serial_number = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

class sparkfun_table(models.Model):
    serial_number = models.CharField(max_length=100)
    batch_number = models.CharField(max_length=100, primary_key=True)
    last_checked = models.CharField(max_length=100)
    sa_serial_number = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    class Meta:
        managed = False  # Set managed to False to tell Django not to manage this model's database table
        db_table = 'sparkfun_table'  # Name of the view in the database
    
class teacherpack(models.Model):
    # This will put a timestamp of whenever a record was added
    created_at = models.DateTimeField(auto_now_add=True)
    serial_number= models.CharField(max_length=100)
    sa_serial_number = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

class teacherpack_table(models.Model):
    serial_number = models.CharField(max_length=100, primary_key=True)
    last_checked = models.CharField(max_length=100)
    sa_serial_number = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    class Meta:
        managed = False  # Set managed to False to tell Django not to manage this model's database table
        db_table = 'teacherpack_table'  # Name of the view in the database

class Raspberry_Pi(models.Model):
    # This will put a timestamp of whenever a record was added
    created_at = models.DateTimeField(auto_now_add=True)
    sa_serial_number = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

class raspberry_pi_table(models.Model):
    last_checked = models.CharField(max_length=100)
    sa_serial_number = models.CharField(max_length=100, primary_key =True)
    location = models.CharField(max_length=100)

    class Meta:
        managed = False  # Set managed to False to tell Django not to manage this model's database table
        db_table = 'raspberry_pi_table'  # Name of the view in the database