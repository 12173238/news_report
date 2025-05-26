"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from myapp import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/project_wra_report/', permanent=True)),

    path("project_wra_report/", views.project_wra_report, name="project_wra_report"),
    path("ai_report/", views.ai_report, name='ai_report'),
    path('train/', views.train_view, name='train_view'),
    path('test-api/', views.test_groq_api, name='test_groq_api'),
    path('generate/', views.generate_view, name='generate_view'),
    path('upload_file/', views.upload_file, name='upload_file'),

]
