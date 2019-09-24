"""python_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from django.views.generic import TemplateView

from rest_framework.routers import DefaultRouter

from python_test.views import ClientCreateView, ClientEditView, ClientListView, ClientViewSet


router = DefaultRouter()
router.register(r'client', ClientViewSet)

urlpatterns = [
	path('', TemplateView.as_view(template_name="home.html")),
    path('admin/', admin.site.urls),
    path('add-client', ClientCreateView.as_view(), name="add_client_view"),
    path('edit-client/<int:pk>/', ClientEditView.as_view(), name="edit_client_view"),
    path('list-client/', ClientListView.as_view(), name="list_client_view"),
    path('api/', include(router.urls))

]
