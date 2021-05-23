"""ssuproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import notice.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',notice.views.home, name="home"),
    path('notice/<int:notice_id>/',notice.views.detail,name="detail"),
    path('notice/new/',notice.views.new,name="new"),
    path('notice/create/',notice.views.create,name="create"),
    path('notice/delete/<int:notice_id>/',notice.views.delete,name="delete"),
    path('notice/edit/<int:notice_id>/',notice.views.edit,name="edit"),
    path('notice/update/<int:notice_id>/',notice.views.update,name="update"),
    path('notice/about/',notice.views.about,name="about"),
]
