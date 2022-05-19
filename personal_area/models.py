from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Skills(models.Model):
    skill = models.CharField(max_length=50, verbose_name='навык', null=True, blank=True)
    user = models.ManyToManyField(User, blank=True, related_name='user_skill')

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'

    def __str__(self):
        return self.skill


class Language(models.Model):
    language = models.CharField(max_length=50, verbose_name='язык', null=True, blank=True)
    user = models.ManyToManyField(User, blank=True, related_name='user_language')

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'

    def __str__(self):
        return self.language


class Hobby(models.Model):
    hobby = models.CharField(max_length=50, verbose_name='увлечения', null=True, blank=True)
    user = models.ManyToManyField(User, blank=True, related_name='user_hobby')

    class Meta:
        verbose_name = 'Увлечение'
        verbose_name_plural = 'Увлечения'

    def __str__(self):
        return self.hobby