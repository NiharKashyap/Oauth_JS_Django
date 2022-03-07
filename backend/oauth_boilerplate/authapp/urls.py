from django.urls import path
# from .views import GoogleView, GoogleRedirectView, RestrictedAccessView, FBLoginView, FBRedirectView, DiscordLoginView, DiscordRedirectView, LoginView, RedirectView

from .views import RestrictedAccessView, LoginView, RedirectView, TestTokenView, GetTokenView, logout_view, test_db, get_code


urlpatterns = [
    path('login/<str:provider>', LoginView.as_view()),
    path('logout/', logout_view),
    path('test_db/', test_db),
    path('get_token', GetTokenView.as_view()),
    path('redirect/<str:provider>', RedirectView.as_view()),
    path('access/', RestrictedAccessView.as_view()),
    path('test/', TestTokenView.as_view()),
    path('getCode/', get_code)
]
