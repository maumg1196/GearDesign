"""Users Urls."""
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [

    # Users Views.
    path(
        'signup/',
        views.signup,
        name='signup'
    ),
    path(
        'logout/',
        views.logout_view,
        name='logout'
    ),
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='users/login.html'
        )
    ),

]
