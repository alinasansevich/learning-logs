#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 10:59:38 2021

@author: alina

Defines URL patterns for learning_logs.
"""
from django.urls import path

#from django.conf.urls import url
from . import views   # the dot tells Python to import views from the same directory as the current urls.py module.

# The variable urlpatterns in this module is a list of individual pages 
# that can be requested from the learning_logs app
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    ]
