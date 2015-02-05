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
    image = models.CharField(max_length=200,default="") # link to image


    def _tickets_available(self):
        count = 0
        for ticket in self.tickets.all():
            if not ticket.sold:
                count += 1
        return count

    tickets_available = property(_tickets_available)

    def __str__(self):
        return self.name


