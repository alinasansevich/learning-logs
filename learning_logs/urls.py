#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 10:59:38 2021

@author: alina

Defines URL patterns for learning_logs.
"""
from django.urls import path
# from django.conf.urls import url --> this is from older Django versions
from . import views   # the dot tells Python to import views from the same directory as the current urls.py module.

from django.conf import settings
from django.conf.urls.static import static

# https://stackoverflow.com/questions/41883254/django-is-not-a-registered-namespace
app_name = "learning_logs" # I added this line!


# The variable urlpatterns in this module is a list of individual pages 
# that can be requested from the learning_logs app
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Show all topics
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic
    path('<int:topic_id>/', views.topic, name='topic'),
    # Page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding a new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page for editing an entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    # Add static files
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# when the requested URL string matches the first argument,
# path calls the function it received in the second argument,
# and the third argument provides a name for this URL pattern,
# so we can refer to it in other sections of the code --> to provide a link to
# the home page, use this name instead of writing out a URL.
