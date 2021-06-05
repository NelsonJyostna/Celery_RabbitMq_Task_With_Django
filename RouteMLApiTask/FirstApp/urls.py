
from django.urls import path
from . import views


urlpatterns = [

    path('std/', views.StudentAPI.as_view() ),

    path('std/<int:pk>/', views.StudentAPI.as_view() )
]

