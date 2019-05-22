"""Design Urls."""
from django.urls import path
from . import views

app_name = 'design'

urlpatterns = [

    # CSM Views.
    path(
        '',
        views.HomeView.as_view(),
        name='home'
    ),

]
