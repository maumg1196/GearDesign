"""Users Urls."""
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

]
