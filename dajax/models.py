from django.db import models

# Create your models here.

class DajaxModel(models.Model):
    name = models.CharField(max_length=230)
    email = models.EmailField()
    phone = models.IntegerField(blank=True, null=True)
    address = models.TextField(max_length=230)

    def __str__(self):
        return self.name