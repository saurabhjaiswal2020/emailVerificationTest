from django.urls import path
from . import views

app_name = 'first_app'

urlpatterns = [
    path('', views.index, name="index"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('cbview/',views.CBView.as_view()),
]