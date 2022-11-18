from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# 캘린더
class Calender(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.name

# 쪽지
class Letter(models.Model):
    calender = models.ForeignKey(Calender, on_delete=models.CASCADE,related_name='letters', null=True, blank=True)
    nickname = models.CharField(max_length=128, blank=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add = True, null=True, blank=True)

    def __str__(self):
        return self.calender