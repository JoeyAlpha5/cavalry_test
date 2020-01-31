from django.urls import path
from .views import index, chart_data
urlpatterns = [
     path('', index),
     path('chart_data', chart_data),
]