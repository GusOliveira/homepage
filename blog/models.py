from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length = 250)
    description = models.TextField()
    date = models.DateField() #in the console 1 -> datetime.date.today()

    def __str__(self):
        return self.title