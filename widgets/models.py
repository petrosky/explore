from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Widget(models.Model):

	name = models.CharField(max_length=30)
	desc = models.TextField(max_length=200)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.name
