from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    get_name.short_description = 'Full Name'
