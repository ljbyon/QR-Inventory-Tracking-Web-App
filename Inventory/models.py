from django.db import models

# Create your models here.
class Alienware(models.Model):
    # This will put a timestamp of whenever a record was added
    created_at = models.DateTimeField(auto_now_add=True)

    serial_number= models.CharField(max_length=30)
    asset_number = models.CharField(max_length=50)
    location = models.CharField(max_length=30)
    updated = models.CharField(max_length=30)
class SparkFunKit(models.Model):
    # This will put a timestamp of whenever a record was added
    created_at = models.DateTimeField(auto_now_add=True)

    serial_number= models.CharField(max_length=30)
    batch_number = models.CharField(max_length=30)
    asset_number = models.CharField(max_length=50)
    location = models.CharField(max_length=30)
    
    def __str__(self):
        return(f"{self.asset_number} {self.location}")