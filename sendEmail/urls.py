from django.urls import path
from sendEmail import views


urlpatterns = [
    path('send', views.EmailView.as_view(), name='send-email'),
]
  