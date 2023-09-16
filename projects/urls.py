from django.urls import path
from .views import ProjectsAPI
urlpatterns = [
    path('', ProjectsAPI.as_view())
]
