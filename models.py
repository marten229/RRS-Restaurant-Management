from django.db import models

class Cuisine(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class OpeningDay(models.Model):
    DAY_CHOICES = [
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
        ('Sun', 'Sunday'),
    ]
    day = models.CharField(max_length=3, choices=DAY_CHOICES, unique=True)

    def __str__(self):
        return self.get_day_display()

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    street = models.CharField(max_length=255, default='Unknown Street')
    city = models.CharField(max_length=100, default='Unknown City')
    house_number = models.CharField(max_length=10, default='0')
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)
    opening_time = models.TimeField(default='09:00')
    closing_time = models.TimeField(default='18:00')
    opening_days = models.ManyToManyField(OpeningDay)
    photo = models.ImageField(upload_to='restaurant_photos/')
    cuisines = models.ManyToManyField(Cuisine)

    def __str__(self):
        return self.name

class Table(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='tables', on_delete=models.CASCADE)
    size = models.IntegerField()
    count = models.IntegerField(default=1)

    def __str__(self):
        return f'Tisch {self.id}: {self.size} Personen, {self.count} Tische'

class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='menu_items', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.name} - {self.price}€'
