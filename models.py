from django.db import models

class Cuisine(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class OpeningDay(models.Model):
    DAY_CHOICES = [
        ('Mon', 'Montag'),
        ('Tue', 'Dienstag'),
        ('Wed', 'Mittwoch'),
        ('Thu', 'Donnerstag'),
        ('Fri', 'Freitag'),
        ('Sat', 'Samstag'),
        ('Sun', 'Sonntag'),
    ]
    day = models.CharField(max_length=3, choices=DAY_CHOICES, unique=True)

    def __str__(self):
        return self.get_day_display()

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    street = models.CharField(max_length=255, default='Strasse')
    city = models.CharField(max_length=100, default='Stadt')
    house_number = models.CharField(max_length=10, default='0')
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)
    opening_time = models.TimeField(default='09:00')
    closing_time = models.TimeField(default='18:00')
    opening_days = models.ManyToManyField(OpeningDay)
    photo = models.ImageField(upload_to='restaurant_photos/')
    cuisines = models.ManyToManyField(Cuisine)

    def check_ifopendayandtime(self, date, time): 
        day_short = date.strftime('%a')[:3]
        if self.opening_days.filter(day=day_short).exists():
            if self.opening_time <= time <= self.closing_time:
                return True
        return False
    

    def __str__(self):
        return self.name

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='menu_items', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.name} - {self.price}€'
