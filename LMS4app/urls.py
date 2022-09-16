from django.urls import path
from .views import RegisterAPIView,AuthenticateUserAPIView

urlpatterns = [
  path('register/',RegisterAPIView.as_view(),name="register") ,
  path('login/',AuthenticateUserAPIView.as_view(),name="login") ,
  
]