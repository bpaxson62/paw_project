from django.views import generic
from django.shortcuts import render, get_object_or_404
from poems.models import Writer, Poem, Publication
# Create your views here.

class WriterIndex(generic.ListView):
    template_name = 'writers.html'
    context_object_name = 'writers'

    def get_queryset(self):
        return Writer.objects.all()


def writer_detail(request, writer_slug):
    writer = get_object_or_404(Writer, slug=writer_slug)

    return render(request, 'writer_detail.html', {'writer': writer, })


def writer_publications(request, writer_slug):
    writer = get_object_or_404(Writer, slug=writer_slug)
    publications = Publication.objects.filter(writer=writer).values()

    return render(request, 'writer_publications.html', {'writer': writer, 'publications': publications})


def writer_poems(request, writer_slug):
    writer = get_object_or_404(Writer, slug=writer_slug)
    poems = Poem.objects.filter(writer=writer).values()
    return render(request, 'writer_poems.html', {'writer': writer, 'poems': poems})