from django.urls import path,include
from . import views

urlpatterns = [
    path('/<int:_id>/',views.detail,name="detail"),
    path('/new/',views.new,name="new"),
    path('/create/',views.create,name="create"),
    path('/delete/<int:_id>/',views.delete,name="delete"),
    path('/edit/<int:_id>/',views.edit,name="edit"),
    path('/update/<int:_id>/',views.update,name="update"),
    path('/about/',views.about,name="about"),
]
