# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .forms import tweetmodelform
# Register your models here.
from .models import tweet

class tweetmodeladmin(admin.ModelAdmin):
	#form = tweetmodelform
	class meta:
		 model = tweet
	


admin.site.register(tweet, tweetmodeladmin)