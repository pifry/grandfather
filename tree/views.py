from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from .models import Person
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def index(request):
	context = { 'person_list': Person.objects.all() }
	return render(request, 'tree/index.html', context)

def detail(request, person_id):
	person = get_object_or_404(Person, pk=person_id)
	return render(request, 'tree/detail.html', { 'person': person })