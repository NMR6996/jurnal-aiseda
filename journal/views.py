from django.shortcuts import render
from journal.models import *


def index(request):
    volumes = Volume.objects.get(is_home=True)
    articles = Article.objects.filter(volumes=volumes)
    context = {
        "volumes": volumes,
        "articles": articles,
        "published": Article.objects.all().count()
    }
    return render(request, "index.html", context)


def volume(request):
    volumes = Volume.objects.all()
    context = {
        "volumes": volumes,
        "published": Article.objects.all().count()
    }
    return render(request, "volumes.html", context)


def volume_details(request, id):
    volume = Volume.objects.get(id=id)
    volume.click_count += 1
    volume.save()
    articles = Article.objects.filter(volumes=volume)
    return render(request, "volume-details.html", {"volume": volume, "articles": articles})
