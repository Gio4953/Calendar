from django.urls import path
from . import views

urlpatterns = [
    path('<int:year>/<int:month>/<int:number>/', views.calendar1_view, name='calendar1_view'),
]
