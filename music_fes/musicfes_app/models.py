from django.db import models

class Reserve(models.Model):
    name = models.CharField(max_length=30)
    sheets = models.IntegerField()
    phone_number = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)

    def __str__(self):
        return '<' + self.name + ' ' + str(self.sheets) \
        + str(self.phone_number) + ' ' + self.adress + '>'

