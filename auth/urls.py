"""auth URL Configuration

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
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from users.views import BookList, BookDetail
schema_view = get_schema_view(
   openapi.Info(
      title="API Documentations",
      default_version='v1',
      description="PythonDjangoTask",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="shindeankita111@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api/view',BookList.as_view()),
    path('api/adds/<int:pk>',BookDetail.as_view()),
    path('admin/', admin.site.urls),

    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]