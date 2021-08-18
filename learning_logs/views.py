from django.shortcuts import render
from .models import Topic


def index(request):
    """The home page for Learning Log."""
    
    return render(request, 'learning_logs/index.html') # render takes the request as first argument, and a template it uses to build the page.


def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added') # &*&*&
    context = {'topics': topics} # this dict contains the data needed to build the webpage with the template
    return render(request, 'learning_logs/topics.html', context)
# &*&*&
# in this line, we query the database by asking for the Topic objects,
# sorted by the date_added attribute. We store the resulting queryset in topics.