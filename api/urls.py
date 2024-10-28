from django.urls import path

from . import views

urlpatterns = [
    path("", views.create_package_view),
    path("create-package", views.PackageView.as_view()),
]
