from django.urls import path
from All_Users import views
from knox.views import LogoutView


urlpatterns = [
    path('send_otp', views.send_otp.as_view()),
    path('verify_user', views.verify_user.as_view()),
    path('Register', views.Register.as_view()),
    
    path('login', views.LoginAPI.as_view()),
    path('logout', LogoutView.as_view()),
    # path('profile', views.ProfileView.as_view()),
]
  