from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    """home page traffic is handled here"""
    return HttpResponse("<h1>Blog Home</h1>")


def about(request):
    """about page traffic is handled here"""
    return HttpResponse("<h1>Blog About</h1>")
