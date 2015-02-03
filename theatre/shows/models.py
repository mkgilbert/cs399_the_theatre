from django.db import models

class Show(models.Model):
    name = models.CharField(max_length=200)
    length = models.IntegerField()
    description = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    date = models.DateField(null=False)

    def __str__(self):
        return self.name
