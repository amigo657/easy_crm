from django.urls import path
from . import views

urlpatterns = [
    path("", views.view_history, name='view_history'),
    path("history/<int:pk>/", views.history_item, name='history_item'),
    path("delete_item/<int:pk>/", views.delete_item, name='delete_item'),
    path("update_item/<int:pk>/", views.update_item, name='update_item'),
    path("add_item/", views.add_item, name='add_item'),
]