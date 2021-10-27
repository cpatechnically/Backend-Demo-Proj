from django.db import models

# Create your models here.
class Genre(models.Model):
    name                    = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'



class Movie(models.Model):
    title                       = models.CharField(max_length=100, blank=True, null=True)
    genre                       = models.ForeignKey(Genre, on_delete=models.CASCADE, blank=True, null=True)
    number_in_stock             = models.IntegerField(default=1)
    daily_rental_rate           = models.FloatField(default=2.50)
    publish_date                = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'