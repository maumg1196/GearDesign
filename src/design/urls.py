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
        '<int:user_id>/',
        views.UserDetail.as_view(),
        name='user'
    ),
    path(
        '<int:user_id>/<int:gear_id>/',
        views.GearDetail.as_view(),
        name='gear'
    ),
    path(
        'create/',
        views.GearCreate.as_view(),
        name='create'
    ),
    path(
        'create/<int:gear_id>/',
        views.SecondView.as_view(),
        name='continue'
    ),
    path(
        'create/<int:gear_id>/final/',
        views.FinalUpdate.as_view(),
        name='final'
    ),

]
