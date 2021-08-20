from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
 
from .models import Entry, Topic
from .forms import EntryForm, TopicForm


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


def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id) # this is  a query
    entries = topic.entry_set.order_by('-date_added') # '-date_added' the '-' in front of 'date_added' sorts the results in reverse order --> it will display the most recent entries first
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = EntryForm()
    else:
        # POST data submitted; process data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))
    
    context = {'topic': topic,
               'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry) # instance=entry --> this will display previous entries
    else:
        # POST data submitted; process data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',
                                                args=[topic.id])) # redirect to the topic page, the user should see the updated version of the entry they edited
    context = {'entry': entry,
               'topic': topic,
               'form': form,}
    return render(request, 'learning_logs/edit_entry.html', context)












            










