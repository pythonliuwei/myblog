from django.urls import path
from blog_admin import views

urlpatterns = [
    path("", views.RegisterView.as_view(),name='register'),
]
