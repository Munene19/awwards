from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from tinymce.models import HTMLField
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.welcome, name='welcome' ),
    path('profile/', views.user_profile, name='user-profile'),
    path('edit/profile', views.edit_profile, name="edit-profile"),
    path('new/project',views.new_project, name ='new-project'),
    path('api/profile/', views.ProfileList.as_view(), name='profile-API'),
    path('api/project/', views.ProjectList.as_view(), name='project-API'),
    path('search/', views.search_results, name='search_results'),
    path('vote/(?P<id>\d+)', views.rating,name='rating'),
    path('newcomment/(\d+)/', views.new_comment, name='new-comment'),
    

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)