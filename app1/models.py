from django.db import models

# Create your models here.


class Granpa(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Papa(models.Model):
    granpa = models.ForeignKey(Granpa)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Child(models.Model):
    papa = models.ForeignKey(Papa)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
