from django.db import models

class Cuisine(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=255)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)
    opening_hours = models.CharField(max_length=255)
    menu = models.TextField()
    photo = models.ImageField(upload_to='restaurant_photos/')
    cuisines = models.ManyToManyField(Cuisine)

    def __str__(self):
        return self.name

class Table(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='tables', on_delete=models.CASCADE)
    size = models.IntegerField()
    count = models.IntegerField()

    def __str__(self):
        return f'{self.size} Personen, {self.count} Tische'