#after altering the models:
#1 - python manage.py makemigrations
#2 - python manage.py migrate --run-syncdb
#3 - python manage.py runserver

from django.db import models

class Project(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 250)
    image = models.ImageField(upload_to='portifolio/images/')
    url = models.URLField(blank = True)

    def __str__(self):
        return self.title