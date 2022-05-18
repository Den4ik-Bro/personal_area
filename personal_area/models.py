from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Skills(models.Model):
    skill = models.CharField(max_length=50, verbose_name='навык')
    user = models.ManyToManyField(User, related_name='skills', verbose_name='навыки', blank=True, null=True)

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'

    def __str__(self):
        return self.skill
