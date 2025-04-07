from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Destination
from .forms import CreateForm, UserForm
from .Serializer import DestinationSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
import logging

# Configure logging
logger = logging.getLogger(__name__)

class DestinationView(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    permission_classes = [IsAuthenticated]

@login_required
def create_destination(request):
    if request.method == 'POST':
        form = CreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateForm()
    return render(request, 'create_destination.html', {'form': form})

def search_destination(request):
    query = request.GET.get('q')
    destinations = Destination.objects.filter(name__icontains=query) if query else []
    return render(request, 'search_results.html', {'destinations': destinations, 'query': query})

def list_destinations(request):
    destinations = Destination.objects.all()
    return render(request, 'list_destinations.html', {'destinations': destinations})

@login_required
def update_destinations(request, pk):
    destination = Destination.objects.get(pk=pk)
    if request.method == 'POST':
        form = CreateForm(request.POST, request.FILES, instance=destination)
        if form.is_valid():
            form.save()
            return redirect('list_destinations')
    else:
        form = CreateForm(instance=destination)
    return render(request, 'update_destination.html', {'form': form, 'destination': destination})

@login_required
def delete_destination(request, pk):
    destination = Destination.objects.get(pk=pk)
    if request.method == 'POST':
        destination.delete()
        return redirect('list_destinations')
    return render(request, 'delete_destination.html', {'destination': destination})

def destination_detail(request, pk):
    destination = Destination.objects.get(pk=pk)
    return render(request, 'destination_detail.html', {'destination': destination})

def home(request):
    destinations = Destination.objects.all()
    for destination in destinations:
        if not destination.image:
            destination.image_url = None
        else:
            destination.image_url = destination.image.url
    return render(request, 'home.html', {'destinations': destinations})

def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('user_login')
        else:
            # Log form errors for debugging
            logger.error(f"Registration form errors: {form.errors}")
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            logger.warning(f"Login form is invalid. Errors: {form.errors}")
            logger.debug(f"Username: {request.POST.get('username')}, Password: {request.POST.get('password')}")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('user_login')

