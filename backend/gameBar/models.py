
from django.db import models


class Participant(models.Model):
  name = models.CharField(max_length=50)
  status = models.BooleanField(default=True)

  def __str__(self):
    return self.name


class Bar(models.Model):
  name = models.CharField(max_length=120)
  description = models.TextField()
  address = models.CharField(max_length = 100)
  status = models.BooleanField(default=True)

  def __str__(self):
    return self.name


class Product(models.Model):
  name = models.CharField(max_length=50)
  value = models.FloatField(null=False)
  bar = models.ForeignKey(Bar, related_name='products', on_delete=models.CASCADE)
  status = models.BooleanField(default=True)

  def __str__(self):
    return self.name

class Game(models.Model):
  title = models.CharField(max_length=120)
  description = models.TextField()
  product = models.ForeignKey(Product, on_delete=models.PROTECT)
  bar = models.ForeignKey(Bar, related_name='games', on_delete=models.CASCADE)
  participantA = models.ForeignKey(Participant, related_name="participantA", on_delete=models.PROTECT)
  participantB = models.ForeignKey(Participant, related_name="participantB", on_delete=models.PROTECT)
  opened = models.DateTimeField()
  closed = models.DateTimeField()
  winner = models.ForeignKey(Participant,related_name="winner", on_delete=models.PROTECT)

  def __str__(self):
    return self.title







