from django.shortcuts import render
from homepage.models import Content


def homepage(request):
    content = Content.objects.filter(published=True)
    return render(request, 'homepage/index.html', {'content': content})
