from .views import index, by_rubric
from django.urls import path

urlpatterns = [
    path('<int:rubric_id>/', by_rubric),
    path('', index),
]