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

# https://stackoverflow.com/questions/41883254/django-is-not-a-registered-namespace
app_name = "learning_logs" # I added this line!


# The variable urlpatterns in this module is a list of individual pages 
# that can be requested from the learning_logs app
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    ]
# when the requested URL string matches the first argument,
# path calls the function it received in the second argument,
# and the third argument provides a name for this URL pattern,
# so we can refer to it in other sections of the code --> to provide a link to
# the home page, use this name instead of writing out a URL.
