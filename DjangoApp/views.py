from django.shortcuts import render
from . models import Member

def index(request):
    all_members = Member.objects.all()
    return render (request, 'index.html', {
        'members':all_members
    })