from django.urls import path
from .views import PollCreateView, vote

urlpatterns = [
    path('create_poll/', PollCreateView.as_view(), name='create_poll'),
    path('vote/<int:poll_pk>/', vote, name='vote')
]