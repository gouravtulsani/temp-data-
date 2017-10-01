from django import forms
from .models import tweet


class tweetmodelform(forms.ModelForm):
	class meta:
		model = tweet
		fields =[
			"content"
			]


	