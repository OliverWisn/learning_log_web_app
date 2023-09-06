"""Defines URL patterns for learning_logs."""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
	# Home.
	path('', views.index, name='index'),
	# View all topics.
	path('topics/', views.topics, name='topics'),
	# Detail page for a single topic.
	path('topics/(<int:topic_id>)/', views.topic, name='topic'),
]