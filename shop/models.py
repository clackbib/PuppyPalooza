from django.db import models

# Create your models here.

class Puppy(models.Model):
    puppy_name = models.CharField(max_length=30)
    description= models.TextField()
    price = models.FloatField()
    quantity_available = models.PositiveIntegerField()
    picture_name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.puppy_name