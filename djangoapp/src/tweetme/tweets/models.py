# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#from django.core.exceptions import ValidationError
from django.db import models
from django.conf import settings

# Create your models here.




class tweet(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1) #user
	content = models.CharField(max_length=120)
	update = models.DateTimeField(auto_now = True)
	timestamp = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return (str(self.content))