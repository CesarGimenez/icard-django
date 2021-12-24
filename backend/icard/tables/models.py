from django.db import models

class Table(models.Model):
    number = models.IntegerField(unique=True)
    waiter = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.number)
