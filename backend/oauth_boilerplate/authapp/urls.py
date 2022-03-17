from django.urls import path
from .views import RestrictedAccessView, LoginView, RedirectView, TestTokenView, GenerateTokenView, ValidateTokenView, logout_view


urlpatterns = [
    path('login/<str:provider>', LoginView.as_view()),
    path('redirect/<str:provider>', RedirectView.as_view()),
    path('logout/', logout_view), 
    path('generate_token', GenerateTokenView.as_view()),
    path('validate/', ValidateTokenView.as_view()),
        
    path('access/', RestrictedAccessView.as_view()),
    path('test/', TestTokenView.as_view()),
    ]
