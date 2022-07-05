from django.urls import path

from .views import RegistrationAPIView, LoginAPIView, CustomUserRetrieveUpdateAPIView, RefreshView


app_name = 'authorization'
urlpatterns = [
    path('registration/', RegistrationAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('user/', CustomUserRetrieveUpdateAPIView.as_view()),
    path('refresh/', RefreshView.as_view())
]