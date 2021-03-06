"""gcp_adaptor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from adaptor import views, models
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tenant', views.TenantViewSet)
router.register(r'apf', views.ApfViewSet)
router.register(r'attribute', views.AttributeViewSet)
router.register(r'operator', views.OperatorViewSet)
router.register(r'value', views.ValueViewSet)
router.register(r'hierarchy', views.HierarchyViewSet)
router.register(r'attribute_mapping', views.AttributeMappingViewSet)
router.register(r'operator_mapping', views.OperatorMappingViewSet)
router.register(r'value_mapping', views.ValueMappingViewSet)

urlpatterns = [
    url(r'^policy2dnf/', views.AdaptorDnfView.as_view(), name='my_rest_view'),
    url(r'^policy2local/', views.AdaptorLocalView.as_view(), name='my_rest_view'),
    url(r'^', include(router.urls)),
]
