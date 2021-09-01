#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 10:41:29 2021

@author: alina

Defines URL patterns for users.
"""
from django.urls import path
# from django.contrib.auth import login # removed this line: https://stackoverflow.com/questions/55768131/typeerror-login-got-an-unexpected-keyword-argument-template-name
from django.contrib.auth.views import LoginView

from . import views

app_name = "users" # I added this line!

urlpatterns = [
    # Login page   login is a built-in view, and the dict passes the template to it
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    # Logout page
    path('logout/', views.logout_view, name='logout'),
    # Registration page
    path('register/', views.register, name='register'),
    ]
