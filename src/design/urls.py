"""Design Urls."""
from django.urls import path
from . import views

app_name = 'design'

urlpatterns = [

    # Design Views.
    path(
        '',
        views.FirstView.as_view(),
        name='home'
    ),
    path(
        'second/',
        views.SecondView.as_view(),
        name='home'
    ),

]