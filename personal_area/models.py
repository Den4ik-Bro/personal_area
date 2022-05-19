from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Skills(models.Model):
    name = models.CharField(max_length=50, verbose_name='название', null=True, blank=True)
    user = models.ManyToManyField(User, blank=True, related_name='skills')

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=50, verbose_name='название', null=True, blank=True)
    user = models.ManyToManyField(User, blank=True, related_name='languages')

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'

    def __str__(self):
        return self.name


class Hobby(models.Model):
    name = models.CharField(max_length=50, verbose_name='название', null=True, blank=True)
    user = models.ManyToManyField(User, blank=True, related_name='hobbys')

    class Meta:
        verbose_name = 'Увлечение'
        verbose_name_plural = 'Увлечения'

    def __str__(self):
        return self.name