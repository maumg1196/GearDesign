"""Design Urls."""
from django.urls import path
from . import views

app_name = 'design'

urlpatterns = [

    # Design Views.
    path(
        '',
        views.FirstView.as_view(),
        name='first'
    ),
    path(
        'create/',
        views.GearCreate.as_view(),
        name='create'
    ),

]
