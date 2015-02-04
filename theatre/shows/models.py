from django.db import models


class Seat(models.Model):
    row = models.IntegerField()
    column = models.IntegerField()
    name = models.CharField(max_length=10)
    group = models.CharField(max_length=30)

class Ticket(models.Model):
    sold = models.BooleanField(default=False)
    seat = models.ForeignKey(Seat)

class Show(models.Model):
    name = models.CharField(max_length=200)
    length = models.IntegerField()
    description = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    date = models.DateField(null=False)
    tickets = models.ManyToManyField(Ticket)

    def __str__(self):
        return self.name


