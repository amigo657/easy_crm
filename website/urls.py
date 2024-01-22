from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("logout/", views.logout_user, name='logout'),
    path("register/", views.register_user, name='register'),
    path("record/<int:pk>/", views.record, name='record'),
    path("delete_record/<int:pk>/", views.delete_record, name='delete_record'),
    path("update_record/<int:pk>/", views.update_record, name='update_record'),
    path("add_client/", views.add_record, name='add_client'),
    path("history/", include("sales_history.urls")),
]