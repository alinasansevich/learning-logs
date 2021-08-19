#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 13:36:10 2021

@author: alina
"""

from django import forms
from .models import Entry, Topic


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'blablabla'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
