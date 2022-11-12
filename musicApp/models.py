from django.db import models

# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=100, blank=False)

    def __str__(self) -> str:
        return self.name

class Singer(models.Model):
    name = models.CharField(max_length=100, blank=False)
    age = models.IntegerField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class Music(models.Model):
    title = models.CharField(max_length=100, blank=False)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    created_date = models.DateField()

    def __str__(self) -> str:
        return self.title