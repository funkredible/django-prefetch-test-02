from django.db import models

# Create your models here.


class Granpa(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Papa(models.Model):
    granpa = models.ForeignKey(Granpa, related_name='papas')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Child(models.Model):
    papa = models.ForeignKey(Papa, related_name='children')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
