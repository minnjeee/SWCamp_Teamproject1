from django.urls import path

from . import views

app_name = 'board'

urlpatterns=[
    path("list/<int:pg>", views.list, name='list'),
    path("view/<int:postnum>",views.views, name='view'),
    path("write", views.write),
    path("save", views.save),
    path("modify/<int:postnum>", views.modify),
    path("save2/<int:postnum>", views.save2),
    path("delete/<int:postnum>", views.delete),
]