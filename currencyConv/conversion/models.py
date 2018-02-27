from django.db import models

# Create your models here.
class Values(models.Model):
    class Meta:
        ordering = ['name']
    name = models.CharField(max_length=100)
    value = models.FloatField()


class ConverterHistory(models.Model):
     user_name = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
     )
     history = models.TextField()
