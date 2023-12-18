from django.urls import path

from . import views

urlpatterns=[
    path("server1", views.server1),
    path("server2", views.server2),
    path("server3", views.server3),
    path("server4", views.server4),
    path("server5", views.server5),
    path("server6", views.server6),
    path("server7", views.server7),
    path("detail/<int:id>", views.detail)
]