from django.db import models

class Project(models.Model):
    title = models.CharField(max_length = 100)
    value = models.CharField(max_length = 100)
    date = models.DateField() #in the console 1 -> datetime.date.today()
    quantity = models.CharField(max_length = 100)


    def __str__(self):
        return self.title

