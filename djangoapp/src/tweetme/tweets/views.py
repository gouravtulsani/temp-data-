# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import DetailView, ListView, CreateView
from django.shortcuts import render, get_object_or_404
from .models import tweet
from .forms import tweetmodelform

# Create your views here.


class TweetCreateView(CreateView):
	#queryset = tweet.objects.all()
	form_class = tweetmodelform.meta
	#fields = ['user','content']
	template_name = "tweet/create_view.html"
	success_url = 'tweet'
	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(TweetCreateView, self).form_valid(form)





class TweetDetailView(DetailView):
	queryset = tweet.objects.all()
	def get_object(self):
		pk = self.kwargs.get("pk")
		obj = get_object_or_404(tweet, pk=pk)
		return obj


class TweetListView(ListView):
	queryset=tweet.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super(TweetListView, self).get_context_data(*args, **kwargs)
		return context





















"""

def tweet_detail_view(request, id=1):
	obj = tweet.objects.get(id=id)
	content ={
		"obj_detail" : obj
	}
	return render(request, "detail_view.html",content)


def tweet_list_view(request):
	queryset = tweet.objects.all()
	content = {
		"obj_list" : queryset
	}
	return render(request, "list_view.html", content)


#def tweet_create_view(request, id=1):
#	return render(request, "create_view.html",{})


def tweet_update_view(request, id=1):
	return render(request, "update_view.html",{})

def tweet_delete_view(request, id=1):
	return render(request, "delete_view.html",{})  

"""