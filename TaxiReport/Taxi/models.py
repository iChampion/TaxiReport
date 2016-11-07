from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Cars(models.Model):
    marka = models.CharField('Марка', max_length=24)
    model = models.CharField('Модель', max_length=24)
    vincode = models.IntegerField('VIN код', blank=True, null=True)
    Agestart = models.DateTimeField('Дата с', blank=True, null=True)
    ctc = models.CharField('CTC', max_length=24)
    number = models.CharField('Гос Номер', max_length=24)
    inwork = models.DateTimeField('В работе с', blank=True, null=True)
    active = models.BooleanField('В работе')
    createown = models.ForeignKey(User, unique=True)
    datacreate = models.DateTimeField('Дата заведения', blank=True, null=True)

