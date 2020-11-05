from django.urls import path
from .views import PollCreateView

urlpatterns = [
    path('create_poll/', PollCreateView.as_view(), name='create_poll')
]