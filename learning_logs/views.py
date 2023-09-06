from django.shortcuts import render

from .models import Topic

def index(request):
	"""Home page for the Learning Log app."""
	return render(request, 'learning_logs/index.html')

def topics(request):
	"""View all topics."""
	topics = Topic.objects.order_by('date_added')
	context = {'topics': topics}
	return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
	"""Displays a single topic and all related contents."""
	topic = Topic.objects.get(id=topic_id)
	entries = topic.entry.set.order_by('-date_added')
	context = {'topic': topic, 'entries': entries}
	return render(request, 'learning_logs/topic.html', context)