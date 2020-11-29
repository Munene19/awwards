from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from .models import Profile,Project,Comment
from .forms import NewProfileForm,NewProjectForm,VoteForm,NewCommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializer
from rest_framework import status
from django.db.models import Max,F

# Create your views here.

@login_required(login_url='/accounts/login/')
def welcome(request):
    current_user = request.user
    user_profile= Profile.objects.filter(user=current_user.id).first()
    comment= Comment.objects.filter(user=current_user.id).first()
    projects = Project.objects.all()
    average=0

    for project in projects:
        average=(project.design + project.usability + project.content)/3
        rating = round(average,2)
    return render(request, 'users/index.html', {'user_profile':user_profile, 'projects':projects,'comment':comment})


@login_required(login_url='/accounts/login/')
def user_profile(request):
    current_user = request.user
    projects = Project.objects.filter(user=current_user).all()
    user_profile = Profile.objects.filter(user=current_user.id).first()
    

    return render(request, 'users/user_profile.html', { 'user_profile':user_profile,'projects':projects})


@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user = request.user
    
    if request.method == 'POST':
        form=NewProfileForm(request.POST, request.FILES)

        if form.is_valid():
            profile=form.save(commit=False)
            profile.user = current_user
            profile.save()

            return redirect('user-profile')

    else:
            form=NewProfileForm()

    return render(request, 'users/edit_profile.html', {'form':form,})

@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
  
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()

        return redirect ("welcome")

    else:
        form = NewProjectForm()

    return render(request, 'users/new_project.html', {"form": form})