from random import randint
from django.shortcuts import render
from poems.models import Related_Link,Video
from poems.models import Writer, Poem

__author__ = 'brian'
from django.http import HttpResponse


def home(request):
    # post random writer and poem on front page
    # writer_index = Writer.objects.count() - 1
    #

    # index1 = randint(0, writer_index)
    # writer = Writer.objects.all().__getitem__(index1)
    # poem_index = writer.poem_set.all().count() - 1
    # index2 = randint(0, poem_index)
    # poem = writer.poem_set.all().__getitem__(index2)
    # writer2 = Writer.objects.all()
    # {'poem': poem, }
    return render(request, 'home.html', {'writer': 'fd', 'poem': 'sd'}, )


def related_links(request):
    links = Related_Link.objects.all()
    return render(request, 'related_links.html', {'links': links}, )


def contact(request):
    return render(request, 'contact.html', {'writer': 'fd', 'poem': 'sd'}, )



def videos(request):
    videos = Video.objects.all()
    # writer = videos.g
    return render(request, 'videos.html', {'videos': videos}, )
